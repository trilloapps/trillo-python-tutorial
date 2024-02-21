from typing import List, Union, Optional
from dataclasses import dataclass

from src.collager.model.DataRequest import DataRequest
from src.collager.model.DataResult import DataResult
from src.collager.pojo.ResultApi import Result
from src.collager.util.Util import Util
from src.collager.util import DSApi
from src.collager.util.CoreDSUtil import CoreDSUtil
from src.collager.util.LogApi import Log


class DataIterator:
    def __init__(self, className, *args, **kwargs):
        self.dataRequest = None
        self.dataResult = None
        self.result = None
        self.index = 0
        self.iteratorEnded = False
        self.noMorePage = False
        self.orderById = False
        self.originalQuery = None
        self.lastId = None
        self.idAttrName = "id"
        self.dsType = CoreDSUtil.MYSQL
        self.firstPage = True
        self.nextStart = 1
        self.countQuery = None
        self.totalItems = -1
        self.errored = False
        self.message = None

        if args or kwargs:
            self.dataRequest = DataRequest(className, *args, **kwargs)
        else:
            self.dataRequest = DataRequest(className)

    def getAppName(self):
        return self.dataRequest.appName

    def setAppName(self, appName):
        self.dataRequest.appName = appName

    def getDsName(self):
        return self.dataRequest.dsName

    def setDsName(self, dsName):
        self.dataRequest.dsName = dsName

    def getDsType(self):
        return self.dsType

    def setDsType(self, dsType):
        self.dsType = dsType

    def getDataRequest(self):
        return self.dataRequest

    def getDataResult(self):
        return self.dataResult

    def getResult(self):
        return self.result

    def hasError(self):
        return self.errored

    def getMessage(self):
        return self.message

    def getIndex(self):
        return self.index

    def initialize(self):
        if self.iteratorEnded:
            return Result.getFailedResult("DataIterator has ended")
        if self.dataResult is None:
            self.fetch()

        if self.errored:
            return Result.getFailedResult(self.message)

        return Result.getSuccessResult()

    def getNext(self):
        if self.iteratorEnded:
            return None
        else:
            if self.dataResult is None:
                self.fetch()
                if self.iteratorEnded:
                    return None
            obj = self.dataResult.items[self.index]
            self.lastId = obj.get(self.idAttrName)
            self.index += 1
            if self.index >= len(self.dataResult.items):
                self.nextStart = self.dataRequest.start + len(self.dataResult.items)
                self.dataResult = None
            return obj

    def fetch(self):
        if self.noMorePage:
            self.iteratorEnded = True
            return

        if self.firstPage:
            self.firstPage = False
            if self.originalQuery and self.orderById:
                self.dataRequest.usingRowLimits = False
                self.dataRequest.sql = CoreDSUtil.updateLimitClause(
                    f"{self.originalQuery} order by {self.idAttrName}", 0, self.dataRequest.size, self.dsType
                )
            self.dataResult = self.retrievePage()
            self.index = 0
        else:
            if self.originalQuery and self.orderById:
                if self.lastId:
                    self.dataRequest.usingRowLimits = False
                    query = (
                        f"{self.originalQuery} and ({self.idAttrName} > {self.lastId})"
                        if " where " in self.originalQuery.lower()
                        else f"{self.originalQuery} where {self.idAttrName} > {self.lastId}"
                    )
                    self.dataRequest.sql = CoreDSUtil.updateLimitClause(
                        f"{query} order by {self.idAttrName}", 0, self.dataRequest.size, self.dsType
                    )
                else:
                    self.dataRequest.start += len(self.dataResult.items)
                    self.dataRequest.sql = f"{self.originalQuery} order by {self.idAttrName}"
            else:
                self.dataRequest.start = self.nextStart
            self.dataResult = self.retrievePage()
            self.index = 0

        if self.dataResult is None or not self.dataResult.items:
            self.noMorePage = True
            self.iteratorEnded = True

    def getPage(self):
        if self.dataResult:
            items = self.dataResult.items
            self.index = len(items)
            self.nextStart = self.dataRequest.start + len(items)
            self.dataResult = None
            return items
        if self.noMorePage:
            return None
        self.fetch()
        if self.noMorePage:
            return None
        items = self.dataResult.items
        self.index = len(items)
        self.nextStart = self.dataRequest.start + len(items)
        self.dataResult = None
        return items

    def hasPage(self):
        if self.noMorePage:
            return False
        if self.dataResult is None:
            self.fetch()
        return not self.iteratorEnded

    def hasNext(self):
        if self.iteratorEnded:
            return False
        if self.dataResult is None:
            self.fetch()
        return not self.iteratorEnded

    def retrievePage(self):
        if self.totalItems == -1:
            self.dataRequest.countQuery = self.countQuery
        res = DSApi.getPage(vars(self.dataRequest))
        self.dataRequest.countQuery = None
        m = None
        if isinstance(res, Result):
            self.result = res
            r = res
            self.errored = r.isFailed()
            self.message = r.getMessage()
            Log.error(f"Failed to retrieve page, error: {r.getMessage()}")
            return None
        if isinstance(res, dict):
            m = res
        if m is None or (m.get("_rtag") and "_r_" == str(m.get("_rtag"))):
            if m:
                self.result = m
                self.errored = m.get("failed") == "true"
                self.message = m.get("message")
                Log.error(f"Failed to retrieve data, error message: {res.getMessage()}")
            self.noMorePage = True
            self.iteratorEnded = True
            return None

        data_result = DataResult(items=Util.fromMap(m, List[dict]), totalItems=self.totalItems)
        if self.totalItems == -1:
            self.totalItems = data_result.totalItems
        if len(data_result.items) < self.dataRequest.size:
            self.noMorePage = True
        return data_result

    def getTotalItems(self):
        if self.totalItems != -1:
            return self.totalItems
        if self.iteratorEnded:
            return self.totalItems
        if self.dataResult is None:
            self.fetch()
        return self.totalItems

    def getCountQuery(self):
        return self.countQuery

    def setCountQuery(self, countQuery):
        self.countQuery = countQuery
