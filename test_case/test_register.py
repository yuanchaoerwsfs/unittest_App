from common.myunit import StartEnd
from businessView.registerView import RegisterView
import logging
import random
import unittest


class RegisterTest(StartEnd):
    """注册案例执行"""

    def test_user_register(self):
        logging.info('======test_user_regeister======')
        r = RegisterView(self.driver)
        username = 'yuan' + 'FLY' + str(random.randint(1000, 9000))
        password = 'qqqq' + str(random.randint(1000, 9000))
        email = 'yuan' + str(random.randint(1000, 9000)) + '@163.com'
        self.assertTrue(r.register_action(username, password, email))


if __name__ == '__main__':
    for i in range(5):
        unittest.main()