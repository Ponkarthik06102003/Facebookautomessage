from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import Chr

driver = webdriver.Chrome(ChromeDriverManager().install())

# enter receiver user name
user = ['naveenkumar_the_magician', 'sanmugavadivel_23',
        's_u_d_h_a_r_s_u_n', 'thiwin_diamond', 'the_tuneoholic_victim__']
message_ = ("testing ...")


class bot:
    def __init__(self):(self, username, password, user, message):

        self.username = username
        self.password = password
        self.user = user
        self.message = message
        self.base_url = 'https://www.instagram.com/'
        self.bot = driver
        self.login()

    def close_browser(self):
        self.browser.close()
        self.browser.quit()

    def login(self):
        self.bot.get(self.base_url)

        enter_username = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'username')))
        enter_username.send_keys(self.username)
        enter_password = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)
        enter_password.send_keys(Keys.RETURN)
        time.sleep(5)

        # first pop-up
        self.bot.find_element(By.XPATH,
                              '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div').click()
        time.sleep(2)

        # 2nd pop-up
        self.bot.find_element(By.XPATH,
                              '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()

        # direct button
        self.bot.find_element(By.XPATH,
                              '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/a').click()
        time.sleep(3)

        # clicks on pencil icon
        self.bot.find_element(By.XPATH,
                              '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[1]/div/div[3]/button').click()
        time.sleep(2)
        for i in user:

            # enter the username
            self.bot.find_element(By.XPATH,
                                  '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input').send_keys(i)
            time.sleep(3)

            # click on the username
            self.bot.find_element(By.XPATH,
                                  '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/div/div[2]/div/div/span[1]/span').click()
            time.sleep(4)

            # next button
            self.bot.find_element(By.XPATH,
                                  '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/button').click()
            time.sleep(4)

            # click on message area
            send = self.bot.find_element(By.XPATH,
                                         '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')

            # types message
            send.send_keys(self.message)
            time.sleep(1)

            # send message
            send.send_keys(Keys.RETURN)
            time.sleep(2)

            # clicks on direct option or pencil icon
            self.bot.find_element(By.XPATH,
                                  '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[1]/div/div[3]/button').click()
            time.sleep(4)


def init():
    # U need to replace ur username and password here
    # login = open(r'C:\Users\Pon Karthik\PycharmProjects\pythonProject\auto dm.txt')
    # line = login.readlines()
    username ="sooniyakarannaveen@gmail.com"
    password ="Naveen@123"

    bot(username, password, user, message_)

    # when our program ends it will show "done".
    input("DONE")
    bot.close_browser()


# calling the function
init()









