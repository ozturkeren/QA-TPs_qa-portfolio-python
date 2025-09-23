from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class SwagLoginPage:
    def __init__(self, headless: bool = True):
        opts = Options()
        if headless:
            opts.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options=opts)  # Selenium Manager auto-installs ChromeDriver
        self.driver.set_window_size(1280, 800)
        self.url = "https://www.saucedemo.com/"

    def open(self):
        self.driver.get(self.url)

    def login(self, user: str, pwd: str):
        self.driver.find_element(By.ID, "user-name").send_keys(user)
        self.driver.find_element(By.ID, "password").send_keys(pwd)
        self.driver.find_element(By.ID, "login-button").click()

    def landing_title(self) -> str:
        return self.driver.title

    def close(self):
        self.driver.quit()
