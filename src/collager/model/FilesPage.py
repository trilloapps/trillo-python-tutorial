from typing import List, Optional, Dict


class FilesPage:
    def __init__(self):
        self.files: Optional[List[Dict[str, object]]] = None
        self.nextPageToken: Optional[str] = None

    def getFiles(self) -> Optional[List[Dict[str, object]]]:
        return self.files

    def setFiles(self, files: Optional[List[Dict[str, object]]]) -> None:
        self.files = files

    def getNextPageToken(self) -> Optional[str]:
        return self.nextPageToken

    def setNextPageToken(self, nextPageToken: Optional[str]) -> None:
        self.nextPageToken = nextPageToken
