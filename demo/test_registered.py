__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from pyse import TestCase, TestRunner
from parameterized import parameterized
import time
import pytesseract,os
from PIL import Image

resultPath=os.getcwd()+"\\img"
class list_info_Test(TestCase):
    # login success test case parameterized

    def test_registered(self):
        '''
        registered test case
        '''
        self.driver.open("http://127.0.0.1:8080/jsds/security/login.jsp")
        self.driver.type("id=>username", 'admin')
        self.driver.type("id=>password", '123456')
        self.driver.type("id=>veriCode", '8888')
        self.driver.click("css=> div.loginform1 > a:nth-child(1) > img")
        self.assertText("css=> div.navbar-header.pull-left > a > label",u'智能终端操作平台服务器控制台')
        self.assertUrl("http://127.0.0.1:8080/jsds/vm/app/show.do")
        self.driver.click("css=>#sidebar > ul > li:nth-child(1)")
        """
        1.断言机器码，iframe标签，先切换switch进去
        """
        self.driver.switch_to_frame('name=>manabox')
        self.assertText('xpath=>//input[@id="machineCode"]/../p[1]',u"机器特征码：")
        # a=self.driver.get_text('xpath=>//input[@id="machineCode"]/../p[1]')
        # print(a)
        self.assertnoteq_js(" return $(\"input[name='machineCode']\").val()",'')
        # b=self.driver.js("return $(\"input[name='machineCode']\").val()")
        # print(b)
        """
        2.上传liscense文件
        """
        self.driver.type("name=>licenseFile",'E:\jsds_liscence\LS201703100015.dat')
        self.driver.click("id=>btnImport")
        #提示框，点击确定按钮
        self.driver.accept_alert()
        self.driver.accept_alert()
        a=self.driver.js('return $("input[name=\'licenseFile\']").val()')
        self.assertIn('LS201703100015.dat',a)
        #iframe标签，switch出去
        self.driver.switch_to_frame_out()

        """
        3.服务器信息
        """
        #获取识别码，然后断言
        self.driver.click('xpath=>//*[@id="sidebar"]/ul/li[2]/a')
        self.driver.switch_to_frame('name=>manabox')
        c=self.driver.get_text("id=>mac")
        self.assertIn('本机标识码：',c)
        c1=self.driver.get_text('xpath=>//*[@id="mac"]/a')
        c1=len(c1)
        self.assertGreater(c1,3)
        self.driver.switch_to_frame_out()
        """
        4.安装服务器组件
        """
        # self.driver.click("css=>#sidebar > ul > li:nth-child(3) > a")
        # self.driver.type("name=>urlinput","E:\zs4s\\2017_10_09\jsds-server-updatesite_win32_x86_v1.1")

        """
        5.上传签名文件
        """
        self.driver.click("xpath=>//*[@id=\"sidebar\"]/ul/li[7]/a")
        self.driver.switch_to_frame('name=>manabox')
        self.driver.type("name=>bundle","E:\jsds_1.2\security.zip")
        self.driver.submit("id=>submitButton")
        self.assertText('#result > a','http://127.0.0.1:8080/security')

if __name__ == '__main__':
    runner = TestRunner('./',u'JSDS登录后注册测试用例',u'测试环境：Chrome')
    runner.run()
