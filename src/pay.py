# -*-coding:utf-8 -*-

import json

product = [{'name': '世园会五十国钱币册', 'id': '001001', 'unit': '册', 'price': 998.00},
           {'name': '2019北京世园会纪念银章大全40g', 'id': '001002', 'unit': '盒', 'price': 1380.00, 'discount': ['可使用9折打折券']},
           {'name': '招财进宝', 'id': '003001', 'unit': '条', 'price': 1586.00, 'discount': ['9折']},
           {'name': '水晶之恋', 'id': '003002', 'unit': '条', 'price': 980.00, 'discount': ['第3件半价', '满3送1']},
           {'name': '中国经典钱币套装', 'id': '002002', 'unit': '套', 'price': 998.00,
            'discount': ['每满2000减30', '每满1000减10', '95折']},
           {'name': '守扩之羽比翼双飞4.8g', 'id': '002001', 'unit': '条', 'price': 998.00,
            'discount': ['每满2000减30', '每满1000减10', '95折']},
           {'name': '中国银象棋12g', 'id': '002003', 'unit': '套', 'price': 698.00,
            'discount': ['每满3000元减350', '每满2000减30', '每满1000减10', '95折']}

           ]

customer = [
    {'name': '马丁', 'level': '普卡', 'card_id': '6236609999', 'points': 9860},
    {'name': '王立', 'level': '金卡', 'card_id': '6630009999', 'points': 48860},
    {'name': '李想', 'level': '白金卡', 'card_id': '8230009999', 'points': 98860},
    {'name': '张三', 'level': '钻石卡', 'card_id': '9230009999', 'points': 198860}
]


class Pay(object):

    def read_json(self, filename):
        with open(filename, 'r') as load_f:
            load_dict = json.load(load_f)
            return load_dict

    def total_amount(self):
        order = self.read_json('../files/sample_command.json')
        product_list = order['items']
        print product_list
        total = 0
        for p in product_list:
            if p['product'] == '001001':
                total += p['amount'] * 998
            if p['product'] == '001002':
                total += p['amount'] * 1380
            if p['product'] == '003001':
                total += p['amount'] * 1580
            if p['product'] == '003002':
                total += p['amount'] * 980
            if p['product'] == '002002':
                total += p['amount'] * 998
            if p['product'] == '002001':
                total += p['amount'] * 1080
            if p['product'] == '002003':
                total += p['amount'] * 698
        return total

    def pay_amount(self, load_dict):
        pass

    def discount_amount(self, product_id, amount):
        discount = 0
        if product_id == '001002':
            discount = 1380 * amount * 0.1

        if product_id == '003001':
            discount = 1580 * amount * 0.05

        if product_id == '002001':
            discount = 1080 * amount * 0.05

        if product_id == '002003':
            discount = 698 * amount * 0.1
        return discount

    def full_reduction(self, product_id, amount):
        reduction = 0
        if product_id == '003002':
            if amount == 3:
                reduction = 980 * 0.5
            elif amount > 3:
                reduction = 980
        if product_id == '002002':
            temp = amount * 998
            if 1000 <= temp < 2000:
                reduction = 10

            elif temp >= 2000:
                reduction = 30

        if product_id == '002001':
            if amount == 3:
                reduction = 1080 * 0.5
            elif amount > 3:
                reduction = 1080
        if product_id == '002003':
            temp = amount * 698
            if 1000 <= temp < 2000:
                reduction = 10

            elif 2000 <= temp < 3000:
                reduction = 30
            elif temp >= 3000:
                reduction = 350
        return reduction

    def max_discount(self, product_id, amount):
        discount = 0
        reduction = 0
        if product_id in ('002001', '002003'):
            discount = self.discount_amount(product_id, amount)
            reduction = self.full_reduction(product_id, amount)
        print 'discount is:%s,reduction is:%s' % (discount, reduction)
        return max(discount, reduction)


# print Pay().full_reduction('002003', 10)
print Pay().max_discount('002003', 5)
