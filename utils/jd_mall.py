# encoding=utf-8

import time
from abc import ABCMeta, abstractmethod
from utils.jd_item import JdItem
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class JdMall(metaclass=ABCMeta):
    '''
    该类继承抽象基类
    一个抽象基类只能被继承，而其本身无法被实例化
    '''
    def __init__(self, driver: Chrome, auto_add=False, sleep_time=0):
        self.mall_name = "none"
        # 是否在爬取商品页的时候，自动将商品种类爬取下来
        self.auto_add = auto_add
        # 爬取每个商品的间隔时间，以秒为单位
        self.sleep_time = sleep_time
        # 检测链接是不是爬过了
        self.url_set = set()
        # 某个商店里的所有要爬的
        self.all_urls = []
        # 保存WebDriver实例
        self.driver = driver

    @abstractmethod
    def get_mall_urls(self):
        '''
        虚函数
        爬取商城的所有需要的商品的链接
        不同的商店，获取方式不一样，该方法需要继承实现
        '''
        print("error")
        pass

    def sleep(self, t=0):
        '''
        每个请求间应该停一下，害怕被限制ip
        '''
        if t > 0:
            time.sleep(t)
        elif self.sleep_time > 0:
            time.sleep(self.sleep_time)

    def add_task_list(self, urls: list):
        '''
        批量添加任务
        '''
        for url in urls:
            self.add_task(url)

    def add_task(self, url: str):
        '''
        添加任务
        '''
        if not url:
            return
        sku_id = self.filter_url(url)
        if sku_id not in self.url_set:
            self.url_set.add(sku_id)
            if sku_id == url:
                url = "https://item.jd.com/" + sku_id + ".html"
            self.all_urls.append(url)

    def get_task(self):
        '''
        获取一个任务链接 —— 商品详情链接
        '''
        if len(self.all_urls) > 0:
            return self.all_urls.pop(0)
        return None

    def filter_url(self, url: str) -> str:
        '''
        将商品的链接去除一些域名前缀，仅将sku-id作为键值
        '''
        url = url.replace("https://item.jd.com/", "")
        url = url.replace("http://item.jd.com/", "")
        url = url.replace(".html", "")
        return url

    def wait_page_load(self, wait_element: str):
        '''
        传入CSS_SELECTOR的规则
        使用WebDriverWait等待该元素加载完成
        '''
        dw = WebDriverWait(self.driver, 10)
        dw.until(EC.presence_of_element_located((By.CSS_SELECTOR, wait_element)))
        pass

    def get_sku_info(self, url: str) -> JdItem:
        '''
        解析商品详情页面，获取商品的信息
        '''
        driver = self.driver
        driver.get(url)
        # 等待页面加载完成
        wait_element = "span.p-price>span.price"
        self.wait_page_load(wait_element)
        self.sleep()

        # 商品名称
        sku_name = driver.find_element_by_class_name('sku-name').text
        # 价格
        cur_price = driver.find_element_by_css_selector(wait_element).text
        try:
            # 不是一家店的不要
            mall_name = driver.find_element_by_css_selector('div.popbox-inner h3').text
            if mall_name and mall_name != self.mall_name:
                return None
        except:
            pass
        try:
            # 旧的价格也可能没有
            old_price = driver.find_element_by_css_selector("span.pricing>del").text[1:]
        except:
            old_price = ""
        try:
            # 获取plus价格
            plus_price = driver.find_element_by_css_selector("div.plus-price span.price").text[1:]
        except:
            plus_price = ""
        try:
            # 获取粉丝价格
            fans_price = driver.find_element_by_css_selector("div.fans-price span.price").text[1:]
        except:
            fans_price = ""
        try:
            # 活动名称
            activity_type = driver.find_element_by_css_selector("div.activity-type").text
        except:
            activity_type = ""
        try:
            # 优惠券
            quan_items = driver.find_elements_by_css_selector("span.quan-item>span.text")
            quan_items = [item.text for item in quan_items]
        except:
            quan_items = []
        try:
            # 促销
            prom_items = driver.find_elements_by_css_selector(".prom-item")
            prom_items = [item.find_elements_by_tag_name("em") for item in prom_items]
            prom_items = [[item.text for item in l] for l in prom_items]
            prom_items = [(" ".join(l)).strip() for l in prom_items]
        except:
            prom_items = []
        try:
            more_prom = driver.find_elements_by_css_selector("div.more-prom-ins em")
            more_prom = [item.text for item in more_prom]
            prom_items += more_prom
        except:
            pass
        try:
            prom_gift = driver.find_elements_by_css_selector("div.prom-gifts")
            prom_gift = [item.text for item in prom_gift]
            prom_items += prom_gift
        except:
            pass
        # 判断是否自动增加那个链接
        if self.auto_add:
            try:
                more_skus = driver.find_elements_by_css_selector("#choose-attrs div.item")
                more_skus = [item.get_attribute("data-sku") for item in more_skus]
                self.add_task_list(more_skus)
            except:
                pass
        return JdItem(url, sku_name, cur_price, old_price, plus_price, fans_price, activity_type, quan_items,
                      prom_items)

    def run(self, limit=float('inf')) -> dict:
        '''
        执行流程，返回结果
        - 先获取商店的所有链接
        - 不断的获取链接并解析
        '''
        item_list, err_list = [], []
        try:
            self.get_mall_urls()
        except:
            err = "解析商品列表异常:" + self.mall_name
            print("[Error]:", err)
            err_list.append(err)
        a_url, idx = self.get_task(), 0
        while a_url and idx < limit:
            try:
                sku_item = self.get_sku_info(a_url)
                if sku_item:
                    # 可以将对象转成字典
                    item_list.append(sku_item.__dict__)
            except:
                err = "解析地址异常:" + a_url
                print("[Error]:", err)
                err_list.append(err)
            a_url = self.get_task()
            idx += 1
        print("[DONE]:", self.mall_name)
        result = {"name": self.mall_name, "item_list": item_list, "err_list": err_list}
        return result

    pass
