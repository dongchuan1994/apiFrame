import pytest,json,os,sys
from base.method import Requests
p=os.path.join(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(p)
from utils.readYaml import OperationYaml
from common.public import filePath,getUrl

obj = Requests()
objYaml = OperationYaml()
@pytest.mark.parametrize('datas', objYaml.readYaml('login.yaml'))
def test_001_SSOLogin(datas):
    test_001_SSOLogin.__doc__ = "登录功能测试：" + datas["casename"]
    print(datas['data'])
    r = obj.post(
        url=datas["url"],
        json=datas["data"]
    )
    print(r.json())
    assert r.json()['result'] == datas['expect']['result']
    assert str(r.json()['message']) == datas['expect']['message']
    try:
        with open(filePath('data','usertoken.txt'),'w') as f:
            f.write(r.json()['data']['userToken'])
    except:
        pass

def test_002_GetAppList():
    test_002_GetAppList.__doc__ = "获取应用列表"
    url = getUrl() + "/service/app/GetAppList"
    datas = """
    {
        "version":"2.0",
        "data":{},
        "token":"",
        "orgcode":"865100000001",
        "Operation":{
            "UserID":"admin",
            "UserName":"admin",
            "UserType":"0",
            "OpType":"查询",
            "OpRemark":"查询"
        }
    }"""
    datas = json.loads(datas)
    with open(filePath("data","usertoken.txt"),"r") as f:
        datas["token"] = f.read()
    print(datas)
    r = obj.post(
        url=url,
        json=datas
    )
    print(r.json())
    assert r.json()['result'] == True

if __name__ == '__main__':
    pytest.main(["-s", "-v", "test_001_login.py"])