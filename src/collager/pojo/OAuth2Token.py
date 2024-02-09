from typing import Dict, Any
import time


class OAuth2Token:
    IMPLICIT_GRANT_TYPE = "implicit"
    AUTHORIZATION_CODE_GRANT_TYPE = "authorization_code"
    PASSWORD_GRANT_TYPE = "password"
    CLIENT_CREDENTIALS_GRANT_TYPE = "client_credentials"

    GRANT_TYPE_ATTR_NAME = "grant_type"
    OAUTH_URL_ATTR_NAME = "oauthUrl"
    TOKEN_URL_ATTR_NAME = "tokenUrl"
    CLIENT_ID_ATTR_NAME = "client_id"
    CLIENT_SECRET_ATTR_NAME = "client_secret"
    USERNAME_ATTR_NAME = "username"
    PASSWORD_ATTR_NAME = "password"
    REDIRECT_URI_ATTR_NAME = "redirect_uri"
    SCOPE_ATTR_NAME = "scope"
    CODE_ATTR_NAME = "code"

    ACCESS_TOKEN_ATTR_NAME = "access_token"
    REFRESH_TOKEN_ATTR_NAME = "refresh_token"
    EXPIRES_IN_ATTR_NAME = "expires_in"
    REFRESH_EXPIRES_IN_ATTR_NAME = "refresh_expires_in"
    REFRESH_TOKEN_GRANT_TYPE = "refresh_token"

    def __init__(self, accessToken: str, refreshToken: str, expiry: int, orgName: str, appName: str, serviceName: str):
        self.accessToken = accessToken
        self.refreshToken = refreshToken
        self.expiry = expiry
        self.createdAt = int(time.time() * 1000)
        if accessToken is None:
            self.expireAccessToken()
        self.orgName = orgName
        self.appName = appName
        self.serviceName = serviceName

    def getAccessToken(self) -> str:
        return self.accessToken

    def getRefreshToken(self) -> str:
        return self.refreshToken

    def getExpiry(self) -> int:
        return self.expiry

    def expireAccessToken(self) -> None:
        self.expiry = 0

    def isAccessTokenExpired(self) -> bool:
        expiresAt = self.createdAt + self.expiry * 1000
        return expiresAt < int(time.time() * 1000)

    def getRefreshTokenExpiry(self) -> int:
        return self.refreshTokenExpiry

    def setRefreshTokenExpiry(self, refreshTokenExpiry: int) -> None:
        self.refreshTokenExpiry = refreshTokenExpiry

    def getOrgName(self) -> str:
        return self.orgName

    def getAppName(self) -> str:
        return self.appName

    def getServiceName(self) -> str:
        return self.serviceName

    @staticmethod
    def makeOAuthToken(response: Dict[str, Any], serviceName: str) -> 'OAuth2Token':
        return OAuth2Token._makeOAuthToken(response, "cloud", "shared", serviceName)

    @staticmethod
    def _makeOAuthToken(response: Dict[str, Any], orgName: str, appName: str, serviceName: str) -> 'OAuth2Token':
        accessToken = response.get(OAuth2Token.ACCESS_TOKEN_ATTR_NAME)
        refreshToken = response.get(OAuth2Token.REFRESH_TOKEN_ATTR_NAME)
        tokenExpiresIn = int(response.get(OAuth2Token.EXPIRES_IN_ATTR_NAME, 86400 * 30))  # default 30 days
        token = OAuth2Token(accessToken, refreshToken, tokenExpiresIn, orgName, appName, serviceName)

        refreshTokenExpiresIn = int(response.get("refresh_expires_in", -1))
        token.setRefreshTokenExpiry(refreshTokenExpiresIn)

        return token
