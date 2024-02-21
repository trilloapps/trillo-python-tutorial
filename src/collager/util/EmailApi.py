from multimethods import multimethod
from src.collager.util.Util import Util
from src.collager.util.HttpRequestUtil import HttpRequestUtil

emailBaseEndpoint = "/api/v1.1/email"


@multimethod(str, str, str, str, str, str, dict)
def sendEmail(appName, email, subject, content, template, fromAlias, templateParams):
    body = {"subject": subject,
            "content": content,
            "appName": appName,
            "email": email,
            "template": template,
            "fromAlias": fromAlias,
            "templateParams": templateParams
            }
    res = HttpRequestUtil.post(emailBaseEndpoint + "/sendEmail", body)
    return Util.convertToResult(res)


@multimethod(str, str, str)
def sendEmail(toEmail, subject, content):
    body = {
        "toEmail": toEmail,
        "subject": subject,
        "content": content
    }
    res = HttpRequestUtil.post(emailBaseEndpoint + "/sendEmail", body)
    return Util.convertToResult(res)


@multimethod(str, str, str)
def sendEmailMarkDownContent(mailTo, content, subject):
    body = {
        "mailTo": mailTo,
        "subject": subject,
        "content": content
    }
    res = HttpRequestUtil.post(emailBaseEndpoint + "/sendEmail", body)
    return Util.convertToResult(res)
