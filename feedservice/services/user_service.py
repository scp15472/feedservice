import requests, json
USER_SERVICE_URL = 'http://localhost/userservice/'

def is_authenticated(token):
    url = USER_SERVICE_URL+'login/'+token
    response = requests.get(url)
    response_code = response.status_code
    data = json.loads(response.content)
    # print data
    if response_code==200:
        user_data = data['login']['user']
        return True,user_data
    else:
        return False

# if __name__ == '__main__':
#     print is_authenticated('c133fef4-a389-437b-aecb-3463980292e4')