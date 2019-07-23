from enum import Enum
import json
from urllib import request
from urllib import parse
from urllib.error import HTTPError
import io
import mimetypes
import uuid
from collections import namedtuple
from pprint import pprint

class BaseRequest():

    class SimpleMethod(Enum):
        GET = "GET"
        DELETE = "DELETE"

    class NonSimpleMethod(Enum):
        POST = "POST"
        PUT = "PUT"
        PATCH = "PATCH"

    class ContentType(Enum):
        TEXTPLAIN = "text/plain"
        JSON = "application/json"
        URLENCODED = "application/x-www-form-urlencoded"
        MULTIPART = "multipart/form-data"

        JPEG = "image/jpeg"
        PNG = "image/png"
        PDF = "application/pdf"

        @classmethod
        def get_filename_extension(cls, content_type):
            filename_extension = ""
            if content_type == cls.JPEG.value:
                filename_extension = ".jpeg"
            elif content_type == cls.PNG.value:
                filename_extension = ".png"
            elif content_type == cls.PDF.value:
                filename_extension = ".pdf"

            return filename_extension

class URLLibUtils(BaseRequest):

    def __init__(self, url, http_method=BaseRequest.SimpleMethod.GET, parameters={}, headers={}, content_type=BaseRequest.ContentType.TEXTPLAIN):
        self.url = url
        self.http_method = http_method
        self.parameters = parameters
        self.headers = headers
        self.content_type = content_type

    def urlopen(self):

        if isinstance(self.http_method, BaseRequest.SimpleMethod) and (self.parameters != {}):
            self.parameters = "?" + parse.urlencode(self.parameters) + "/"
            self.url += self.parameters

        req = request.Request(self.url, headers=self.headers, method=self.http_method.value)
        content_type = self.content_type.value

        data = None

        if isinstance(self.http_method, BaseRequest.NonSimpleMethod):
            if content_type == BaseRequest.ContentType.JSON.value:
                data = json.dumps(self.parameters).encode('utf-8')
            elif content_type == BaseRequest.ContentType.URLENCODED.value:
                data = bytes(parse.urlencode(self.parameters), encoding='utf8')
            elif content_type == BaseRequest.ContentType.MULTIPART.value:
                data, content_type = self._get_multipart_form(self.parameters)
            # elif content_type == BaseRequest.ContentType.TEXTPLAIN.value:
            #     print(BaseRequest.ContentType.TEXTPLAIN.value)

            req.data = data
        req.add_header('Content-type', content_type)
        result = self._validate_response(req)
        return result

    def _validate_response(self, req):
        Result = namedtuple('Result', 'status_code response')
        status_code = None
        try:
            response = request.urlopen(req, timeout=60)
            status_code = response.getcode()
            if status_code not in range(200, 300):
                raise HTTPError('status code not equal to 2xx')
            json_string = response.read().decode('utf-8')
            dict_from_json = json.loads(json_string)
            result = Result(status_code=status_code, response=dict_from_json)
        except HTTPError as e:
            result = Result(status_code=status_code, response=e)
        except Exception as e:
            result = Result(status_code=status_code, response=e)
        finally:
            return result

    def _seperate_files_and_pure_parameters(self, parameters):
        form_fields, files = [], []
        for key, value in parameters.items():
            if isinstance(value, io.BufferedReader):
                body = value.read()
                mimetype = (
                        mimetypes.guess_type(value.name)[0] or
                        'application/octet-stream'
                )
                files.append((key, value.name, mimetype, body))
            else:
                form_fields.append((key, value))
        return form_fields, files

    def _get_multipart_form(self, parameters):

        form_fields, files = self._seperate_files_and_pure_parameters(parameters)
        boundary = uuid.uuid4().hex.encode('utf-8')
        content_type = BaseRequest.ContentType.MULTIPART.value + '; boundary={}'.format(boundary.decode('utf-8'))

        buffer = io.BytesIO()
        boundary = b'--' + boundary + b'\r\n'

        for name, value in form_fields:
            buffer.write(boundary)
            buffer.write(('Content-Disposition: form-data; '
                'name="{}"\r\n').format(name).encode('utf-8'))
            buffer.write(b'\r\n')
            buffer.write(value.encode('utf-8'))
            buffer.write(b'\r\n')

        for f_name, filename, f_content_type, body in files:
            buffer.write(boundary)
            buffer.write(('Content-Disposition: file; '
                'name="{}"; filename="{}"\r\n').format(
                f_name, filename).encode('utf-8'))
            buffer.write('Content-Type: {}\r\n'.format(f_content_type).encode('utf-8'))
            buffer.write(b'\r\n')
            buffer.write(body)
            buffer.write(b'\r\n')

        buffer.write(b'--' + boundary + b'--\r\n')
        return buffer.getvalue(), content_type


simple_method = URLLibUtils.SimpleMethod
non_simple_method = URLLibUtils.NonSimpleMethod
content_type = URLLibUtils.ContentType

import inspect
import time
#todo 未來新增 project 的環境變數
from projects.Project_A.resources import Environments as Project_A_ENV
from projects.Project_B.resources import Environments as Project_B_ENV

def send_request(url, http_method=URLLibUtils.SimpleMethod.GET, parameters={}, headers={}, content_type=URLLibUtils.ContentType.TEXTPLAIN):

    calframe = inspect.getouterframes(inspect.currentframe(), 2)
    project_path = None
    caller_method = None
    try:
        #呼叫來源的檔案 ex: /Users/(user_name)/Documents/........../projects/Project_A/apps/App_A1.py
        project_path = calframe[1][1]
        #呼叫來源的方法 project, app ex: App_A1.route_A101_GET_JSON()
        caller_method = calframe[2][4][1]
    except:
        pass

    # todo 未來新增/修改 project 的 server
    if "Project_A" in project_path:
        server = Project_A_ENV.server
    elif "Project_B" in project_path:
        server = Project_B_ENV.server

    url = server + url
    start_time = time.perf_counter()
    utils = URLLibUtils(url, http_method, parameters, headers, content_type)
    result = utils.urlopen()
    end_time = time.perf_counter()
    run_time = end_time - start_time

    pprint(f"--------------Finished {caller_method} in {run_time:.4f} secs--------------")
    pprint(result.response)
