from common.common_fun import Common
from selenium.webdriver.common.by import By
from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
import random,logging
from time import sleep


class RegisterView(Common):
    # 登录界面注册按钮
    register_text = (By.ID, 'com.tal.kaoyan:id/login_register_text')

    #我的信息
    button_mysefl = (By.ID, 'com.tal.kaoyan:id/mainactivity_button_mysefl')
    username = (By.ID, 'com.tal.kaoyan:id/activity_usercenter_username')


    # 头像设置相关元素
    userheader = (By.ID, 'com.tal.kaoyan:id/activity_register_userheader')
    item_image = (By.ID, 'com.tal.kaoyan:id/item_image')
    saveBtn = (By.ID, 'com.tal.kaoyan:id/save')

    # 输入注册账号、密码、邮箱信息
    register_username = (By.ID, 'com.tal.kaoyan:id/activity_register_username_edittext')
    register_password = (By.ID, 'com.tal.kaoyan:id/activity_register_password_edittext')
    register_email = (By.ID, 'com.tal.kaoyan:id/activity_register_email_edittext')
    register_btn = (By.ID, 'com.tal.kaoyan:id/activity_register_register_btn')

    # 进入考研帮按钮
    perfectinfomation_goBtn = (By.ID, 'com.tal.kaoyan:id/activity_perfectinfomation_goBtn')

    # 考试年份
    perfectinfomation_time = (By.ID, 'com.tal.kaoyan:id/activity_perfectinfomation_time')
    perfectinfomation_time_1 = (By.CLASS_NAME, 'android.widget.TextView')

    # 注册院校选择
    perfectinfomation_school = (By.ID, 'com.tal.kaoyan:id/perfectinfomation_edit_school_name')
    forum_title = (By.ID, 'com.tal.kaoyan:id/more_forum_title')
    university_search_item_name = (By.ID, 'com.tal.kaoyan:id/university_search_item_name')
    # 专业选择
    perfectinfomation_major = (By.ID, 'com.tal.kaoyan:id/activity_perfectinfomation_major')
    subject_title = (By.ID, 'com.tal.kaoyan:id/major_subject_title')
    group_title = (By.ID, 'com.tal.kaoyan:id/major_group_title')
    major_search_item_name = (By.ID, 'com.tal.kaoyan:id/major_search_item_name')

    def register_action(self, register_username, register_password, register_email):
        self.check_updateBtn()
        self.check_skipBtn()

        logging.info('点击注册按钮')
        self.driver.find_element(*self.register_text).click()

        logging.info('=========register_action===========')
        self.driver.find_element(*self.userheader).click()
        sleep(0.5)
        self.driver.find_elements(*self.item_image)[10].click()
        self.driver.find_element(*self.saveBtn).click()

        # 用户名密码填写
        logging.info('register username is %s' % register_username)
        self.driver.find_element(*self.register_username).click()
        self.driver.find_element(*self.register_username).send_keys(register_username)

        logging.info('register_password is %s' % register_password)
        self.driver.find_element(*self.register_password).click()
        self.driver.find_element(*self.register_password).send_keys(register_password)

        logging.info('register_email is %s' % register_email)
        self.driver.find_element(*self.register_email).click()
        self.driver.find_element(*self.register_email).send_keys(register_email)

        logging.info('click register button')
        self.driver.find_element(*self.register_btn).click()

        try:
            self.driver.find_element(*self.perfectinfomation_school)
        except NoSuchElementException:
            logging.error('register Fail!')
            self.getScreenShot('register Fail')
            return False
        else:
            logging.info('进入信息完善选择界面')
            self.add_register_info()
            # 注册结果判断
            if self.check_register_status():
                return True
            else:
                return False

    def add_register_info(self):
        logging.info('===========add_register_info===========')
        # 考试年份选择
        logging.info('考试年份选择')
        self.find_element(*self.perfectinfomation_time).click()
        sleep(0.5)
        self.find_elements(*self.perfectinfomation_time_1)[5].click()

        # 注册院校一选择  天津-外国语大学
        logging.info('注册院校一选择  天津-外国语大学')
        self.find_elements(*self.perfectinfomation_school)[0].click()
        self.find_elements(*self.forum_title)[2].click()
        self.find_elements(*self.university_search_item_name)[5].click()

        # 注册院校二选择   重庆-重庆理工
        logging.info('注册院校二选择   重庆-重庆理工')
        self.find_elements(*self.perfectinfomation_school)[1].click()
        self.find_elements(*self.forum_title)[7].click()
        self.find_elements(*self.university_search_item_name)[2].click()

        # 注册院校三选择  山东-中国石油大学
        logging.info('注册院校三选择  山东-中国石油大学')
        self.find_elements(*self.perfectinfomation_school)[2].click()
        self.find_elements(*self.forum_title)[8].click()
        self.find_elements(*self.university_search_item_name)[1].click()
        # 专业选择
        logging.info('专业选择')
        self.find_element(*self.perfectinfomation_major).click()
        self.find_elements(*self.subject_title)[9].click()
        self.find_elements(*self.group_title)[2].click()
        self.find_elements(*self.major_search_item_name)[0].click()
        # 点击进入考研帮按钮
        logging.info('点击进入考研帮按钮')
        self.find_element(*self.perfectinfomation_goBtn).click()

    def check_register_status(self):
        self.check_market_ad()
        logging.info('==========check_registerStatus===========')

        try:
            self.driver.find_element(*self.button_mysefl).click()
            self.driver.find_element(*self.username)
        except NoSuchElementException:
            logging.error('register Fail!')
            self.getScreenShot('register_Fail')
            return False
        else:
            logging.info('register success!')
            self.getScreenShot('register_success')
            return True


if __name__ == '__main__':
    driver=appium_desired()
    register=RegisterView(driver)

    username='yuan'+'FLY'+str(random.randint(1000,9000))
    password='qqqq'+str(random.randint(1000,9000))
    email='yuan'+str(random.randint(1000,9000))+'@163.com'

    register.register_action(username,password,email)