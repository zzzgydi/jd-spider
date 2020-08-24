# encoding=utf-8


class JdItem:
    def __init__(self, sku_url, sku_name, cur_price, old_price, plus_price, fans_price, activity_type, quan_items,
                 prom_items):
        self.sku_url = sku_url  # 商品链接
        self.sku_name = sku_name
        self.cur_price = cur_price
        self.old_price = old_price
        self.plus_price = plus_price
        self.fans_price = fans_price
        self.activity_type = activity_type
        self.quan_items = quan_items
        self.prom_items = prom_items

    def print_info(self):
        print("商品链接：", self.sku_url)
        print("商品名称：", self.sku_name)
        print("商品价格：", self.cur_price)
        print("商品原价格：", self.old_price)
        print("商品plus价格：", self.plus_price)
        print("商品粉丝价格：", self.fans_price)
        print("活动名称：", self.activity_type)
        print("优惠券：", self.quan_items)
        print("促销：", self.prom_items)
        print("=" * 20)
