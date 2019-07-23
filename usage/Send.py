from projects.Project_A.apps import App_A1, App_A2
from projects.Project_B.apps import App_B1, App_B2

'''
使用方法：
1. 在 projects 資料夾下為各專案，專案之下有 apps, resources 資料夾
    apps: Django 專案中各 apps 之下的所有 route
    resources: Environment.py 放置route 內需要用到的共同參數
2. 將 usage/Send.py 內 from...import 所需要的 project 及 apps
3. 將 tools/ResquestUtils.py 之中，send_request function 內加入新的 server

執行：
1. 選定 usage/Send.py 檔案， 按 control + R or ccontrol + shift + R 即可執行
'''

App_A1.route_A101_GET_JSON()
# App_A2.route_A203_POST_MULTIPART()

# App_B1.route_B102_POST_JSON()
# App_B2.route_B201_GET_JSON()