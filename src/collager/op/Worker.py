from typing import Dict, Any, Callable
from src.collager.pojo.ResultApi import Result


class Worker:
    def perform(self, params: Dict[str, Any]) -> Result:
        pass
