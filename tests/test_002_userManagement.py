import pytest,json,os,sys
p=os.path.join(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(p)
from base.method import Requests
from utils.readYaml import OperationYaml
from common.public import filePath


obj = Requests()
objYaml = OperationYaml()
addTeacherIdList = []


@pytest.mark.parametrize('datas', objYaml.readYaml('addTeacher.yaml'))
def test_001_addTeacher(datas):
    test_001_addTeacher.__doc__ = "用户管理：" + datas["casename"]
    with open(filePath("data","usertoken.txt"),"r") as f:
        datas["data"]["token"] = f.read()
    print(datas["data"])
    r = obj.post(
        url=datas["url"],
        json=datas["data"]
    )
    print(r.json())
    assert r.json()['result'] == datas['expect']['result']
    assert str(r.json()['message']) == datas['expect']['message']

@pytest.mark.parametrize('datas', objYaml.readYaml('findTeacher.yaml'))
def test_002_findTeacher(datas):
    test_002_findTeacher.__doc__ = "用户管理：" + datas["casename"]
    with open(filePath("data","usertoken.txt"),"r") as f:
        datas["data"]["token"] = f.read()
    print(datas["data"])
    r = obj.post(
        url=datas["url"],
        json=datas["data"]
    )
    print(r.json())
    assert r.json()['result'] == datas['expect']['result']
    assert str(r.json()['message']) == datas['expect']['message']
    for i in r.json()['data']:
        addTeacherIdList.append(i['uid'])

@pytest.mark.parametrize('datas', objYaml.readYaml('updateTeacher.yaml'))
def test_003_updateTeacher(datas):
    test_003_updateTeacher.__doc__ = "用户管理：" + datas["casename"]
    datas["data"]["data"]["Uid"] = addTeacherIdList[0]
    with open(filePath("data","usertoken.txt"),"r") as f:
        datas["data"]["token"] = f.read()
    print(datas["data"])
    r = obj.post(
        url=datas["url"],
        json=datas["data"]
    )
    print(r.json())
    assert r.json()['result'] == datas['expect']['result']
    assert str(r.json()['message']) == datas['expect']['message']

@pytest.mark.parametrize('datas', objYaml.readYaml('deleteTeacher.yaml'))
def test_004_deleteTeacher(datas):
    test_004_deleteTeacher.__doc__ = "用户管理：" + datas["casename"]
    with open(filePath("data","usertoken.txt"),"r") as f:
        datas["data"]["token"] = f.read()
    for i in addTeacherIdList:
        d = {}
        d['Uid'] = i
        d['Status'] = 'D'
        datas['data']['data']['Statu_Params'].append(d)
    print(datas["data"])
    r = obj.post(
        url=datas["url"],
        json=datas["data"]
    )
    print(r.json())
    assert r.json()['result'] == datas['expect']['result']
    assert str(r.json()['message']) == datas['expect']['message']

if __name__ == '__main__':
    pytest.main(["-s", "-v", "test_002_userManagement.py"])