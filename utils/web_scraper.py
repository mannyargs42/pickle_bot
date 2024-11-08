from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
# from webdriver_manager.chrome import ChromeDriverManager

"""
Step 2 of the project guide: Implement Web Scraping-
Use Selenium to automate browser interactions-
Navigate to target website.

Use OOP for modular code, encapsulation, reusability and readability:
* __init__: Instantiate Selenium ChromeDriver and open web browser.
* navigator: Navigate to the web page for scheduling tennis/pickleball.
* login: Locate the "Log In & Continue" element of the webpage and click.
    Enter email and password.
    Click the log in button.
* choose_date: Locate the calendar and click.
    Locate date (two days from today) and click.
* choose_time: Locate desired time option and click.
    Open participant list.
    Choose participant.
    Find "BOOK" button and click.
    Find "SEND CODE" button and click.


"""

class WebScraper:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def navigator(self, url):
        self.driver.get(url)

    def login(self, email, password):
        initial_login = self.driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/div/div/div[3]/button[1]/div')
        initial_login.click()
        enter_email = self.driver.find_element(By.XPATH, '//*[@id="email"]')
        enter_password = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="radix-:ri:"]/div[2]/div[2]/button')
        enter_email.send_keys(email)
        enter_password.send_keys(password)
        login_button.click()

    def choose_date(self, two_days_date):
        calendar_popup = self.driver.find_element(By.XPATH, '//*[@id="panel:r2:0"]/div[1]/div/div')
        calendar_popup.click()
        choose_date = self.driver.find_element(By.CSS_SELECTOR, f'[aria-label="Choose {two_days_date}"]')
        choose_date.click()

    def choose_time(self, optimal_time, participant):
        choose_time = self.driver.find_element(By.XPATH, f'//div[@class="swiper-slide"]//p[text()="{optimal_time}"]')
        choose_time.click()
        open_participant = self.driver.find_element(By.XPATH, f'//div[@class="flex flex-col text-left"]//p[text()="Select participant"]')
        open_participant.click()
        choose_participant = self.driver.find_element(By.ID, f'headlessui-listbox-option-:r6u:')
        choose_participant.click()
        book_button = self.driver.find_element(By.XPATH, '//button[contains(@class, "uppercase text-sm font-bold border-2")]')
        book_button.click()
        send_code = self.driver.find_element(By.XPATH, '//button[contains(@class, "uppercase text-sm font-bold border-2")]')
        send_code.click()

url = "url.com"
email = ""
rec_password = ""
two_days_date = "Day, Month Xth, Year"
optimal_time = "0:00 XX"
participant = ""

scraper = WebScraper()
scraper.navigator(url)
scraper.login(email, rec_password)
scraper.choose_date(two_days_date)
scraper.choose_time(optimal_time, participant)


print("so far so good")

time.sleep(120)
#<div class="text-sm font-medium text-neutral-900">Log In</div>
#//*[@id="__next"]/main/div[2]/div/div/div[3]/button[1]/div