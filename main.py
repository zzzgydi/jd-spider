# encoding=utf-8

import time
from utils.malls import MallOne, MallTwo, MallThree, MallFour, MallFive
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from flask import Flask, render_template, jsonify, make_response
import logging

# 初始化 WebDriver
driver = Chrome(executable_path='./bin/chromedriver.exe')
# 初始化 server 相关
app = Flask(__name__, static_folder='web/dist/static', template_folder='web/dist')
# 全局保存结果
global_data = []
# 关闭该死的日志
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@app.route('/')
def index_html():  # 注册 server 监听
    return render_template('index.html')


@app.route('/get_data')
def get_data():  # 注册 server 监听
    return jsonify(global_data)


@app.after_request
def af_request(resp):  # 跨域处理
    resp = make_response(resp)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return resp


if __name__ == '__main__':
    # malls_class = [MallOne, MallTwo, MallThree, MallFour, MallFive]
    malls_class = [MallFour, MallFive]
    for mall in malls_class:
        mall_ins = mall(driver, auto_add=True, sleep_time=0.1)
        result = mall_ins.run(limit=10)  # limit参数测试时使用
        # result = mall_ins.run()
        global_data.append(result)
    print("[INFO]: 正在关闭爬虫，开启服务器...")
    # WebDriver退出
    driver.quit()
    print("[INFO]: 请打开浏览器查看结果: http://localhost:7788")
    print("[INFO]: 正在运行，请勿关闭...")
    # 打开server
    app.run(host="localhost", port=7788)
