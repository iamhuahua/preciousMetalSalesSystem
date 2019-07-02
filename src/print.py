# -*-coding:utf-8 -*-
import json
from pay import Pay


class Print(object):

    def write_txt(self):
        p = Pay()
        total_product_list = p.total_amount()
        discount_product_list = p.pay_amount()
        c_info = p.customer_info(total_product_list['memberId'])
        # print c_info
        order_id = json.dumps(total_product_list['order_id'])
        create_time = json.dumps(total_product_list['create_time'])
        member_id = json.dumps(total_product_list['memberId'])
        points = json.dumps(c_info['points'])

        with open("../files/result.txt", 'w') as wf:
            new_context = "方鼎银行贵金属购买凭证\r\n\r\n销售单号：" + order_id + " 日期：" + create_time + "\r\n" + \
                          "客户卡号：" + member_id + " 会员姓名：" + c_info['name'] + " 客户等级：" + c_info[
                              'level'] + " 累计积分：" + points
            new_context += "\r\n\r\n商品及数量           单价         金额\r\n"
            for total_product in total_product_list['product_detail']:
                id = json.dumps(total_product['id'])
                amount = json.dumps(total_product['amount'])
                price = json.dumps(total_product['price'])
                total_amount = json.dumps(total_product['total_amount'])
                new_context += "(" + id + ")" + total_product['name'] + "*" + amount + "," + price + "," + \
                               total_amount + "\r\n"

            new_context += "合计：" + json.dumps(total_product_list['total']) + "\r\n\r\n优惠清单：\r\n"
            for discount_product in discount_product_list:
                id = json.dumps(discount_product['id'])
                total_amount = json.dumps(discount_product['total_amount'])
                new_context += "(" + discount_product['id'] + ")" + discount_product['name'] + "：-" + total_amount + \
                               total_amount + "\r\n"

            wf.write(new_context)


Print().write_txt()
