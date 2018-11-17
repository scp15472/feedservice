import json
import requests

USER_SERVICE_URL = 'http://localhost/userservice/'

def is_authenticated(token):
    url = USER_SERVICE_URL + 'login/' + token
    response = requests.get(url)
    response_code = response.status_code
    print response
    data = json.loads(response.content)
    print(data)
    if response_code == 200:
        username = data['Login']['user']
        return True, username
    else:
        return False, None


if __name__ == '__main__':
    print is_authenticated('c133fef4-a389-437b-aecb-3463980292e4')
