from common.common_fun import Common
from selenium.webdriver.common.by import By
from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
import logging


class LoginView(Common):
    # 登陆界面元素
    username_type = (By.XPATH, '//*[@class="android.widget.EditText" and @text="请输入用户名"]')
    password_type = (By.ID, 'com.tal.kaoyan:id/login_password_edittext')
    loginBtn_type = (By.ID, 'com.tal.kaoyan:id/login_login_btn')
    username_clear = (By.ID, 'com.tal.kaoyan:id/login_email_edittext')
    # 个人中心下线警告提醒确定按钮
    commitBtn = (By.ID, 'com.tal.kaoyan:id/tip_commit')
    button_mysefl = (By.ID, 'com.tal.kaoyan:id/mainactivity_button_mysefl')

    # 个人中心元素
    username = (By.ID, 'com.tal.kaoyan:id/activity_usercenter_username')
    # 退出登陆元素
    settingBtn = (By.ID, 'com.tal.kaoyan:id/myapptitle_RightButton_textview')
    logoutBtn = (By.ID, 'com.tal.kaoyan:id/setting_logout_text')
    commit = (By.ID, 'com.tal.kaoyan:id/tip_commit')

    def login_action(self, username, password):
        self.check_updateBtn()
        self.check_skipBtn()

        logging.info('======================login start======================')

        logging.info("username_clear")
        self.driver.find_element(*self.username_clear).clear()
        logging.info("username_clear finished!")

        logging.info("login_username")
        logging.info('input username:%s' % username)
        self.driver.find_element(*self.username_type).send_keys(username)
        logging.info("login_username finished!")

        logging.info("login_password")
        logging.info('input password:%s' % password)
        self.driver.find_element(*self.password_type).send_keys(password)
        logging.info("login_password finished!")

        logging.info("click loginBtn")
        self.driver.find_element(*self.loginBtn_type).click()
        logging.info('click loginBtn finished!')

        logging.info('======================login finished!======================')

    def check_account_alert(self):
        '''检测账户登录后是否有账户下线提示'''
        logging.info('====check_account_alert======')
        try:
            element = self.driver.find_element(*self.commitBtn)
        except NoSuchElementException:
            pass
        else:
            logging.info('click commitBtn')
            element.click()

    def logout_action(self):
        logging.info('进行退出登陆操作')
        self.find_element(*self.settingBtn).click()
        self.find_element(*self.logoutBtn).click()
        self.find_element(*self.commit).click()
        logging.info('退出登录成功')

    def check_loginStatus(self):
        self.check_market_ad()
        self.check_account_alert()
        logging.info('获取当前APP登陆状态')
        try:
            self.driver.find_element(*self.button_mysefl).click()
            self.driver.find_element(*self.username)
        except NoSuchElementException:
            logging.error('登陆失败！！！')
            self.getScreenShot('check_loginStatus')
            return False
        else:
            logging.info('登陆成功，login_out')
            self.logout_action()
            logging.info('退出登陆成功')
            return True


if __name__ == '__main__':
    driver = appium_desired()
    l = LoginView(driver)
    l.login_action('yuanchaoer', 'qq123456')
    l.check_loginStatus()
