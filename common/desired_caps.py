import logging.config
import yaml
from appium import webdriver
import os, csv, codecs
import multiprocessing, logging

CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


def appium_desired():
    with open('../config/kyb_caps.yaml', 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.SafeLoader)

    desired_caps = {}
    desired_caps['platformName'] = data['platformName']

    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']

    base_dir = os.path.dirname(os.path.dirname(__file__))
    app_path = os.path.join(base_dir, 'app', data['appname'])
    desired_caps['app'] = app_path
    # os.path.dirname(__file__) 表示获取当前路径
    # os.path.dirname(A)   表示在A路径的基础上返回上一级，可多次返回上级
    # os.path.join(base_dir,'app',data['appname'])  join表示连接函数，base_dir路径里连接上app文件夹在连接上data[appname]名字的文件
    desired_caps['noReset'] = data['noReset']

    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']

    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    logging.info('start APP .....')
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' +str(data['port']) + '/wd/hub', desired_caps)

    driver.implicitly_wait(10)
    return driver


if __name__ == '__main__':
    appium_desired()
