import requests

CLIENT_ID = '7b4f08d78c1044288d0aba1b4e73449f'
CLIENT_SECRET = 'dbfe3a685dc249b2b51c4fd2a828a23a'


AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET
})

auth_response_data = auth_response.json()


access_token = auth_response_data['access_token']
ACCESS_TOKEN = access_token
print(ACCESS_TOKEN, '\n\n')
