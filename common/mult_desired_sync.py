import logging.config
import yaml
from appium import webdriver
import os, csv, codecs
import multiprocessing
from time import ctime

CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()

with open('../config/kyb_caps.yaml', 'r', encoding='utf-8') as file:
    data = yaml.load(file, Loader=yaml.SafeLoader)

    devices_list = ['127.0.0.1:62001','127.0.0.1:62025']


def appium_desired(udid, port):
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
    desired_caps['udid'] = udid
    desired_caps['noReset'] = data['noReset']

    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']

    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    logging.info('start APP .....')
    print('appium port:%s start run %s at %s' % (port, udid, ctime()))
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(port) + '/wd/hub', desired_caps)

    driver.implicitly_wait(10)
    return driver


# 构建进程组
desired_process = []

# 加载desired进程
for i in range(len(devices_list)):
    port = 4723+2*i
    logging.info('异步添加之前port值：'+str(port))
    logging.info('异步添加之前i值：'+str(i))
    logging.info('异步添加之前设备IP值：'+str(devices_list[i]))
    desired = multiprocessing.Process(target=appium_desired, args=(devices_list[i], port))

    desired_process.append(desired)

if __name__ == '__main__':
    for desired in desired_process:
        desired.start()
    for desired in desired_process:
        desired.join()
