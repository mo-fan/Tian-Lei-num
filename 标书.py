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
    #访问官网的登陆页面
    url = "https://www.okcis.cn/search/"
    bro.get(url)
    time.sleep(2)
    # page_text = bro.page_source
    #点击账号登陆找到验证码识别并等待3秒钟进行页面加载
    #num_go = bro.find_element_by_xpath("/html/body/div[2]/div[2]/div/ul/li[4]/div/a")
    above = bro.find_element_by_xpath("/html/body/div[2]/div[2]/div/ul/li[4]/div/a")
    ActionChains(bro).move_to_element(above).perform()
    time.sleep(3)
    bro.switch_to_frame("site-top-login-iframe")

    # 输入手机号和密码
    srarch_input_phone = bro.find_element_by_xpath("//*[@id='ptlogin']/ul[2]/form/li[1]/div/input")
    srarch_input_phone.send_keys("手机号")
    time.sleep(0.5)
    search_input_password = bro.find_element_by_xpath("//*[@id='ptlogin']/ul[2]/form/li[2]/div/input")
    search_input_password.send_keys("密码")
    bro.maximize_window()
    bro.save_screenshot("image.png")
    #定位到验证码对应的图片
    image_code = bro.find_element_by_id("yztp")
    location = image_code.location   #验证码图片基于整张页面的左下角坐标
    size = image_code.size  #验证码图片的长和宽
    #裁剪的矩形（左下角和右上角的图标）
    rangle = (int(location["x"]+900),int(location["y"]+40),int(location["x"]+900+size["width"]),int(location["y"]+40+size["height"]))
    i = Image.open("image.png")
    frame = i.crop(rangle)
    frame.save("code.png")
    print(location,size)

    #使用打码平台进行验证码识别
    chaojiying = Chaojiying_Client('fan1996', '19960919', '	902601')
    im = open("code.png", 'rb').read()
    result =  chaojiying.PostPic(im, 6001)["pic_str"]
    print(result) #x1,y1|x2,y2|x3,y3 ==>[[x1,y1],[x2,y2],[x3,y3]]

    #输入验证码
    search_input_yzm = bro.find_element_by_xpath("//*[@id='ptlogin']/ul[2]/form/li[4]/div/input")
    search_input_yzm.send_keys(result)

    time.sleep(0.5)

    # 点击登录
    bro.find_element_by_xpath("//*[@id='ptlogin']/ul[2]/form/li[6]/input").click()

    time.sleep(2)

    #详情页内容获取
    search_input_find = bro.find_element_by_id("k1")
    search_input_find.send_keys("全民健身")
    time.sleep(0.5)
    bro.find_element_by_xpath("//*[@id='search-form-on']/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[5]/p[1]/label/input").click()
    bro.find_element_by_xpath("//*[@id='search-form-on']/div/div[2]/div[2]/div[5]/div[1]/label[7]/input").click()
    bro.find_element_by_xpath("//*[@id='search-form-on']/div/div[2]/div[2]/div[6]/div[1]/label[8]/input").click()

    time.sleep(0.5)
    bro.find_element_by_xpath("//*[@id='search-form-on']/div/div[2]/div[3]/a").click()

    #获取点击登录后页面的信息
    time.sleep(2)
    page_text = bro.page_source
    print(page_text)

    #关闭浏览器
    time.sleep(5)
    bro.quit()




if __name__ == "__main__":
    main()
