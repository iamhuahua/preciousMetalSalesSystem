# -*-coding:utf-8 -*-

from pay import customer


class Upgrade(object):
    def upgrade(self, c_id, pay):
        c_info = []
        for c in customer:
            if c['card_id'] == id:
                if c['level'] == '普卡':
                    c_info['points'] = c.points + int(pay)
                elif c['level'] == '金卡':
                    c_info['points'] += int(pay) * 1.5
                elif c['level'] == '白金卡':
                    c_info['points'] += int(pay) * 1.8
                elif c['level'] == '钻石卡':
                    c_info['points'] += int(pay) * 2

            if int(c_info['points']) < 10000:
                c_info['level'] = '普卡'
            elif 10000 <= int(c_info['points']) < 50000:
                c_info['level'] = '金卡'
            elif 50000 <= int(c_info['points']) < 100000:
                c_info['level'] = '白金卡'
            elif int(c_info['points']) >= 100000:
                c_info['level'] = '钻石卡'
            c_info['name'] = c['name']
            c_info['card_id'] = c['card_id']

        return c_info


print Upgrade().upgrade('6236609999', 1000)
