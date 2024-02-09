import logging
from collections import OrderedDict
import json
from functools import cmp_to_key


class ClassM:
    def __init__(self):
        self.superClass = None
        self.nameInDS = None
        self.tableCreateable = True
        self.deleteAllBeforeSync = False
        self.primaryKeyGenerator = "serial"
        self.attributes = []
        self.associations = []
        self.dsSqlTemplates = None
        self.apiSpecs = []
        self.viewCreateStmt = None
        self.appName = None
        self.dsName = None
        self.tableDbViewName = None
        self.custom = False
        self.schemaName = None
        self.dsType = None
        self.multiTenancyOptional = False
        self.uiProps = None

    def getDsSqlTemplates(self):
        return self.dsSqlTemplates

    def setDsSqlTemplates(self, dsSqlTemplates):
        self.dsSqlTemplates = dsSqlTemplates

    def getDsSqlTemplateByName(self, name):
        if self.dsSqlTemplates is None:
            return None
        for template in self.dsSqlTemplates:
            if name.lower() == template.getName().lower():
                return template
        return None

    def getSuperClass(self):
        return self.superClass

    def setSuperClass(self, superClass):
        self.superClass = superClass

    def getNameInDS(self):
        if self.nameInDS is None:
            return self.getName() + "_tbl"
        return self.nameInDS

    def setNameInDS(self, nameInDS):
        self.nameInDS = nameInDS

    def isTableCreateable(self):
        return self.tableCreateable

    def setTableCreateable(self, tableCreateable):
        self.tableCreateable = tableCreateable

    def getPrimaryKeyGenerator(self):
        return self.primaryKeyGenerator

    def setPrimaryKeyGenerator(self, primaryKeyGenerator):
        self.primaryKeyGenerator = primaryKeyGenerator

    def getSchemaName(self):
        return self.schemaName

    def setSchemaName(self, schemaName):
        self.schemaName = schemaName

    def getAttributes(self):
        return self.attributes

    def setAttributes(self, attrs):
        self.attributes = attrs

    def getAssociations(self):
        return self.associations

    def setAssociations(self, associations):
        self.associations = associations

    def addAttribute(self, attrM):
        current = self.getAttribute(attrM.getName())
        if current is None:
            self.attributes.append(attrM)

    def addAssociation(self, associationM):
        current = self.getAssociation(associationM.getName())
        if current is None:
            self.associations.append(associationM)

    def getAttribute(self, attrName):
        if attrName is None:
            return None
        for attrM in self.attributes:
            if attrName.lower() == attrM.getName().lower():
                return attrM
        return None

    def getAttributeByNameInDs(self, nameInDS):
        for attrM in self.attributes:
            if nameInDS.lower() == attrM.getNameInDS().lower():
                return attrM
        return None

    def getAttributeByBestMatch(self, name):
        for attrM in self.attributes:
            if name.lower() == attrM.getName2().lower():
                return attrM
        a = self.getAttributeByNameInDs(name)
        if a is not None:
            return a
        return self.getAttribute(name)

    def getAssociation(self, assocName):
        for assocM in self.associations:
            if assocName.lower() == assocM.getName().lower():
                return assocM
        return None

    def getAssociationByClass2(self, class2Name):
        for assocM in self.associations:
            if class2Name.lower() == assocM.getClass2Name().lower():
                return assocM
        return None

    def retrievePrimaryKeyAttribute(self):
        for attrM in self.attributes:
            if attrM.isPersistent() and attrM.isPrimaryKey():
                return attrM
        return None

    def getAssociationsJson(self):
        return json.dumps([assoc.__dict__ for assoc in self.associations])

    def setAssociationsJson(self, json_str):
        self.associations = json.loads(json_str, object_hook=lambda d: AssociationM(**d))

    def getViewCreateStmt(self):
        return self.viewCreateStmt

    def setViewCreateStmt(self, viewCreateStmt):
        self.viewCreateStmt = viewCreateStmt

    def addAttributes(self, l):
        for attr in l:
            self.addAttribute(attr)

    def addAssociations(self, l):
        for a in l:
            self.addAssociation(a)

    def isMultiTenancyOptional(self):
        return self.multiTenancyOptional

    def setMultiTenancyOptional(self, multiTenancyOptional):
        self.multiTenancyOptional = multiTenancyOptional

    def retrieveTenantAttribute(self):
        for attr in self.attributes:
            if attr.isTenant():
                return attr
        return None

    def retrieveRepresentUserAttribute(self):
        for attr in self.attributes:
            if attr.isRepresentsUser():
                return attr
        return None

    def retrieveRepresentOrderingAttribute(self):
        for attr in self.attributes:
            if attr.isRepresentsOrdering():
                v = attr.convertValue("")
                if isinstance(v, int):
                    return attr
        return None

    def retrieveTableNameWithoutSchema(self):
        if self.nameInDS is not None:
            return self.nameInDS
        return self.getName().lower() + "_tbl"

    def retrieveTableName(self):
        name = self.nameInDS if self.nameInDS is not None else self.getName()
        if self.schemaName is not None and self.schemaName.strip() != "":
            return f'"{self.schemaName}"."{name}"'
        return name

    def retrieveApiClassPath(self):
        return (
                   f"{self.schemaName}." if self.schemaName is not None and self.schemaName.strip() != "" else "") + self.getName()

    def getAppName(self):
        return self.appName

    def setAppName(self, appName):
        self.appName = appName

    def getDsName(self):
        return self.dsName

    def setDsName(self, dsName):
        self.dsName = dsName

    def getDsType(self):
        return self.dsType

    def setDsType(self, dsType):
        self.dsType = dsType

    def fixIt(self):
        for attr in self.attributes:
            attr.fixIt()

    def getApiSpecs(self):
        return self.apiSpecs

    def setApiSpecs(self, apiSpecs):
        self.apiSpecs = apiSpecs

    def isDeleteAllBeforeSync(self):
        return self.deleteAllBeforeSync

    def setDeleteAllBeforeSync(self, deleteAllBeforeSync):
        self.deleteAllBeforeSync = deleteAllBeforeSync

    def mapValues(self, buffer, targetMap):
        for attrM in self.attributes:
            st = attrM.getSourceStartPos()
            end = attrM.getSourceEndPos()
            if st > -1 and end > -1 and end - st >= 0:
                try:
                    v = buffer[st - 1:end].strip()
                except Exception as exc:
                    continue
            else:
                continue
            try:
                targetMap[attrM.getName()] = AttributeM.convertValue(v, attrM.getType(), attrM.getSourceFormat())
            except Exception as exc:
                logging.error(
                    f"Failed to convert attribute : {attrM.getName()}\n {exc}\n ignoring error. Function may be handling it")
                return False
        return True

    def mapValues2(self, srcMap, targetMap, attrMappings, srcTimeZone):
        if attrMappings is not None and len(attrMappings) > 0:
            for am in attrMappings:
                temp = am.getFromAttr()
                if temp in srcMap:
                    a = self.getAttribute(am.getToAttr())
                    if a is not None:
                        targetMap[a.getName()] = AttributeM.convertValue2(srcMap[temp], a.getType(),
                                                                          srcTimeZone if srcTimeZone is not None else a.getSourceTimeZone())
                    else:
                        targetMap[temp] = srcMap[temp]
        else:
            for attrM in self.attributes:
                temp = attrM.getNameInSource() if attrM.getNameInSource() is not None and attrM.getNameInSource() in srcMap else attrM.getName()
                if temp in srcMap:
                    targetMap[attrM.getName()] = AttributeM.convertValue2(srcMap[temp], attrM.getType(),
                                                                          srcTimeZone if srcTimeZone is not None else attrM.getSourceTimeZone())

    def getSourceColumnNames(self):
        l = [attrM for attrM in self.attributes if attrM.getSourceColNum() > -1]
        l.sort(key=cmp_to_key(lambda a1, a2: -1 if a1.getSourceColNum() < a2.getSourceColNum() else (
            1 if a1.getSourceColNum() > a2.getSourceColNum() else 0)))
        return [attrM.getName() for attrM in l]

    def retrieveSystemAttrs(self):
        return [attr.getName() for attr in self.attributes if attr.isSystemAttr()]

    def getTableDbViewName(self):
        return self.tableDbViewName

    def setTableDbViewName(self, tableDbViewName):
        self.tableDbViewName = tableDbViewName

    def getSchemaForDataStudio(self, includeAllSysAttrs):
        l = []
        for attr in self.attributes:
            if includeAllSysAttrs or (
                    not attr.isSystemAttr() or attr.getName() == "id" or attr.getName() == "createdAt"):
                m = OrderedDict()
                m["name"] = attr.getName()
                m["displayName"] = attr.getDisplayName() if attr.getDisplayName() != "" else attr.getName()
                conceptType = "DIMENSION"
                if attr.isNumericType():
                    m["type"] = "NUMBER"
                    conceptType = "METRIC"
                elif attr.getType().lower() == "boolean":
                    m["type"] = "BOOLEAN"
                else:
                    m["type"] = "STRING"
                m["conceptType"] = conceptType
                l.append(m)
        return l

    def isCustom(self):
        return self.custom

    def setCustom(self, custom):
        self.custom = custom

    def getUiProps(self):
        return self.uiProps

    def setUiProps(self, uiProps):
        self.uiProps = uiProps


