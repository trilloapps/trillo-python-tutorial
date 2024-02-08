from typing import List, Optional

from src.collager.model.FlowNodeM import FlowNodeM


class FlowM:
    def __init__(self):
        self.type: Optional[str] = None
        self.orgName: Optional[str] = None  # orgName to which the flow metadata belongs
        self.appName: Optional[str] = None  # orgName to which the flow metadata belongs
        self.flowNodes: Optional[List[FlowNodeM]] = None

    def getType(self) -> Optional[str]:
        return self.type

    def setType(self, type: Optional[str]) -> None:
        self.type = type

    def getOrgName(self) -> Optional[str]:
        return self.orgName

    def setOrgName(self, orgName: Optional[str]) -> None:
        self.orgName = orgName

    def getAppName(self) -> Optional[str]:
        return self.appName

    def setAppName(self, appName: Optional[str]) -> None:
        self.appName = appName

    def getFlowNodes(self) -> Optional[List[FlowNodeM]]:
        return self.flowNodes

    def setFlowNodes(self, flowNodes: Optional[List[FlowNodeM]]) -> None:
        self.flowNodes = flowNodes

    def addFlowNode(self, flowNode: FlowNodeM) -> None:
        if self.flowNodes is None:
            self.flowNodes = []
        self.flowNodes.append(flowNode)

    def addFunction(self, name: str, functionName: str, failureFunctionName: Optional[str] = None) -> FlowNodeM:
        flowNode = FlowNodeM()
        flowNode.setName(name)
        flowNode.setType(FlowNodeM.ACTIVITY_TYPE)
        flowNode.setActivityType(FlowNodeM.FUNCTION_ACTIVITY_TYPE)
        flowNode.setFunctionName(functionName)
        if failureFunctionName is not None:
            flowNode.setFailureFunctionName(failureFunctionName)
        self.addFlowNode(flowNode)
        return flowNode

    @staticmethod
    def newFlow(name: str) -> 'FlowM':
        fl = FlowM()
        fl.setName(name)
        return fl
