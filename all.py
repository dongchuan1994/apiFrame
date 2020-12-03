import pytest,time,os

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d_%H-%M", time.localtime())
    path = './allureReport/' + now + '/allure'
    pytest.main(['--alluredir',path])

    reportPath = 'allure generate ./allureReport/' + now + '/allure -o ./allureReport/' + now + '/report --clean'
    os.system(reportPath)

    pytest.main(['--alluredir', 'allureReport/allure'])