class AssociationM:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.class2Name = kwargs.get("class2Name")


class AttributeM:
    @staticmethod
    def convertValue(value, type, sourceFormat):
        pass

    @staticmethod
    def convertValue2(value, type, sourceTimeZone):
        pass

    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.nameInDS = kwargs.get("nameInDS")
        self.sourceColNum = kwargs.get("sourceColNum")
        self.sourceStartPos = kwargs.get("sourceStartPos")
        self.sourceEndPos = kwargs.get("sourceEndPos")
        self.persistent = kwargs.get("persistent")
        self.primaryKey = kwargs.get("primaryKey")
        self.tenant = kwargs.get("tenant")
        self.representsUser = kwargs.get("representsUser")
        self.representsOrdering = kwargs.get("representsOrdering")
        self.type = kwargs.get("type")
        self.sourceFormat = kwargs.get("sourceFormat")
        self.sourceTimeZone = kwargs.get("sourceTimeZone")
        self.systemAttr = kwargs.get("systemAttr")
        self.displayName = kwargs.get("displayName")

    def getSourceColNum(self):
        return self.sourceColNum

    def getSourceStartPos(self):
        return self.sourceStartPos

    def getSourceEndPos(self):
        return self.sourceEndPos

    def isPersistent(self):
        return self.persistent

    def isPrimaryKey(self):
        return self.primaryKey

    def isTenant(self):
        return self.tenant

    def isRepresentsUser(self):
        return self.representsUser

    def isRepresentsOrdering(self):
        return self.representsOrdering

    def getType(self):
        return self.type

    def getName(self):
        return self.name

    def getNameInDS(self):
        return self.nameInDS

    def getNameInSource(self):
        pass

    def getSourceFormat(self):
        return self.sourceFormat

    def getSourceTimeZone(self):
        return self.sourceTimeZone

    def isSystemAttr(self):
        return self.systemAttr

    def getDisplayName(self):
        return self.displayName
