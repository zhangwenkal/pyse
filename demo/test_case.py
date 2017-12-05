# -*- coding: utf-8 -*-
from pyse import TestCase, TestRunner
from parameterized import parameterized
import time


class loginTest(TestCase):
    # login success test case parameterized

    def test_login_success(self):
        '''
        login success test case
        '''
        self.driver.open("http://127.0.0.1:8080/jsds/security/login.jsp")
        self.driver.type("id=>username", 'admin')
        self.driver.type("id=>password", '123456')
        self.driver.type("id=>veriCode", '8888')
        self.driver.click("css=> div.loginform1 > a:nth-child(1) > img")
        self.assertText("css=> div.navbar-header.pull-left > a > label",u'智能终端操作平台服务器控制台')
        self.assertUrl("http://127.0.0.1:8080/jsds/vm/app/show.do")

    def test_reset(self):
        '''
        login reset test case
        '''
        try:
            a=['admin11','1234444','2222']
            b=['username','password','veriCode']
            c=['','',' ']
            self.driver.open("http://127.0.0.1:8080/jsds/security/login.jsp")
            for x, y in zip(a, b):
                self.driver.clear("id=>"+y)
                self.driver.type("id=>"+y, x)
            time.sleep(2)
            #a1=self.driver.js("return $('#username').attr('value');")
            for x, y in zip(a, b):
                self.assertattr("id=>"+y,"value", x)

            self.driver.click("css=> div.loginform1 > a:nth-child(2) > img")
            for z,w in zip(b, c):
                m1=self.driver.get_attribute("id=>"+z,"value")
                print(m1)
                self.assertattr("id=>"+z,"value",w)

            self.assertUrl("http://127.0.0.1:8080/jsds/security/login.jsp")
        except Exception as e:
            print(e)

class loginTest2(TestCase):
    ''' login error test case parameterized'''

    @parameterized.expand([
        (1, 'admin','123','8888','css=>#myform > div.wrong',u'用户密码不正确！！'),
        (2, '123','123456','8888','css=>#myform > div.wrong',u'用户密码不正确！！'),
        (3, 'admin','123456','888','css=>#myform > div.wrong',u'验证码不正确！！！'),
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
    runner = TestRunner('./',u'JSDS登录测试用例',u'测试环境：Chrome')
    runner.run()
