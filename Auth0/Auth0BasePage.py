from auth0.v3.authentication import GetToken
from auth0.v3.management import Auth0 as Auth0Management
from auth0.v3.exceptions import Auth0Error

class Auth0BasePage:
    def __init__(self, settings):
        self.settings = settings
        self.signing_algorithm = "RS256"  # Replace with your actual signing algorithm

    def get_auth_client(self):
        return GetToken("the Authority of the project")

    def get_management_api_client(self):
        management_token = self.get_client_credentials_token()
        return Auth0Management(token=management_token, domain="the Authority of the project")

    async def get_client_credentials_token(self):
        auth_client = self.get_auth_client()
        try:
            tokens = await auth_client.client_credentials(
                client_id="the ClientId",
                client_secret="the ClientSecret",
                audience="the Audience of the project",
                grant_type=""
                #signing_algorithm=self.signing_algorithm # this most likely should be RS256
            )
            return tokens['access_token']
        except Auth0Error as e:
            # Handle authentication errors here
            raise e

