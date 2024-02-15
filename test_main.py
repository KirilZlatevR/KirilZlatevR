import requests
import BearerTokenResponse


def test_get_access_token():
    data = {"returnUrl": 'home', "email": 'sisautomationtest@gustr.com', "password": 'Qwerty123'}  
    response = requests.post("https://api.dev.sis.amexis.net/api/account/login", json=data)
    assert response.status_code == 200
    response_to_json = response.json()
    bearer_token = BearerTokenResponse.Token(response_to_json['accessToken'], response_to_json['refreshToken'])

    access_token = bearer_token.accessToken

    print(access_token)

