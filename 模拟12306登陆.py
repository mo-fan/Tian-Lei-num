#Author:fanzhenzhen
from selenium import webdriver
import time
# from hashlib import md5
# import requests
from lxml import etree
from PIL import Image
from ChaoJiYing import Chaojiying_Client
from selenium.webdriver import ActionChains


def main():
    #模拟一个谷歌浏览器
    bro = webdriver.Chrome(executable_path=r"C:\Users\Administrator\Desktop\python资料\谷歌驱动\chromedriver.exe")
    #访问12306官网的登陆页面
    url = "https://kyfw.12306.cn/otn/resources/login.html"
    bro.get(url)
    time.sleep(2)
    # page_text = bro.page_source
    #点击账号登陆找到验证码识别并等待3秒钟进行页面加载
    num_go = bro.find_element_by_xpath("/html/body/div[2]/div[2]/ul/li[2]/a").click()
    bro.maximize_window()
    time.sleep(3)
    bro.save_screenshot("image.png")
    #定位到验证码对应的图片
    image_code = bro.find_element_by_id("J-loginImg")
    location = image_code.location   #验证码图片基于整张页面的左下角坐标
    size = image_code.size  #验证码图片的长和宽
    #裁剪的矩形（左下角和右上角的图标）
    rangle = (int(location["x"]),int(location["y"]),int(location["x"]+size["width"]),int(location["y"]+size["height"]))
    i = Image.open("image.png")
    frame = i.crop(rangle)
    frame.save("code.png")

    #使用打码平台进行验证码识别
    # chaojiying = Chaojiying_Client('fan1996', '19960919', '	902601')
    # im = open("code.png", 'rb').read()
    # result =  chaojiying.PostPic(im, 9004)["pic_str"]
    # print(result) #x1,y1|x2,y2|x3,y3 ==>[[x1,y1],[x2,y2],[x3,y3]]
    #
    # al_list = []    #[[x1,y1],[x2,y2],[x3,y3]] 每一个列表元素对应一个点的坐标，坐标对应的0,0点的坐标为验证码的左下角的坐标。
    # if "|" in result:
    #     list_1 = result.split("|")
    #     count_1 = len(list_1)
    #     for i in range(count_1):
    #         xy_list = []
    #         x = int(list_1[i].split(",")[0])
    #         y = int(list_1[i].split(",")[1])
    #         xy_list.append(x)
    #         xy_list.append(y)
    #         al_list.append(xy_list)
    # else:
    #     x = int(result.split(",")[0])
    #     y = int(result.split(",")[1])
    #     xy_list = []
    #     xy_list.append(x)
    #     xy_list.append(y)
    #     al_list.append(xy_list)
    #
    # #创建一个动作链进行验证码的点击
    # # action = ActionChains(bro)
    # for l in al_list:
    #     x = l[0]
    #     y = l[1]
    #     ActionChains(bro).move_to_element_with_offset(image_code,x,y).click().perform()    #perform()为让动作链立即执行
    #     time.sleep(1)
    # action.release()

    # 输入手机号和密码
    srarch_input_phone = bro.find_element_by_id("J-userName")
    srarch_input_phone.send_keys("手机号")
    time.sleep(0.5)
    search_input_password = bro.find_element_by_id("J-password")
    search_input_password.send_keys("密码")
    # 点击登录
    # main_go = bro.find_element_by_id("J-login").click()

    #获取点击登录后页面的信息
    time.sleep(2)
    page_text = bro.page_source
    print(page_text)

    #关闭浏览器
    time.sleep(5)
    bro.quit()




if __name__ == "__main__":
    main()
