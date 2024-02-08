class ApiSpec:
    def __init__(self):
        self.impl = None
        self.cls = None
        self.filter = None
        self.orderBy = None
        self.query = None
        self.options = None
        self.body = None
        self.serviceUrl = None
        self.method = None
        self.querySchema = None
        self.headers = None
        self.bodySchema = None
        self.outputSchema = None
        self.testBody = None
        self.testQuery = None
        self.bodyMapping = None
        self.queryMapping = None
        self.bodyParamName = None
        self.bodyMappingScript = None
        self.outputMappingScript = None
        self.uid = None

    def getImpl(self):
        return self.impl

    def setImpl(self, impl):
        self.impl = impl

    def getCls(self):
        return self.cls

    def setCls(self, cls):
        self.cls = cls

    def getFilter(self):
        return self.filter

    def setFilter(self, filter):
        self.filter = filter

    def getOrderBy(self):
        return self.orderBy

    def setOrderBy(self, orderBy):
        self.orderBy = orderBy

    def getServiceUrl(self):
        return self.serviceUrl

    def setServiceUrl(self, serviceUrl):
        self.serviceUrl = serviceUrl
        self.uid = serviceUrl

    def getOptions(self):
        return self.options

    def setOptions(self, options):
        self.options = options

    def getQuery(self):
        return self.query

    def setQuery(self, query):
        self.query = query

    def getBody(self):
        return self.body

    def setBody(self, body):
        self.body = body

    def getHeaders(self):
        return self.headers

    def setHeaders(self, headers):
        self.headers = headers

    def getMethod(self):
        return self.method

    def setMethod(self, method):
        self.method = method

    def getBodySchema(self):
        return self.bodySchema

    def setBodySchema(self, bodySchema):
        self.bodySchema = bodySchema

    def getOutputSchema(self):
        return self.outputSchema

    def setOutputSchema(self, outputSchema):
        self.outputSchema = outputSchema

    def getQuerySchema(self):
        return self.querySchema

    def setQuerySchema(self, querySchema):
        self.querySchema = querySchema

    def getTestBody(self):
        return self.testBody

    def setTestBody(self, testBody):
        self.testBody = testBody

    def getTestQuery(self):
        return self.testQuery

    def setTestQuery(self, testQuery):
        self.testQuery = testQuery

    def getBodyMapping(self):
        return self.bodyMapping

    def setBodyMapping(self, bodyMapping):
        self.bodyMapping = bodyMapping

    def getQueryMapping(self):
        return self.queryMapping

    def setQueryMapping(self, queryMapping):
        self.queryMapping = queryMapping

    def getBodyParamName(self):
        return self.bodyParamName

    def setBodyParamName(self, bodyParamName):
        self.bodyParamName = bodyParamName

    def getBodyMappingScript(self):
        return self.bodyMappingScript

    def setBodyMappingScript(self, bodyMappingScript):
        self.bodyMappingScript = bodyMappingScript

    def getOutputMappingScript(self):
        return self.outputMappingScript

    def setOutputMappingScript(self, outputMappingScript):
        self.outputMappingScript = outputMappingScript

    def getUid(self):
        return self.uid

    def setUid(self, uid):
        self.uid = uid
