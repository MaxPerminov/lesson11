from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
import time


class Test:

    def __init__(self):
        pass

    @staticmethod
    def driver_installer(url):
        try:
            ua = UserAgent()
            op = webdriver.ChromeOptions()
            op.add_argument(f"user_agent={ua}")
            op.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                            + "AppleWebKit/537.36 (KHTML, like Gecko)")

            driver = webdriver.Chrome(options=op, service=ChromeService(ChromeDriverManager().install()))
            # driver.add_cookie({"name": "John", "surname": "Doe", "age": 23})
            driver.get(url)
            time.sleep(20)
        # except Exception as ex:
        #     print(ex)
        finally:
            driver.close()
            driver.quit()


user_agent = [
    "hello world",
    "something else"
]


Test.driver_installer("https://www.whatismybrowser.com/")
