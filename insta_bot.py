from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException 
from time import sleep
from secrets import username, password

class InstaBot():
    def __init__(self):
        self.driver = webdriver.Chrome((r"C:\chromedriver_win32\chromedriver"))

    def check_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def login_with_fb(self):
        self.driver.get('https://instagram.com')

        sleep(10)

        ## instagram home page
        fb_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[6]/button')
        fb_btn.click()

        #### fb login
        email_input = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_input.clear()
        email_input.send_keys(username)

        password_input = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password_input.clear()
        password_input.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        login_btn.click()

        sleep(5)

        """ vkey = input('enter vkey : ')

        vkey_input = self.driver.find_element_by_xpath('//*[@id="approvals_code"]')
        vkey_input.send_keys(vkey)
        if (self.check_exists_by_xpath('//*[@id="checkpointSubmitButton"]')):
            continue_btn = self.driver.find_element_by_xpath('//*[@id="checkpointSubmitButton"]')
            continue_btn.click()

        sleep(5)

        checkpoint_radio = self.driver.find_element_by_xpath('//*[@id="u_0_3"]')
        checkpoint_radio.click()

        checkpoint_btn = self.driver.find_element_by_xpath('//*[@id="checkpointSubmitButton"]')
        checkpoint_btn.click()

        sleep(5) """

        ## go back to instagram again

        self.driver.get('https://instagram.com')

        sleep(5)

        login = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/div[2]/button')
        login.click()

        sleep(5)

        ##notification ass pain
        while(self.check_exists_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')):
            noti_btn = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
            noti_btn.click()

        sleep(5)







    def login_with_cred(self):
        self.driver.get('https://instagram.com')

        sleep(10)

        #### login
        email_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
        email_input.clear()
        email_input.send_keys(username)

        password_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
        password_input.clear()
        password_input.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button')
        login_btn.click()

        sleep(5)

        ##notification ass pain
        while(self.check_exists_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')):
            noti_btn = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
            noti_btn.click()

        sleep(5)







    def search_for_hashtag(self):

        search = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys('#like4like')

        sleep(5)

        search_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]')
        search_btn.click()

    def like(self):

        photo = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]')
        photo.click()

        sleep(5)

        like_btn = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
        like_btn.click()

        sleep (9)
        for i in range(50):
            """ next_btn = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a')
            next_btn.click() """
            self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a').send_keys('\ue014')

            sleep(2)

            like_btn = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
            like_btn.click()

            sleep(3)


# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID,"CloseLink"))).click()
bot = InstaBot()
bot.login_with_cred()





