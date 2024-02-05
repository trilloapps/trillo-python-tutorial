from typing import List, Dict

class DataResult:
    def __init__(self):
        self.items = None
        self.totalItems = 0
        self.start = 0

    def getItems(self) -> List[object]:
        return self.items

    def setItems(self, items: List[object]):
        self.items = items

    def getTotalItems(self) -> int:
        return self.totalItems

    def setTotalItems(self, totalItems: int):
        self.totalItems = totalItems

    def getStart(self) -> int:
        return self.start

    def setStart(self, start: int):
        self.start = start

    def is_paginated_(self) -> bool:
        return True

    def getItemsAsListOfMaps(self) -> List[Dict[str, object]]:
        l = []
        if self.items is None:
            return None

        for item in self.items:
            l.append(dict(item))

        return l
