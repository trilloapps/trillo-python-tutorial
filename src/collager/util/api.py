from typing import Callable
from enum import Enum
from functools import wraps

class HttpMethod(Enum):
    POST = "post"
    GET = "get"
    PUT = "put"
    DELETE = "delete"

class Api:
    def __init__(self, httpMethod: HttpMethod = HttpMethod.POST):
        self.httpMethod = httpMethod

    def __call__(self, func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        wrapper.httpMethod = self.httpMethod
        return wrapper
