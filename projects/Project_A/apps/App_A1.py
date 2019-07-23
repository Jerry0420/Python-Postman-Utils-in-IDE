from tools.RequestUtils import Project_A_ENV, simple_method, non_simple_method, send_request, content_type

def route_A101_GET_JSON():
    url = "/users/info/{user_id}/".format(user_id=Project_A_ENV.user_id)
    parameters = {}
    headers = {
        "Authorization": Project_A_ENV.auth_token
    }
    send_request(url, simple_method.GET, parameters, headers, content_type.TEXTPLAIN)

def route_A102_POST_JSON():
    url = "/users/account/reset-pwd/"
    parameters = {
        "user": {
            "email": "xxxxx@gmail.com",
            "password": "oooooooooo"
        }
    }
    headers = {
        "Authorization": Project_A_ENV.auth_token
    }
    send_request(url, non_simple_method.POST, parameters, headers, content_type.JSON)

def route_A103_POST_MULTIPART():
    url = "/users/info/{user_id}/".format(user_id=Project_A_ENV.user_id)
    parameters = {
        "info": {
            "user_name": "jerry wang",
            "birth_date":1537512987000,
            "parent": [
                {
                  "father_name": "xxxxx",
                  "mother_name":"oooooo"
                }
            ],
            "mobile":"0900000000"
        },
        "avatar": Project_A_ENV.picture_file
    }
    headers = {
        "Authorization": Project_A_ENV.auth_token
    }
    send_request(url, non_simple_method.POST, parameters, headers, content_type.MULTIPART)