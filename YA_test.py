from YADisk import YaDisk
import pytest, requests, os

@pytest.mark.parametrize (
    "path",
    [('Папочка_1'),('Папочка_2')]
)
def test_on_successful_create(path):
    TOKEN = os.getenv('TOKEN')
    YD = YaDisk(TOKEN) 
    header = YD.get_headers()
    param1 = {"path": path, "limit": 0}
    resp = requests.get("https://cloud-api.yandex.net/v1/disk/resources/", headers = header, params = param1)
# Для универсальности проверки: если папка уже создана - будет изначально удалена
    if resp.status_code in (200,201):
        param1 = {"path": path,"permanently":True}
        requests.delete("https://cloud-api.yandex.net/v1/disk/resources/", headers = header, params = param1)
    res_code = YD.create_catalog(path)
    assert res_code in (200,201) 
    param1 = {"path": path, "limit": 0}
    resp = requests.get("https://cloud-api.yandex.net/v1/disk/resources/", headers = header, params = param1)
    assert resp.status_code in (200,201)


@pytest.mark.parametrize (
        "path", ['Папочка_1']
)
def test_on_error_availability_catalog(path):
    TOKEN = os.getenv('TOKEN')
    YD = YaDisk(TOKEN) 
    header = YD.get_headers()
    param1 = {"path": path, "limit": 0}
    resp = requests.get("https://cloud-api.yandex.net/v1/disk/resources/", headers = header, params = param1)
    param1 = {"path": path, "overwrite": "true"}
    if resp.status_code not in (200,201):
    # можно было запускать тесты последовательно, но для универсальности сделано так:
    # проверяется - есть ли уже данный каталог на ЯДиске, если нет - создается изначально, а затем 
    #повторно производится попытка создания того же каталога  
        requests.put("https://cloud-api.yandex.net/v1/disk/resources/", headers = header, params = param1)  
    resp = requests.put("https://cloud-api.yandex.net/v1/disk/resources/", headers = header, params = param1)
    assert resp.status_code == 409   
  
@pytest.mark.parametrize (
        "path", ['Папочка_1']
)
def test_on_not_authorized(path):
    YD = YaDisk('TOKEN') 
    res_code = YD.create_catalog(path)
    assert res_code == 401
    



