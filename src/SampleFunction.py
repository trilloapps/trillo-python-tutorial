from src.collager.util.api import Api


@Api(httpMethod="post")
def postMethodChangeMe(parameters):
   return parameters


@Api(httpMethod="get")
def getMethodChangeMe(parameters):
   return parameters


@Api(httpMethod="put")
def putMethodChangeMe(parameters):
   return parameters


@Api(httpMethod="delete")
def deleteMethodChangeMe(parameters):
   return parameters
