import json
import logging


class BaseApi:
    log = logging.getLogger(__name__)

    @staticmethod
    def asJSONPrettyString(my_dict):
        json_string = json.dumps(my_dict, indent=2, sort_keys=True)
        return json_string
