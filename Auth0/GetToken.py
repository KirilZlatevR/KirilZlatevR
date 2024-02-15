import Auth0.Auth0Service as auth0Service
import LoginUserCredentialsInputModel as loginInputModel

def GetToken(inputModel):
    token = auth0Service.Auth0Service.get_token_for_each_access_level(inputModel)

    print(token)

inputModel = loginInputModel.LoginUserCredentialsInputModel()
inputModel.email = "testcase@gmail.com"
inputModel.password = "Qwerty123"
inputModel.client_id = "clientId for the project"
inputModel.client_secret = "clientSecret for the project"

GetToken(inputModel)