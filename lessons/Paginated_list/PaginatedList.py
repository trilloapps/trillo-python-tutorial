from typing import List, Dict, Union
from src.collager.model.DataRequest import DataRequest
from src.collager.pojo.ResultApi import Result
from src.collager.util import DSApi, LogApi
from src.collager.model.Exp import Exp
from src.collager.util.api import Api

@Api(httpMethod="post")
def page(parameters: Dict[str, Union[str, int]]) -> Union[List[Dict[str, Union[int, List[Dict[str, Union[str, int]]]]]], None]:
    dsr = DataRequest()
    # fetch records of class customers
    dsr.setClassName("Customer")
    # page size is 3
    dsr.setSize(3)
     # start index is 0
    dsr.setStart(0)

    # create a filter expression which says id < 5
    exp = Exp()
    exp.setLhs("id")
    exp.setOp("<")
    exp.setRhs(5)
    dsr.setFilter(vars(exp))  # comment out this line to fetch all records

    result_list: List[Dict[str, Union[int, List[Dict[str, Union[str, int]]]]]] = []
    total_items = -1
    result: Result
    while True:
        # returns a Map or Result object (in case of error)
        # if successful, the map contains the following keys:
        # totalItems
        # start
        # items of List<Object> type
        r = DSApi.getPage(vars(dsr))
        if isinstance(r, dict):
            response = r
            if total_items == -1:
                # save totalItems
                total_items = response.get("totalItems", -1)
            result_list.append(response.get("items", []))
            if len(result_list) == total_items:
                break
        elif isinstance(r, Result):
            # returns result if there is a failure
            result = r
            if result.isFailed():
                LogApi.error(f"Failed: {result.getMessage()}")
            else:
                LogApi.info(f"Message: {result.getMessage()}")
            break

    LogApi.info(f"Number of items fetched: {len(result_list)}")
    return result_list
