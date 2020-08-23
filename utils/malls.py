# encoding=utf-8

from utils.jd_mall import JdMall
from selenium.webdriver import Chrome


class MallOne(JdMall):
    '''
    该类是爬取 光明低温乳品旗舰店
    '''
    def __init__(self, *args, **kwargs):
        JdMall.__init__(self, *args, **kwargs)
        self.mall_name = "光明低温乳品旗舰店"

    def get_mall_urls(self):
        # 爬取的店的地址
        url_format = "https://mall.jd.com/view_search-653995-0-0-1-24-{}.html"
        url_index = 1
        driver = self.driver
        is_continue = True
        last_item_len = 0
        while is_continue:
            self.sleep()
            url = url_format.format(url_index)
            driver.get(url)
            css_select = "div.j-module div.jItem>div.jPic>a"
            all_items = driver.find_elements_by_css_selector(css_select)
            # 获取到所有商品id
            all_items = [item.get_attribute("href") for item in all_items]
            if len(all_items) < last_item_len:
                is_continue = False
            else:
                url_index += 1
                last_item_len = len(all_items)
            self.add_task_list(all_items)
        pass


class MallTwo(JdMall):
    '''
    该类是爬取 蒙牛低温乳品京东自营旗舰店
    '''
    def __init__(self, *args, **kwargs):
        JdMall.__init__(self, *args, **kwargs)
        self.mall_name = "蒙牛低温乳品京东自营旗舰店"

    def get_mall_urls(self):
        # 爬取的店的地址
        url = "https://mall.jd.com/index-1000078305.html"
        driver = self.driver
        driver.get(url)
        self.sleep(2)
        # 把该页商品展示部分的链接全爬了
        all_links = driver.find_elements_by_css_selector("div.J_layoutBg a")
        all_links = [item.get_attribute("href") for item in all_links]
        all_links = [item for item in all_links if item.find("item.jd.com") != -1]
        self.add_task_list(all_links)


class MallThree(JdMall):
    '''
    该类是爬取 简爱低温乳品京东自营旗舰店
    '''
    def __init__(self, *args, **kwargs):
        JdMall.__init__(self, *args, **kwargs)
        self.mall_name = "简爱低温乳品京东自营旗舰店"

    def get_mall_urls(self):
        # 爬取的店的地址
        url = "https://mall.jd.com/index-1000118193.html"
        driver = self.driver
        driver.get(url)
        self.sleep(1)
        # 把该页商品展示部分的链接全爬了
        all_links = driver.find_elements_by_css_selector("div.d-hotSpot a")
        all_links = [item.get_attribute("href") for item in all_links]
        all_links = [item for item in all_links if item.find("item.jd.com") != -1]
        self.add_task_list(all_links)


class MallFour(JdMall):
    '''
    该类是爬取 伊利低温乳品京东自营旗舰店
    '''
    def __init__(self, *args, **kwargs):
        JdMall.__init__(self, *args, **kwargs)
        self.mall_name = "伊利低温乳品京东自营旗舰店"

    def get_mall_urls(self):
        # 爬取的店的地址
        url = "https://mall.jd.com/index-1000091721.html"
        driver = self.driver
        driver.get(url)
        self.sleep(1)
        # 把该页商品展示部分的链接全爬了
        all_links = driver.find_elements_by_css_selector("div.layout-container a")
        all_links = [item.get_attribute("href") for item in all_links]
        all_links = [item for item in all_links if item.find("item.jd.com") != -1]
        self.add_task_list(all_links)
        # 再爬一下列表
        url = "https://mall.jd.com/view_search-709952-0-99-1-24-1.html"
        driver = self.driver
        driver.get(url)
        self.sleep(1)
        css_select = 'div.J_LayoutArea a'
        all_links = driver.find_elements_by_css_selector(css_select)
        all_links = [item.get_attribute("href") for item in all_links]
        all_links = [item for item in all_links if item.find("item.jd.com") != -1]
        self.add_task_list(all_links)


class MallFive(JdMall):
    '''
    该类是爬取 卡士（CLASSY.KISS）京东自营旗舰店
    '''
    def __init__(self, *args, **kwargs):
        JdMall.__init__(self, *args, **kwargs)
        self.mall_name = "卡士（CLASSY.KISS）京东自营旗舰店"

    def get_mall_urls(self):
        # 爬取的店的地址
        url = "https://mall.jd.com/index-1000091721.html"
        driver = self.driver
        driver.get(url)
        self.sleep(1)
        # 把该页商品展示部分的链接全爬了
        all_links = driver.find_elements_by_css_selector("div.d-layout-row a")
        all_links = [item.get_attribute("href") for item in all_links]
        all_links = [item for item in all_links if item.find("item.jd.com") != -1]
        self.add_task_list(all_links)
