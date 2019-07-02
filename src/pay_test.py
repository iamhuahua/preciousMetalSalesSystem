# -*-coding:utf-8 -*-

import unittest
from pay import Pay


class PayTest(unittest.TestCase):
    """
    测试计算支付金额核心功能
    """

    def setUp(self):
        self.p = Pay()

    def tearDown(self):
        print "测试结束"

    # 测试读取json文件功能
    def test_read_json(self):
        print self.p.read_json('../filses/sample_command.json')

    # 测试计算订单总金额功能
    def test_total_amount(self):
        print self.p.read_json()

    # 测试计算订单实际支付金额功能
    def test_pay_amount(self):
        print self.p.pay_amount()

    def test_discount_amount(self):
        discount_amount = self.p.discount_amount('001002', 5, ['9折'])
        self.assertEqual(discount_amount, 690)

    def test_full_reduction(self):
        reduction_amount = self.p.full_reduction('002003', 10)
        self.assertEqual(reduction_amount, 350)

    def test_max_discount(self):
        max_discount = self.p.max_discount('001002', 5, ['9折'])
        self.assertEqual(max_discount, 690)

    def test_customer_info(self):
        print self.p.customer_info('6236609999')


if __name__ == '__main__':
    unittest.main(verbosity=2)
