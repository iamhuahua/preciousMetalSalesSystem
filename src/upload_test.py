# -*-coding:utf-8 -*-

import unittest
from upgrade import Upgrade


class UploadTest(unittest.TestCase):
    """
    测试客户积分累积功能，等级升级功能
    """
    def setUp(self):
        self.upload = Upgrade()

    def tearDown(self):
        print "测试结束"

    def test_upload(self):
        print self.upload.upgrade('6236609999', 1000)


if __name__ == '__main__':
    unittest.main(verbosity=2)
