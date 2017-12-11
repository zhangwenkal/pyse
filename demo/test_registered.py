__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from pyse import TestCase, TestRunner
from parameterized import parameterized
import time
import pytesseract,os
from PIL import Image

resultPath=os.getcwd()+"\\img"
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
        self.driver.click("css=>#sidebar > ul > li:nth-child(1)")
        self.assertText('xpath=>//input[@id="machineCode"]/../p[1]',u"机器特征码：")
        self.assertnoteq_text(" return $(\"input[name='machineCode']\").val()",'')

if __name__ == '__main__':
    runner = TestRunner('./',u'JSDS登录后注册测试用例',u'测试环境：Chrome')
    runner.run()
