from tools.RequestUtils import Project_B_ENV, simple_method, non_simple_method, send_request, content_type

def route_B201_GET_JSON():
    url = "/users/info/{user_id}/".format(user_id=Project_B_ENV.user_id)
    parameters = {}
    headers = {
        "Authorization": Project_B_ENV.auth_token
    }
    send_request(url, simple_method.GET, parameters, headers, content_type.TEXTPLAIN)

def route_B202_POST_JSON():
    url = "/users/account/reset-pwd/"
    parameters = {
        "user": {
            "email": "xxxxx@gmail.com",
            "password": "oooooooooo"
        }
    }
    headers = {
        "Authorization": Project_B_ENV.auth_token
    }
    send_request(url, non_simple_method.POST, parameters, headers, content_type.JSON)

def route_B203_POST_MULTIPART():
    url = "/users/info/{user_id}/".format(user_id=Project_B_ENV.user_id)
    parameters = {
        "info": str({
            "user_name": "jerry wang",
            "birth_date":1537512987000,
            "parent": [
                {
                  "father_name": "xxxxx",
                  "mother_name":"oooooo"
                }
            ],
            "mobile":"0900000000"
        }),
        "avatar": Project_B_ENV.picture_file
    }
    headers = {
        "Authorization": Project_B_ENV.auth_token
    }
    send_request(url, non_simple_method.POST, parameters, headers, content_type.MULTIPART)