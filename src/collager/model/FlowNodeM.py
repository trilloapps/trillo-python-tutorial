from typing import List, Optional


class FlowNodeM:
    START_TYPE = "start"
    END_TYPE = "end"
    MULTI_ACTIVITY_TYPE = "multiActivity"
    PARALLEL_TYPE = "parallelActivity"
    REPEAT_ACTIVITY_TYPE = "repeatActivity"
    BRANCH_TYPE = "branch"
    DEFAULT_BRANCH_TYPE = "defaultBranch"
    PARALLEL_BRANCH_TYPE = "parallelBranch"
    BRANCH_ENTRY_TYPE = "branchEntry"
    DEFAULT_ENTRY_TYPE = "defaultBranchEntry"
    REPEAT_BRANCH_ENTRY_TYPE = "repeatBranchEntry"
    REPEAT_START_EXP_TYPE = "repeatStartExp"
    REPEAT_END_EXP_TYPE = "repeatEndExp"
    ACTIVITY_TYPE = "activity"
    FUNCTION_ACTIVITY_TYPE = "function"
    SCRIPT_ACTIVITY_TYPE = "script"
    FLOW_ACTIVITY_TYPE = "flow"

    def __init__(self):
        self.name: Optional[str] = None
        self.type: Optional[str] = None
        self.activityType: Optional[str] = None
        self.flowNodes: Optional[List[FlowNodeM]] = None
        self.parent: Optional[FlowNodeM] = None
        self.functionName: Optional[str] = None
        self.failureFunctionName: Optional[str] = None
        self.timeout: int = -1
        self.inputParameterId: Optional[str] = None
        self.inputParameterName: Optional[str] = None

    def getName(self) -> Optional[str]:
        return self.name

    def setName(self, name: Optional[str]) -> None:
        self.name = name

    def getType(self) -> Optional[str]:
        return self.type

    def setType(self, type: Optional[str]) -> None:
        self.type = type

    def getActivityType(self) -> Optional[str]:
        return self.activityType

    def setActivityType(self, activityType: Optional[str]) -> None:
        self.activityType = activityType

    def getTimeout(self) -> int:
        return self.timeout

    def setTimeout(self, timeout: int) -> None:
        self.timeout = timeout

    def getFlowNodes(self) -> Optional[List['FlowNodeM']]:
        return self.flowNodes

    def setFlowNodes(self, flowNodes: Optional[List['FlowNodeM']]) -> None:
        self.flowNodes = flowNodes

    def updateParent(self, parent: 'FlowNodeM') -> None:
        self.parent = parent
        if self.flowNodes is not None:
            for child in self.flowNodes:
                child.updateParent(self)

    def retreiveParent(self) -> Optional['FlowNodeM']:
        return self.parent

    def getStartNode(self) -> Optional['FlowNodeM']:
        if self.flowNodes is not None and len(self.flowNodes) > 0 and self.flowNodes[0].getType() == self.START_TYPE:
            return self.flowNodes[0]
        return None

    def getFunctionName(self) -> Optional[str]:
        return self.functionName

    def setFunctionName(self, functionName: Optional[str]) -> None:
        self.functionName = functionName

    def getFailureFunctionName(self) -> Optional[str]:
        return self.failureFunctionName

    def setFailureFunctionName(self, failureFunctionName: Optional[str]) -> None:
        self.failureFunctionName = failureFunctionName

    def getInputParameterId(self) -> Optional[str]:
        return self.inputParameterId

    def setInputParameterId(self, inputParameterId: Optional[str]) -> None:
        self.inputParameterId = inputParameterId

    def getInputParameterName(self) -> Optional[str]:
        return self.inputParameterName

    def setInputParameterName(self, inputParameterName: Optional[str]) -> None:
        self.inputParameterName = inputParameterName
