from typing import Dict, List, Union

from src.collager.util import DSApi
from src.collager.util.LogApi import Log



SQL_QUERY_TEMPLATE =  "SELECT " + "  c.id AS customer_id, " + "  c.firstName AS first_name, " + "  c.lastName AS last_name, " + "  li.id AS line_item_id, " + "  li.description, " + "  li.price " + "FROM " + "  Customer_tbl c " + "JOIN " + "  LineItem_tbl li ON c.id = li.customerId " + "WHERE " +  "  c.id = {{{id}}}"


def iterate(parameters):
    # instantiate a data iterator using SQL template.
    dataIterator = DSApi.getDataIterator(1, 3, SQL_QUERY_TEMPLATE)
    # Set parameters into dataIterator's DataRequest.
    dataIterator.getDataRequest().setParams(parameters)
    # Initialize DataIterator.
    r = dataIterator.initialize()

    if r.isFailed():
        Log.error("Failed to initialize DataIterator", "error", r.getMessage())
        return r

    total_count = dataIterator.getTotalItems()

    # print total number of records iterator will iterate through.
    Log.info(f"Total number of items: {total_count}")
    all_items: List[Dict[str, Union[str, int]]] = []

    # iterate through each record.
    while dataIterator.hasNext():
        items = dataIterator.getPage()
        all_items.extend(items)

    return all_items
