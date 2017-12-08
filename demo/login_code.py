__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import pytesseract,os
from PIL import Image
from pyse import TestCase, TestRunner

'''
#执行不了
resultPath=os.path.join(os.getcwd()+"\\img","test.text")
print(resultPath)
image=Image.open(r"F:\git\pyse\demo\img\code.png")
vcode=pytesseract.image_to_string(image)
with open(resultPath, 'w') as f:
    f.write(vcode)
'''
#os.chdir("D:\PF\python\Lib\site-packages\pytesseract")
resultPath=os.getcwd()+"\\img"
class loginTest(TestCase):
    # login success test case parameterized

    def test_login_code(self):
        '''
        login success test case
        '''
        self.driver.open("http://127.0.0.1:8080/jsds/security/login.jsp")
        self.driver.max_window()
        self.driver.get_windows_img(os.path.join(resultPath,'aa.png'))
        imgelement =self.driver.get_element("id=>loginrandom")
        location = imgelement.location   #获取验证码x，y轴
        size=imgelement.size             #获取验证码的长宽
        rangle=(int(location['x']),int(location['y']),
                int(location['x']+size['width']),
                int(location['y']+size['height']))         #写成我们需要的坐标
        i=Image.open(os.path.join(resultPath,'aa.png'))   #打开截图
        frame4=i.crop(rangle)                              #使用Image的crop函数，获取我们需要的区域
        frame4.save(os.path.join(resultPath,'bb.png'))
        qq=Image.open(os.path.join(resultPath,'bb.png'))
        vecode=pytesseract.image_to_string(qq)    #使用image_to_string识别验证码
        print(vecode)
if __name__ == '__main__':
    r=loginTest()
    r.test_login_code()


