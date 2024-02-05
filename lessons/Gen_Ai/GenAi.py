from src.collager.pojo.ResultApi import Result
from src.collager.util.LogApi import Log
from src.collager.util.GCPGenApi import GCPGenApi


def summarizeText(parameters):
    if "text" not in parameters:
        return Result.getFailedResult("text is missing")
    text = parameters["text"]
    return GCPGenApi.summarizeText(text)


def chat(parameters):
    if "messages" not in parameters:
        return Result.getFailedResult("messages1 is missing")
    # call GCPGenApi to send messages
    Log.info("Sending request to chat...")
    res = GCPGenApi.chat(parameters)
    # in case of any error log it
    if res.isFailed():
        Log.error("There is an error to get response from GCPGenApi Model. Error: " + res.getMessage())
        return Result.getFailedResult("There is an error to get response from GCPGenApi Model")
    Log.info("Successfully fetched response")
    # return the successful response
    responseMessages = {
        "messages": (dict(res.getData())).get("messages")
    }

    return Result.getSuccessResultWithData(responseMessages)
