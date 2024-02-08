

class AssociationM:

    def __init__(self):
        self.type = None
        self.dir = "CLS1_TO_CLS2"
        self.class2Name = None
        self.attrMapping = None
        self.importAttrMapping = None
        self.where = None
        self.orderBy = None
        self.groupBy = None
        self.having = None
        self.start = 1
        self.size = 10000
        self.sql = None

    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type

    def getDir(self):
        return self.dir

    def setDir(self, dir):
        self.dir = dir

    def getClass2Name(self):
        return self.class2Name

    def setClass2Name(self, class2Name):
        self.class2Name = class2Name

    def getAttrMapping(self):
        return self.attrMapping

    def setAttrMapping(self, attrMapping):
        self.attrMapping = attrMapping

    def getImportAttrMapping(self):
        return self.importAttrMapping

    def setImportAttrMapping(self, importAttrMapping):
        self.importAttrMapping = importAttrMapping

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

    def getHaving(self):
        return self.having

    def setHaving(self, having):
        self.having = having

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

    def checkIfManyToMany(self):
        return "MANY_TO_MANY".equalsIgnoreCase(self.type)

    def checkIfOneToMany(self):
        return "ONE_TO_MANY".equalsIgnoreCase(self.type)

    def checkIfManyToOne(self):
        return "MANY_TO_ONE".equalsIgnoreCase(self.type)

    def checkIfOneToOne(self):
        return "ONE_TO_ONE".equalsIgnoreCase(self.type)
