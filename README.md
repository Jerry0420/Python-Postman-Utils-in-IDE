# Python-Postman-Utils-in-IDE

使用 Django/Flask...等 Python 後端框架開發 Restful API 時，可直接在 IDE 內測試 Restful API 的工具，如同 Postman。
* 以下以 Pycharm, Django 為範例

<a href="https://github.com/Jerry0420/Utils-for-Python-and-Django" title="Title">
參考此專案內的程式碼：Utils for Python and Django</a> 

## 前置作業
1. 在 projects 資料夾下為各專案，專案之下有 apps, resources 資料夾。ex: 此範例有 Project_A, Project_B
2. apps: Django 專案中各 apps 之下的所有 route。 Project_A 之下有 App_A1 和 App_A2 ， Project_B 之下有 App_B1 和 App_B2
3. resources/Environment.py 放置route 內需要用到的共同參數
4. 將 usage/Send.py 內 from...import 所需要的 project 及 apps
5. 將 tools/ResquestUtils.py 之中，send_request function 內加入新的 server   
* p.s. 記得在設計 Restful API 時將各 route 編號及命名，方便後續開發。

## 執行方式
1. 選定 usage/Send.py 檔案， 按 control + R or ccontrol + shift + R 即可執行
   
## 優勢
1. 不需在 IDE, Postman 之間進行切換，加快開發速度
2. 可以程式化的架構管理所有 route 所需的參數
3. 可批次且照順序的執行各個 route
   
## 顯示
route 執行完後，會在 console 內跑出類似以下的結果，可看到每條 route 執行的時間，以及 http response。

```
'-----------Finished App_A1.route_A101_GET_JSON()\n in 0.0064 secs-----------'
{'birth_date': 198475857, 'mobile': '0980888888', 'name': 'jerry wang'}
```
