from typing import Dict, Any

from src.io.util.Proxy import Proxy


class AuditLogUtil:
    MAX_SUMMARY_SIZE = 255
    MAX_ACTION_SIZE = 48

    @staticmethod
    def makeAuditLog(type: str, sourceUid: str, action: str, summary: str, detail: str = None, json: str = None) -> \
    Dict[str, Any]:
        m = AuditLogUtil.makeAuditLogWithDetail(type, sourceUid, action, summary, detail)
        m["json"] = json
        return m

    @staticmethod
    def makeAuditLogWithDetail(type: str, sourceUid: str, action: str, summary: str, detail: str) -> Dict[str, Any]:
        m = AuditLogUtil.makeAuditLogWithoutDetail(type, sourceUid, action, summary)
        m["detail"] = detail
        return m

    @staticmethod
    def makeAuditLogWithoutDetail(type: str, sourceUid: str, action: str, summary: str) -> Dict[str, Any]:
        m = AuditLogUtil.createLogObject(type, action, summary)
        m["sourceUid"] = sourceUid
        return m

    @staticmethod
    def makeTaskLog(type: str, action: str, summary: str, taskExecId: int) -> Dict[str, Any]:
        m = AuditLogUtil.createLogObject(type, action, summary)
        m["taskExecId"] = taskExecId
        return m

    @staticmethod
    def createLogObject(type: str, action: str, summary: str) -> Dict[str, Any]:
        m = {
            "summary": summary,
            "type": type,
            "action": action[:AuditLogUtil.MAX_ACTION_SIZE],
            "idOfUser": Proxy.getIdOfCurrentUser(),
            "userId": Proxy.getUserId(),
            "taskExecId": "-1"
        }
        if len(summary) > AuditLogUtil.MAX_SUMMARY_SIZE:
            m["summary"] = summary[:AuditLogUtil.MAX_SUMMARY_SIZE]
        return m
