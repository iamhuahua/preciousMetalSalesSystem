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
    """
    支付核心功能：订单总额，实际支付金额，优惠金额
    """


# 读取json文件功能
def read_json(self, filename):
    with open(filename, 'r') as load_f:
        load_dict = json.load(load_f)
        return load_dict


# 计算订单总金额功能，并返回商品信息
def total_amount(self):
    order = self.read_json('../files/sample_command.json')
    product_list = order['items']
    product_detail = []
    print product_list
    total = 0
    for p in product_list:
        # print p
        a = {}
        if p['product'] == '001001':
            total += p['amount'] * 998

            a['id'] = '001001'
            a['name'] = '世园会五十国钱币册'
            a['amount'] = p['amount']
            a['price'] = 998
            a['total_amount'] = p['amount'] * 998
            product_detail.append(a)
        if p['product'] == '001002':
            total += p['amount'] * 1380
            a['id'] = '001002'
            a['name'] = '2019北京世园会纪念银章大全40g'
            a['amount'] = p['amount']
            a['price'] = 1380
            a['total_amount'] = p['amount'] * 1380
            product_detail.append(a)
        if p['product'] == '003001':
            total += p['amount'] * 1580
            a['id'] = '003001'
            a['name'] = '招财进宝'
            a['amount'] = p['amount']
            a['price'] = 1580
            a['total_amount'] = p['amount'] * 1580
            product_detail.append(a)
        if p['product'] == '003002':
            total += p['amount'] * 980
            a['id'] = '003002'
            a['name'] = '水晶之恋'
            a['amount'] = p['amount']
            a['price'] = 980
            a['total_amount'] = p['amount'] * 980
            product_detail.append(a)
        if p['product'] == '002002':
            total += p['amount'] * 998
            a['id'] = '002002'
            a['name'] = '中国经典钱币套装'
            a['amount'] = p['amount']
            a['price'] = 998
            a['total_amount'] = p['amount'] * 998
            product_detail.append(a)
        if p['product'] == '002001':
            total += p['amount'] * 1080
            a['id'] = '002001'
            a['name'] = '守扩之羽比翼双飞4.8g'
            a['amount'] = p['amount']
            a['price'] = 1080
            a['total_amount'] = p['amount'] * 1080
            product_detail.append(a)
        if p['product'] == '002003':
            total += p['amount'] * 698
            a['id'] = '002003'
            a['name'] = '中国银象棋12g'
            a['amount'] = p['amount']
            a['price'] = 698
            a['total_amount'] = p['amount'] * 698
            product_detail.append(a)
    # print product_detail
    data = {
        'product_detail': product_detail,
        'total': total,
        'order_id': order['orderId'],
        'memberId': order['memberId'],
        'create_time': order['createTime'],

    }
    return data


# 计算订单实际支付金额功能，并返回商品信息
def pay_amount(self):
    order = self.read_json('../files/sample_command.json')
    product_list = order['items']
    discount_cards = order['discountCards']
    print type(discount_cards)
    print discount_cards
    discount_product_detail = []
    discount = 0
    for p in product_list:
        a = {}
        max_discount_amount = self.max_discount(p['product'], p['amount'], discount_cards)
        print max_discount_amount
        if p['product'] == '001001':
            discount += max_discount_amount

            a['id'] = '001001'
            a['name'] = '世园会五十国钱币册'
            a['amount'] = p['amount']
            a['price'] = 998
            a['total_amount'] = max_discount_amount
            if max_discount_amount:
                discount_product_detail.append(a)
        if p['product'] == '001002':
            discount += max_discount_amount
            a['id'] = '001002'
            a['name'] = '2019北京世园会纪念银章大全40g'
            a['amount'] = p['amount']
            a['price'] = 1380
            a['total_amount'] = max_discount_amount
            if max_discount_amount:
                discount_product_detail.append(a)
        if p['product'] == '003001':
            discount += max_discount_amount
            a['id'] = '003001'
            a['name'] = '招财进宝'
            a['amount'] = p['amount']
            a['price'] = 1580
            a['total_amount'] = max_discount_amount
            discount_product_detail.append(a)
        if p['product'] == '003002':
            discount += max_discount_amount
            a['id'] = '003002'
            a['name'] = '水晶之恋'
            a['amount'] = p['amount']
            a['price'] = 980
            a['total_amount'] = max_discount_amount
            discount_product_detail.append(a)
        if p['product'] == '002002':
            discount += max_discount_amount
            a['id'] = '002002'
            a['name'] = '中国经典钱币套装'
            a['amount'] = p['amount']
            a['price'] = 998
            a['total_amount'] = max_discount_amount
            discount_product_detail.append(a)
        if p['product'] == '002001':
            discount += max_discount_amount
            a['id'] = '002001'
            a['name'] = '守扩之羽比翼双飞4.8g'
            a['amount'] = p['amount']
            a['price'] = 1080
            a['total_amount'] = max_discount_amount
            discount_product_detail.append(a)
        if p['product'] == '002003':
            discount += max_discount_amount
            a['id'] = '002003'
            a['name'] = '中国银象棋12g'
            a['amount'] = p['amount']
            a['price'] = 698
            a['total_amount'] = max_discount_amount
            discount_product_detail.append(a)
    data = {
        'discount_product_detail': discount_product_detail,
        'discount': discount,
        'real_pay_amount': self.total_amount()['total'] - discount
    }

    return data


# 根据客户拥有的打折券，计算支持打折的商品打折金额
def discount_amount(self, product_id, amount, discount_cards):
    discount = 0
    if discount_cards:
        for card in discount_cards:
            # card = json.dumps(card)
            # print card
            # print type(card)
            # print type('9折券')
            if card in '9折券':
                if product_id == '001002':
                    discount = 1380 * amount * 0.1
                if product_id == '002003':
                    discount = 698 * amount * 0.1
            elif card in '95折券':

                if product_id == '003001':
                    discount = 1580 * amount * 0.05

                if product_id == '002001':
                    discount = 1080 * amount * 0.05

    return discount


# 根据商品id计算商品满减优惠的金额
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


# 根据商品id和 数量，以及客户拥有的打折券，计算出最大优惠金额
def max_discount(self, product_id, amount, discount_cards=[]):
    discount = 0
    reduction = 0
    # if product_id in ('002001', '002003'):
    if discount_cards:
        discount = self.discount_amount(product_id, amount, discount_cards)
    reduction = self.full_reduction(product_id, amount)
    # print 'discount is:%s,reduction is:%s' % (discount, reduction)
    return max(discount, reduction)


# 根据客户id返回客户详细信息：姓名，等级，积分，卡号
def customer_info(self, id):
    c_info = {}
    for c in customer:
        if c['card_id'] == id:
            c_info['name'] = c['name']
            c_info['level'] = c['level']
            c_info['points'] = c['points']
    return c_info

# print Pay().full_reduction('002003', 10)
# print Pay().max_discount('002003', 5)
# Pay().total_amount()
# print Pay().max_discount('001002', 5, ['9折'])
# print Pay().pay_amount()
# print Pay().discount_amount('001002', 5, ['9折'])
# print Pay().customer_info('6236609999')
