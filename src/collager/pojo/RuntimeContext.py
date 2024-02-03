from src.io.util.Proxy import Proxy


class RuntimeContext(dict):

    def __init__(self):
        super().__init__()
        self.id_of_user = 0
        self.user_id = "guest"
        self.first_name = ""
        self.last_name = ""
        self.email = ""
        self.external_id = ""
        self.role = ""
        self.user_org_name = ""
        self.email_verified = False
        self.tenant_id = ""
        self.tenant_name = ""
        self.user_org_id = 0
        self.picture_url = ""
        self.org_name = ""
        self.app_name = ""
        self.task_name = ""
        self.execution_id = -1
        self.mobile_phone = ""
        self.v = {}

    def get_full_name(self):
        if self.first_name or self.last_name:
            return f"{self.first_name} {self.last_name}".strip()
        else:
            return self.user_id

    def to_map(self):
        return {
            "id_of_user": self.id_of_user,
            "user_id": self.user_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "org_name": self.org_name,
            "app_name": self.app_name,
            "external_id": self.external_id,
            "role": self.role,
            "user_org_name": self.user_org_name,
            "email_verified": self.email_verified,
            "tenant_id": self.tenant_id,
            "tenant_name": self.tenant_name,
            "user_org_id": self.user_org_id,
            "picture_url": self.picture_url,
            "v": self.v,
            "task_name": self.task_name,
            "execution_id": self.execution_id
        }


class ScriptParameter(RuntimeContext):

    def __init__(self):
        super().__init__()

    @classmethod
    def make_script_parameter(cls, input_data, state_map=None, task_name=None, execution_id=-1):
        p = cls()
        p.v = input_data

        if state_map is not None:
            p.update(state_map)

        p.task_name = task_name
        p.execution_id = execution_id

        login_response = Proxy.get_login_response()

        if isinstance(login_response.get("user"), dict):
            um = login_response["user"]
            p.id_of_user = int(um.get("id", -1))
            p.user_id = um.get("userId", "guest")
            p.first_name = um.get("firstName", "")
            p.last_name = um.get("lastName", "")
            p.email = um.get("email", "")
            p.user_org_name = um.get("orgName", "")
            p.external_id = um.get("externalId", "")
            p.role = um.get("role", "")
            p.email_verified = bool(str(um.get("emailVerified")))
            p.tenant_id = um.get("tenantId", "")
            p.tenant_name = um.get("tenantName", "")
            p.user_org_id = int(um.get("orgId", 0))

        p.app_name = Proxy.get_app_name()
        p.org_name = Proxy.get_org_name()

        return p
