from pyse import TestCase, TestRunner
from parameterized import parameterized


class loginTest(TestCase):
    ''' login success test case parameterized'''

    def test_login_success(self):
        ''' login success test case '''
        self.driver.open("http://127.0.0.1:8080/jsds/security/login.jsp")
        self.driver.type("id=>username", 'admin')
        self.driver.type("id=>password", '123456')
        self.driver.type("id=>veriCode", '8888')
        self.driver.click("css=> div.loginform1 > a:nth-child(1) > img")
        self.assertUrl("http://127.0.0.1:8080/jsds/vm/app/show.do")

class loginTest2(TestCase):
    ''' login error test case parameterized'''

    @parameterized.expand([
        (1, 'admin','123','8888','css=>#myform > div.wrong','用户密码不正确！！'),
        (2, '123','123456','8888','css=>#myform > div.wrong','用户密码不正确！！'),
        (3, 'admin','123456','888','css=>#myform > div.wrong','验证码不正确！！！'),
    ])
    def test_login_error(self,name,search_key1,search_key2,search_key3,search_key4,search_key5):
        ''' login error test case : pyse '''
        self.driver.open("http://127.0.0.1:8080/jsds/security/login.jsp")
        self.driver.clear("id=>username")
        self.driver.type("id=>username", search_key1)
        self.driver.clear("id=>password")
        self.driver.type("id=>password", search_key2)
        self.driver.clear("id=>veriCode")
        self.driver.type("id=>veriCode", search_key3)
        self.driver.click("css=> div.loginform1 > a:nth-child(1) > img")
        self.assertText(search_key4,search_key5)
        self.assertUrl("http://127.0.0.1:8080/jsds/security/login.jsp")

if __name__ == '__main__':
    runner = TestRunner('./','JSDS登录测试用例','测试环境：Chrome')
    runner.run()

'''
说明：
'./' ： 指定测试目录。
'登录测试用例' ： 指定测试项目标题。
'测试环境：Chrome' ： 指定测试环境描述。
'''

