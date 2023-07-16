import requests

class YaDisk:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_catalog(self,path):
        header = self.get_headers()
        param1 = {"path": path, "overwrite": "true"}
        resp = requests.put("https://cloud-api.yandex.net/v1/disk/resources/", headers = header, params = param1)
        return resp.status_code


