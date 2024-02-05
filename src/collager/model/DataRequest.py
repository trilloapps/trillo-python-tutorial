class DataRequest:
    def __init__(self, *args, **kwargs):
        self.appName = None
        self.dsName = None
        self.className = None
        self.where = None
        self.orderBy = None
        self.groupBy = None
        self.start = 1
        self.size = 10
        self.sql = None
        self.sqlTemplate = None
        self.params = None
        self.includeDeleted = False
        self.usingRowLimits = False
        self.usingView = False
        self.viewName = None
        self.forAllUsers = False
        self.countQuery = None
        self.filter = None

    def getClassName(self):
        return self.className

    def setClassName(self, className):
        self.className = className

    def getWhere(self):
        return self.where

    def setWhere(self, where):
        self.where = where

    def getOrderBy(self):
        return self.orderBy

    def setOrderBy(self, orderBy):
        self.orderBy = orderBy

    def getGroupBy(self):
        return self.groupBy

    def setGroupBy(self, groupBy):
        self.groupBy = groupBy

    def getStart(self):
        return self.start

    def setStart(self, start):
        self.start = start

    def getSize(self):
        return self.size

    def setSize(self, size):
        self.size = size

    def getSql(self):
        return self.sql

    def setSql(self, sql):
        self.sql = sql

    def getSqlTemplate(self):
        return self.sqlTemplate

    def setSqlTemplate(self, sqlTemplate):
        self.sqlTemplate = sqlTemplate

    def getParams(self):
        return self.params

    def setParams(self, params):
        self.params = params

    def isIncludeDeleted(self):
        return self.includeDeleted

    def setIncludeDeleted(self, includeDeleted):
        self.includeDeleted = includeDeleted

    def isUsingRowLimits(self):
        return self.usingRowLimits

    def setUsingRowLimits(self, usingRowLimits):
        self.usingRowLimits = usingRowLimits

    def isUsingView(self):
        return self.usingView

    def setUsingView(self, usingView):
        self.usingView = usingView

    def getViewName(self):
        return self.viewName

    def setViewName(self, viewName):
        self.viewName = viewName

    def isForAllUsers(self):
        return self.forAllUsers

    def setForAllUsers(self, forAllUsers):
        self.forAllUsers = forAllUsers

    def getFilter(self):
        return self.filter

    def setFilter(self, filter):
        self.filter = filter

    def getCountQuery(self):
        return self.countQuery

    def setCountQuery(self, countQuery):
        self.countQuery = countQuery

    def getAppName(self):
        return self.appName

    def setAppName(self, appName):
        self.appName = appName

    def getDsName(self):
        return self.dsName

    def setDsName(self, dsName):
        self.dsName = dsName
