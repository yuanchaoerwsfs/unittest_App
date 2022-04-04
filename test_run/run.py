import sys

path = 'D:\\Sun\\Sun_SONY\\kyb_unittest_Project\\'
sys.path.append(path)

import unittest
from BSTestRunner import BSTestRunner
import os, time, logging

# 测试报告和测试案例路径
test_dir = '../test_case'
report_dir = '../reports'

# 加载测试用例
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_register.py')

# 定义测试报告格式
now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = report_dir + '/' + now + 'test_report.html'

# 生成测试报告
with open(report_name, 'wb')as f:
    runner = BSTestRunner(stream=f, title='Kyb Test Report', description='Kyb Android app Test Report')
    logging.info('start run testcare....')
    runner.run(discover)
