from typing import List, Dict, Union

from src.collager.model.DataRequest import DataRequest
from src.collager.pojo.ResultApi import Result
from src.collager.util import DSApi
from src.collager.util.LogApi import Log

SQL_QUERY_TEMPLATE = '''SELECT 
          c.id AS customer_id, 
          c.firstName AS first_name, 
          c.lastName AS last_name, 
          li.id AS line_item_id, 
          li.description, 
          li.price 
        FROM 
          Customer_tbl c 
        JOIN 
          LineItem_tbl li ON c.id = li.customerId 
        WHERE 
          c.id = {{{id}}}
    '''


def page(parameters: Dict[str, Union[str, int]]) -> List[Dict[str, Union[str, int]]]:
    dsr = DataRequest()
    # fetch records of class customers
    dsr.setClassName("Customer")
    # page size is 3
    dsr.setSize(3)
    # start index is 0
    dsr.setStart(0)
    dsr.setSql(SQL_QUERY_TEMPLATE)

    # we passed incoming parameters in dsr. Trillo Workbench uses them to process the template.
    dsr.setParams(dict(parameters))

    r = None
    data_list = []
    response = {}
    total_items = -1
    result = Result()
    while True:
        # returns a Map or Result object (in case of error)
        # if successful, the map contains the following keys.
        # totalItems
        # start
        # items of List<Object> type
        r = DSApi.getPage(vars(dsr))
        if isinstance(r, dict):
            response = r
            if total_items == -1:
                # save totalItems
                total_items = response.get("totalItems", -1)
            data_list.append(response.get("items", []))
            if len(data_list) == total_items:
                break
        elif isinstance(r, Result):
            # returns result if there is failure
            result = r
            if result.isFailed():
                Log.error("Failed: " + result.getMessage())
            else:
                Log.info("Message: " + result.getMessage())
            break

    Log.info("Number of items fetched: " + str(len(data_list)))
    return data_list
