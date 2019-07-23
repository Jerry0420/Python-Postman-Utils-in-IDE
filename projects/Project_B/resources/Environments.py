from pathlib import Path

server = "http://127.0.0.1:8000/project_b/api/v7"
user_id = 1
picture_file = open(Path(__file__).absolute().parent / 'meta' / 'example.jpg', 'rb')
auth_token = "Bearer " \
             "eyJ0eXAiOiJKV1efrJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJyb2xlX2lkIjoxLCJleHAiOjE1NTY4OTcyMDMuMzA1Mzc0LCJpYXQiOjE1NTYyOTI0MDMuMzA1Mzc0fQ.fJ53xQfCLQOz61IqV68gxnfoHkPyQWBJmqKD9ppUkhU"
