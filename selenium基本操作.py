#Author:fanzzhenzhen
from selenium import webdriver
from time import sleep

def main():

    bro = webdriver.Chrome(executable_path=r"C:\Users\Administrator\Desktop\python资料\谷歌驱动\chromedriver.exe")
    url = "https://www.baidu.com/"
    bro.get(url)
    search_input = bro.find_element_by_id("kw")
    search_input.send_keys("西安")
    btn = bro.find_element_by_xpath("//*[@id='su']")
    btn.click()
    sleep(3)

    jscode = "window.scrollTo(0,document.body.scrollHeight)"
    bro.execute_script(jscode)

    sleep(3)
    bro.quit()

if __name__ == "__main__":
    main()
