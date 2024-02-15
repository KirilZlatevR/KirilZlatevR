from auth0.v3.authentication import GetToken
from auth0.v3.exceptions import Auth0Error
from Auth0.Auth0BasePage import Auth0BasePage


class Auth0Service(Auth0BasePage):
    def __init__(self, format_data_from_file, auth0_update_user_data):
        self.format_data_from_file = format_data_from_file
        self.auth0_update_user_data = auth0_update_user_data

    async def login_async(self, model):
        client_id = model.get('client_id')
        client_secret = model.get('client_secret')

        try:
            request = {
                "audience": "the Audience for the project",
                "username": model.get('email'),
                "password": model.get('password'),
                "signing_algorithm": self.signing_algorithm,
                "client_id": client_id,
                "client_secret": client_secret,
                "scope": "the scope",
            }

            with GetToken(self.get_auth_client()) as auth_client:
                response = auth_client.login_with_resource_owner_password(**request)
                return response
        except Auth0Error as e:
            # Handle authentication errors here
            raise e

    def get_token_for_each_access_level(self, model):
        token = ""
        token = self.login_async(model)['access_token']

        return  token

