from collections import OrderedDict
import logging
from typing import List

from src.collager.model.AuditLogUtil import AuditLogUtil
from src.collager.pojo.ResultApi import Result
from src.collager.util.CallLogger import CallLogger
from src.collager.util.Util import Util
from src.io.util.Proxy import Proxy

_logger = logging.getLogger(__name__)
_call_logger = CallLogger()

LogApiBaseEndpoint = "/api/v1.1/log"


def callLogger():
    return _call_logger


def setLogLevel(logLevel):
    callLogger().setLogLevel(logLevel)


def disableLogsCollection():
    callLogger().setCollectCallLogs(False)


def enableLogsCollection():
    callLogger().setCollectCallLogs(True)


def debug(msg, *args):
    cl = callLogger()
    if cl.isDebugOn():
        _log(logging.DEBUG, msg, args, None)
        cl.debug(msg)


def info(msg, *args):
    cl = callLogger()
    if cl.isInfoOn():
        _log(logging.INFO, msg, args, None)
        cl.info(msg)


def warn(msg, *args):
    cl = callLogger()
    if cl.isWarningOn():
        _log(logging.WARNING, msg, args, None)
        cl.warn(msg)


def error(msg, *args):
    cl = callLogger()
    if cl.isErrorOn():
        _log(logging.ERROR, msg, args, None)
        cl.error(msg)


def infoR(msg, *args):
    info(msg, *args)
    return Result.getSuccessResult(msg)


def warnR(msg, *args):
    warn(msg, *args)
    return Result.getSuccessResult(msg)


def errorR(msg, *args):
    error(msg, *args)
    return Result.getFailedResult(msg)


def auditLogWarning(summary, *args):
    auditLog(type="warn", summary=summary, *args)
    callLogger().warn(summary)


def auditLogWarn(summary, *args):
    auditLog(type="warn", summary=summary, *args)
    callLogger().warn(summary)


def auditLogError(summary, *args):
    auditLog(type="error", summary=summary, *args)
    callLogger().error(summary)


def auditLogCritical(summary, *args):
    auditLog(type="critical", summary=summary, *args)
    callLogger().critical(summary)


def auditInfo(action, summary, detail, sourceUid, *args):
    auditLog2(action, "info", summary, detail, sourceUid, *args)


def auditWarn(action, summary, detail, sourceUid, *args):
    auditLog2(action, "warn", summary, detail, sourceUid, *args)


def auditError(action, summary, detail, sourceUid, *args):
    auditLog2(action, "error", summary, detail, sourceUid, *args)


def auditCritical(action, summary, detail, sourceUid, *args):
    auditLog2(action, "critical", summary, detail, sourceUid, *args)


def auditInfo2(action, summary, *args):
    auditLog2(action, "info", summary, None, None, *args)


def auditWarn2(action, summary, *args):
    auditLog2(action, "warn", summary, None, None, *args)


def auditError2(action, summary, *args):
    auditLog2(action, "error", summary, None, None, *args)


def auditCritical2(action, summary, *args):
    auditLog2(action, "critical", summary, None, None, *args)


def auditInfoR(action, summary, detail, sourceUid, *args):
    auditInfo(action, summary, detail, sourceUid, *args)
    return Result.getSuccessResult(summary)


def auditWarnR(action, summary, detail, sourceUid, *args):
    auditWarn(action, summary, detail, sourceUid, *args)
    return Result.getSuccessResult(summary)


def auditErrorR(action, summary, detail, sourceUid, *args):
    auditError(action, summary, detail, sourceUid, *args)
    return Result.getFailedResult(summary)


def auditCriticalR(action, summary, detail, sourceUid, *args):
    auditCritical(action, summary, detail, sourceUid, *args)
    return Result.getFailedResult(summary)


def auditInfo2R(action, summary, *args):
    auditInfo2(action, summary, *args)
    return Result.getSuccessResult(summary)


def auditWarn2R(action, summary, *args):
    auditWarn2(action, summary, *args)
    return Result.getSuccessResult(summary)


def auditError2R(action, summary, *args):
    auditError2(action, summary, *args)
    return Result.getFailedResult(summary)


def auditCritical2R(action, summary, *args):
    auditCritical2(action, summary, *args)
    return Result.getFailedResult(summary)


def auditLog(logObject=None, type=None, summary=None, *args):
    if logObject is not None:

        # no server side logging is done from the local env.
        return None
    sl = [""] * 4
    for i, arg in enumerate(args):
        if i >= 4:
            break
        sl[i] = arg
    _auditLog(type, summary, sl[0], sl[1], sl[2], sl[3])


# @multimethod(dict)
# def auditLog(logObject):
#     # no server side logging is done from the local env.
#     pass

def auditLog2(action, type, summary, detail, sourceUid, *args):
    summary = makeFullMessage(summary, args)
    detail_str = None
    if isinstance(detail, str):
        detail_str = detail
    elif isinstance(detail, dict):
        detail_str = Util.asJSONPrettyString(detail)
    json = makeMapParametersJson(args)
    _auditLog(type, summary, detail_str, json, action, sourceUid)


def _auditLog(type, summary, detail, json, action, sourceUid):
    auditLog(logObject=AuditLogUtil.makeAuditLog(type, sourceUid, action, summary, detail, json))
    logToConsole(type, summary)


def logToConsole(type, msg):
    if type == "debug":
        log(logging.DEBUG, msg)
    elif type == "info":
        log(logging.INFO, msg)
    elif type == "warn":
        log(logging.WARNING, msg)
    elif type == "error":
        log(logging.ERROR, msg)
    elif type == "critical":
        log(logging.ERROR, msg)


def log(level, msg):
    userId = Proxy.getUserId() or ""
    txId = ""
    if userId == "guest":
        userId = ""
    s = f"({userId}) " if userId else ""
    if txId:
        s += f"({userId}|{txId}) "
    msg = s + msg
    _logger.log(level, msg)


def _log(level, msg, args, t):
    userId = Proxy.getUserId() or ""
    txId = ""
    if userId == "guest":
        userId = ""
    s = f"({userId}) " if userId else ""
    if txId:
        s += f"({userId}|{txId}) "
    msg = s + msg
    msg = makeFullMessage(msg, args)
    _logger.log(level, msg, exc_info=t)


def makeFullMessage(msg, args):
    json = makeNameValueJson(args)
    if json:
        msg += f" {json}"
    return msg


def makeNameValueJson(args):
    if not args:
        return None
    m = OrderedDict()
    i = 0
    n = len(args)
    while i < n:
        name = args[i]
        if isinstance(name, str):
            i += 1
            if i < n:
                value = args[i]
                m[name] = value
            else:
                break
        i += 1
    if not m:
        return None
    return Util.asJSONString(m)


def makeMapParametersJson(args):
    if not args:
        return None
    m = OrderedDict()
    for v in args:
        if isinstance(v, dict):
            m.update(v)
    if not m:
        return None
    return Util.asJSONPrettyString(m)


def logInfo(msg):
    cl = callLogger()
    if cl.isInfoOn():
        logging.log(logging.INFO, msg)


def logWarn(msg):
    cl = callLogger()
    if cl.isWarningOn():
        logging.log(logging.WARNING, msg)


def logError(msg):
    cl = callLogger()
    if cl.isErrorOn():
        logging.log(logging.ERROR, msg)


def auditLogInfo(summary: str, *args: List[str]) -> None:
    auditLog(type="info", summary=summary, *args)
    callLogger().info(summary)

