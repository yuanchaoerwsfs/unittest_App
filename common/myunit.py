import unittest
from time import sleep
import logging
from common.desired_caps import appium_desired


class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info('======setUp======')
        self.driver = appium_desired()

    def tearDown(self):
        logging.info('=======tearDown=======')
        sleep(5)
        self.driver.close_app()
