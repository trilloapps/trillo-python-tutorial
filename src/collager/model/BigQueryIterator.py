from typing import List, Any

from src.collager.pojo.ResultApi import Result
from src.collager.util import BigQueryApi, Util


class BigQueryIterator:

    def __init__(self, serviceName: str = "", query: str = "", start: int = 1, size: int = 10):
        self.serviceName = serviceName if serviceName else Util.GCP_SSERVICE_NAME
        self.query = query
        self.start = start
        self.size = size
        self.iteratorEnded = False
        self.noMorePage = False
        self.result = None
        self.listIterator = None
        self.page = None

    def retrievePage(self) -> None:
        try:
            self.page = self.getBQPage()
            self.listIterator = None  # set iterator to None so it can be initialized from the page
        except Exception as exc:
            self.page = None
            self.result = Result.getFailedResult("Failed to query page, error: " + str(exc))

    def getPage(self) -> Any:
        if self.noMorePage:
            return None

        self.retrievePage()

        if self.page is None:
            self.noMorePage = True
            self.iteratorEnded = True
            return self.result

        if len(self.page) < self.size:
            self.noMorePage = True

        return self.page

    def fetch(self) -> None:
        if self.noMorePage:
            # if no more pages, end the iterator
            self.iteratorEnded = True
            return

        self.retrievePage()
        if self.page is None:
            self.noMorePage = True
            self.iteratorEnded = True
            return

        self.listIterator = iter(self.page)
        if not self.listIterator.__length_hint__():
            self.noMorePage = True
            self.iteratorEnded = True

    def getNext(self) -> Any:
        if self.iteratorEnded:
            return None
        else:
            if self.listIterator is None or not self.listIterator.__length_hint__():
                self.fetch()
                if self.iteratorEnded:
                    return None
            return next(self.listIterator, None)

    def hasNext(self) -> bool:
        if self.listIterator is None:
            self.fetch()
        return not self.iteratorEnded

    def hasNextPage(self) -> bool:
        if self.listIterator is None:
            self.fetch()
        return not self.iteratorEnded

    def getResult(self) -> Any:
        return self.result

    def getBQPage(self) -> List[Any]:
        return BigQueryApi.getPage(self.query, self.start, self.size)
