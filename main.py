from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pyautogui
import keyboard

class TypingBot:

    def __init__(self):
        self.webdriver_service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.webdriver_service)
        self.driver.get('https://monkeytype.com')
        self.driver.implicitly_wait(10)
        time.sleep(5)

    def get_current_word(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.word.active')

    def type_slow(self):
        # just messing around with pyautogui
        while True:
            try:
                current_word = self.get_current_word().text
                # interval is the time between each word. the lower the faster.
                pyautogui.write(current_word + ' ', interval=0.000)
            except:
                print("parole finite")
                break

    def type_fast(self):
        # yolo this function types so fast, MonkeyType can't keep up and just gives us an "infinite" score.
        while True:
            try:
                current_word = self.get_current_word().text
                keyboard.write(current_word + ' ')
            except:
                print("parole finite")
                break

    def type_letter_by_letter(self):
        while True:
            try:
                current_word = self.get_current_word().text
                for letter in list(current_word):
                    keyboard.write(letter)
                    # this is the time between each letter. the lower the faster.
                    # a higher value will be more human like.
                    time.sleep(0.04)
                keyboard.press_and_release('space')
            except:
                print("parole finite")
                break

if __name__ == "__main__":
    bot = TypingBot()
    # comment out the ones you don't want to use
    # bot.type_slow()
    # bot.type_fast()
    bot.type_letter_by_letter()