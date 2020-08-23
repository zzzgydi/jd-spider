# encoding=utf-8

import time
from utils.malls import MallOne, MallTwo
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 初始化 WebDriver
driver = Chrome(executable_path='./bin/chromedriver.exe')
# 全局保存结果
global_data = []

if __name__ == '__main__':
    try:
        # a_mall = MallOne(driver, False)
        a_mall = MallTwo(driver)
        a_mall.get_mall_urls()
        for link in a_mall.all_urls:
            print(link)
        # result = a_mall.run()
    finally:
        # WebDriver退出
        driver.quit()
