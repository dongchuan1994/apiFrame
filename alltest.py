import pytest,time,os,shutil
from common.public import filePath,mkdir,sendEmail


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d_%H-%M", time.localtime())
    path = filePath('report',now)
    mkdir(path)
    path = filePath('report', 'assets')
    mkdir(path)
    filedir = 'report/' + now
    path = filePath(filedir,'测试报告.html')
    path = "--html=" + path
    # pytest.main([path])
    pytest.main(['--alluredir ./allure-results'])
    p = os.path.join(os.path.dirname(__file__),"report","assets","style.css")
    p1 = os.path.join(os.path.dirname(__file__),"report",now,"assets","style.css")
    shutil.copy(p1,p)
    p = os.path.join(os.path.dirname(__file__), "report", "测试报告.html")
    p1 = os.path.join(os.path.dirname(__file__), "report", now, "测试报告.html")
    shutil.copy(p1, p)
    sendEmail()

    # shutil.copy("E:\\pytest\\apiFrame\\report\\2020-12-01_13-39\\assets\\style.css","E:\\pytest\\apiFrame\\report\\style.css")
    # os.system("pytest  --alluredir report/" + now)
    # path_report = path + '\html'
    # os.system("allure generate " + path + " -o " + path_report + " --clean")
