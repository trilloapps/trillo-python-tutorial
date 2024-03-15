from typing import List, Any, Dict

from src.collager.model.DataRequest import DataRequest
from src.collager.model.DataResult import DataResult
from src.collager.model.Exp import Exp
from src.collager.pojo.ResultApi import Result
from src.collager.util import DSApi
from src.collager.util.BaseApi import BaseApi
from src.collager.util.CoreDSUtil import CoreDSUtil
from src.collager.util.LogPy import Log
from src.collager.util.Util import Util


class DataIterator:

    def __init__(self,  *args: Any):
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

        if len(args) == 1:
            self.__init_1__(args[0])
        if len(args) == 2:
            self.__init_5__(args[0], args[1])
        elif len(args) == 3:
            if isinstance(args[0], int) and isinstance(args[1], int):
                self.__init_6__(args[0], args[1], args[2])
            elif isinstance(args[0], str) and isinstance(args[1], int):
                self.__init_2__(args[0], args[1], args[2])
            else :
                self.__init_3__(args[0], args[1], args[2])
        elif len(args) == 4:
            self.__init_4__(args[0], args[1], args[2], args[3], args[4])
        elif len(args) == 1 and isinstance(args[0], int):
            self.__init_5__(args[0], args[1])
        elif len(args) == 3 and isinstance(args[0], int):
            self.__init_6__(args[0], args[1], args[2])
        elif len(args) == 5 and isinstance(args[0], int):
            self.__init_7__(args[0], args[1], args[2], args[3], args[4])

    def __init_1__(self, className: str):
        self.__init_4__(className, Exp(), None, 1, 10)

    def __init_2__(self, className: str, start: int, pageSize: int):
        self.__init_4__(className, Exp(), None, start, pageSize)

    def __init_3__(self, className: str, where: str, orderBy: str):
        self.__init_4__(className, where, orderBy, 1, 10)

    def __init_4__(self, className: str, where: str, orderBy: str, start: int, pageSize: int):
        self.dataRequest = DataRequest()
        self.dataRequest.setClassName(className)
        self.dataRequest.setWhere(where)
        self.dataRequest.setOrderBy(orderBy)
        self.dataRequest.setStart(start)
        self.dataRequest.setSize(pageSize)
        self.dataRequest.setUsingRowLimits(True)
        self.dataRequest.setAppName(BaseApi.app(className))
        self.dataRequest.setDsName(BaseApi.ds(className))
        self.dataRequest.setClassName(BaseApi.cls(className))

    def __init_5__(self, start: int, pageSize: int):
        self.__init_6__(start, pageSize, "")

    def __init_6__(self, start: int, pageSize: int, sqlQuery: str):
        self.dataRequest = DataRequest()
        self.dataRequest.setSql(sqlQuery)
        self.dataRequest.setStart(start)
        self.dataRequest.setSize(pageSize)
        self.dataRequest.setUsingRowLimits(True)

    def __init_7__(self, appName: str, dsName: str, start: int, pageSize: int, sqlQuery: str):
        self.dataRequest = DataRequest()
        self.dataRequest.setAppName(appName)
        self.dataRequest.setDsName(dsName)
        self.dataRequest.setSql(sqlQuery)
        self.dataRequest.setStart(start)
        self.dataRequest.setSize(pageSize)
        self.dataRequest.setUsingRowLimits(True)

    def getAppName(self) -> str:
        return self.dataRequest.getAppName()

    def setAppName(self, appName: str) -> None:
        self.dataRequest.setAppName(appName)

    def getDsName(self) -> str:
        return self.dataRequest.getDsName()

    def setDsName(self, dsName: str) -> None:
        self.dataRequest.setDsName(dsName)

    def getDsType(self) -> str:
        return self.dsType

    def setDsType(self, dsType: str) -> None:
        self.dsType = dsType

    def getDataRequest(self) -> DataRequest:
        return self.dataRequest

    def getDataResult(self) -> DataResult:
        return self.dataResult

    def getResult(self) -> Any:
        return self.result

    def hasError(self) -> Any:
        return self.errored

    def getMessage(self) -> Any:
        return self.message

    def getIndex(self) -> int:
        return self.index

    def initialize(self) -> Result:
        if self.iteratorEnded:
            return Result.getFailedResult("DataIterator has ended")
        if self.dataResult is None:
            self.fetch()
        if self.errored:
            return Result.getFailedResult(self.message)
        return Result.getSuccessResult()

    def getNext(self) -> Any:
        if self.iteratorEnded:
            return None
        else:
            if self.dataResult is None:
                self.fetch()
                if self.iteratorEnded:
                    return None
            obj = self.dataResult.getItems()[self.index]
            self.lastId = obj.get(self.idAttrName)
            self.index += 1
            if self.index >= len(self.dataResult.getItems()):
                self.nextStart = self.dataRequest.getStart() + len(self.dataResult.getItems())
                self.dataResult = None
            return obj

    def fetch(self) -> None:
        if self.noMorePage:
            self.iteratorEnded = True
            return
        if self.firstPage:
            self.firstPage = False
            if self.originalQuery is not None and self.orderById:
                self.dataRequest.setUsingRowLimits(False)
                self.dataRequest.setSql(CoreDSUtil.updateLimitClause(self.originalQuery + " order by " + self.idAttrName, 0, self.dataRequest.getSize(), self.dsType))
            self.dataResult = self.retrievePage()
            self.index = 0
        else:
            if self.originalQuery is not None and self.orderById:
                if self.lastId is not None:
                    self.dataRequest.setUsingRowLimits(False)
                    query = self.originalQuery.lower().index(" where ") > 0 and (self.originalQuery + " and (" + self.idAttrName + " > " + str(self.lastId) + ")") or (self.originalQuery + " where " + self.idAttrName + " > " + str(self.lastId))
                    self.dataRequest.setSql(CoreDSUtil.updateLimitClause(query + " order by " + self.idAttrName, 0, self.dataRequest.getSize(), self.dsType))
                else:
                    self.dataRequest.setStart(self.dataRequest.getStart() + len(self.dataResult.getItems()))
                    self.dataRequest.setSql(self.originalQuery + " order by " + self.idAttrName)
            else:
                self.dataRequest.setStart(self.nextStart)
            self.dataResult = self.retrievePage()
            self.index = 0
        if self.dataResult is None or len(self.dataResult.getItems()) == 0:
            self.noMorePage = True
            self.iteratorEnded = True

    def getPage(self) -> List[Dict[str, Any]]:
        if self.dataResult is not None:
            l = self.dataResult.getItemsAsListOfMaps()
            self.index = len(l)
            self.nextStart = self.dataRequest.getStart() + len(self.dataResult.getItems())
            self.dataResult = None
            return l
        if self.noMorePage:
            return None
        self.fetch()
        if self.noMorePage:
            return None
        else:
            l = self.dataResult.getItemsAsListOfMaps()
            self.index = len(l)
            self.nextStart = self.dataRequest.getStart() + len(self.dataResult.getItems())
            self.dataResult = None
            return l

    def hasPage(self) -> bool:
        if self.noMorePage:
            return False
        if self.dataResult is None:
            self.fetch()
        return not self.iteratorEnded

    def hasNext(self) -> bool:
        if self.iteratorEnded:
            return False
        if self.dataResult is None:
            self.fetch()
        return not self.iteratorEnded

    def retrievePage(self) -> DataResult:
        if self.totalItems == -1:
            self.dataRequest.setCountQuery(self.countQuery)
        res = DSApi.getPage(vars(self.dataRequest))
        self.dataRequest.setCountQuery(None)
        m = None
        if isinstance(res, Result):
            self.result = res
            r = res
            self.errored = r.isFailed()
            self.message = r.getMessage()
            Log.error("Failed to retrieve page, error: " + r.getMessage())
            return None
        if isinstance(res, dict):
            m = res
        if m is None or (m.get("_rtag") and "_r_" == str(m.get("_rtag"))):
            if m is not None:
                self.result = m
                self.errored = "true" == str(m.get("failed"))
                self.message = str(m.get("message"))
                Log.error("Failed to retrieve data, error message: " + (res).getMessage())
            self.noMorePage = True
            self.iteratorEnded = True
            return None
        dataResult = DataResult(m)
        if self.totalItems == -1:
            self.totalItems = dataResult.getTotalItems()
        if len(dataResult.getItems()) < self.dataRequest.getSize():
            self.noMorePage = True
        return dataResult

    def getTotalItems(self) -> int:
        if self.totalItems != -1:
            return self.totalItems
        if self.iteratorEnded:
            return self.totalItems
        if self.dataResult is None:
            self.fetch()
        return self.totalItems

    def getCountQuery(self) -> str:
        return self.countQuery

    def setCountQuery(self, countQuery: str) -> None:
        self.countQuery = countQuery
