import pytest
from selenium import webdriver
from pageObjects.LoginPage import Loginpage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePagetitle(self,setup):
        self.logger.info("**************Test_001_Login*************")
        self.logger.info("*************Verifying Home Page**************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title =="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*************Home Page title is passed**************")

        else:
            self.driver.get_screenshot_as_file(".\\screenshots\\" + "test_homePagetitle.png")
            self.driver.close()
            self.logger.error("*************Home Page title is Failed**************")
            assert False

    def test_login(self,setup):
        self.logger.info("*************Verifying the login test**************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassWord(self.password)
        self.lp.clickLogin()
        act_title =self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*************Login test is passed**************")
            self.driver.close()

        else:
            self.driver.get_screenshot_as_file(".\\screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("*************Login test is Failed**************")
            assert False