from typing import Any, Dict

from src.collager.pojo.RuntimeContext import RuntimeContext
from src.io.util.Proxy import Proxy


class ScriptParameter(RuntimeContext):

    def __init__(self):
        super().__init__()

    @classmethod
    def make_script_parameter(cls, input_data: Any, state_map: Dict[str, Any], task_name: str = None,
                              execution_id: int = -1):
        p = ScriptParameter()
        p.set_v(input_data)

        if state_map is not None:
            p.update(state_map)

        p.set_task_name(task_name)
        p.set_execution_id(execution_id)

        login_response = Proxy.get_login_response()

        if isinstance(login_response.get("user"), dict):
            um = login_response.get("user")
            p.set_id_of_user(int(um.get("id", -1)))
            p.set_user_id(um.get("userId"))
            p.set_first_name(um.get("firstName"))
            p.set_last_name(um.get("lastName"))
            p.set_email(um.get("email"))
            p.set_user_org_name(um.get("orgName"))
            p.set_external_id(um.get("externalId"))
            p.set_role(um.get("role"))
            p.set_email_verified(bool(um.get("emailVerified")))
            p.set_tenant_id(um.get("tenantId"))
            p.set_tenant_name(um.get("tenantName"))
            p.set_user_org_id(int(um.get("orgId", -1)))

        p.set_app_name(Proxy.get_app_name())
        p.set_org_name(Proxy.get_org_name())

        return p
