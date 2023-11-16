# import pyautogui as pg
# import random
#
# pg.FAILSAFE = True
# pg.PAUSE = 2
#
# key_words = ["hello world", "cats", "planes"]
#
# icon_location = pg.locateCenterOnScreen('icons/chrome.png', confidence=0.9)
# pg.click(icon_location.x, icon_location.y, duration=0.5)
#
# random_word = random.choice(key_words)
#
# pg.hotkey('ctrl', 'shift', 'n')
# pg.typewrite(random_word, interval=0.1)
# pg.hotkey('enter')
# pg.hotkey('ctrl', 'f')
# pg.typewrite('https', interval=0.1)
# pg.hotkey('ctrl', 'enter')
# pg.moveTo(0.5 * pg.size()[0], 0.5 * pg.size()[1])
# pg.scroll(-500)
#
# back_location = pg.locateCenterOnScreen('icons/back.png', confidence=0.9)
# pg.click(back_location.x, back_location.y, duration=0.5)
# pg.hotkey('ctrl', 'f')
# pg.hotkey('enter')
# pg.hotkey('ctrl', 'enter')
# pg.moveTo(0.5 * pg.size()[0], 0.5 * pg.size()[1])
# pg.scroll(-500)
# back_location = pg.locateCenterOnScreen('icons/back.png', confidence=0.9)
# pg.click(back_location.x, back_location.y, duration=0.5)


import pyautogui as pg
import random

class AutoBrowserSearch:
    def __init__(self, count_visit):
        pg.FAILSAFE = True
        pg.PAUSE = 2
        self.count_visit = count_visit
        self.key_words = ["hello world", "cats", "planes"]

    def open_chrome(self):
        icon_location = pg.locateCenterOnScreen('icons/chrome.png', confidence=0.9)
        pg.click(icon_location.x, icon_location.y, duration=0.5)

    def search_random_word(self):
        random_word = random.choice(self.key_words)
        pg.hotkey('ctrl', 'shift', 'n')
        pg.typewrite(random_word, interval=0.2)
        pg.hotkey('enter')

    def search_url(self):
        pg.hotkey('ctrl', 'f')
        pg.typewrite('https', interval=0.2)
        pg.hotkey('ctrl', 'enter')

    def scroll_page(self):
        pg.moveTo(0.5 * pg.size()[0], 0.5 * pg.size()[1], duration=0.5)
        pg.scroll(-500)
        pg.sleep(random.uniform(5, 15))
        self.push_back()

    def push_back(self):
        back_location = pg.locateCenterOnScreen('icons/back.png', confidence=0.9)
        pg.click(back_location.x, back_location.y, duration=0.5)


if __name__ == "__main__":
    count_visit = int(input("Write count of visit of websites: "))
    auto_browser = AutoBrowserSearch(count_visit)
    auto_browser.open_chrome()
    auto_browser.search_random_word()
    for visit in range(auto_browser.count_visit):
        auto_browser.search_url()
        auto_browser.scroll_page()


# import pyautogui as pg
# import random
#
# class AutoBrowserInteraction:
#     def __init__(self):
#         pg.FAILSAFE = True
#         pg.PAUSE = 2
#         self.key_words = ["hello world", "cats", "planes"]
#
#     def click_icon(self, icon_path, duration=0.5):
#         icon_location = pg.locateCenterOnScreen(icon_path, confidence=0.9)
#         pg.click(icon_location.x, icon_location.y, duration=duration)
#
#     def type_and_enter(self, text, interval=0.1):
#         pg.typewrite(text, interval=interval)
#         pg.hotkey('enter')
#
#     def search_random_word(self):
#         random_word = random.choice(self.key_words)
#         pg.hotkey('ctrl', 'shift', 'n')
#         self.type_and_enter(random_word)
#
#     def search_url(self):
#         pg.hotkey('ctrl', 'f')
#         self.type_and_enter('https')
#         pg.hotkey('ctrl', 'enter')
#
#     def scroll_page(self, distance=-500):
#         pg.moveTo(0.5 * pg.size()[0], 0.5 * pg.size()[1])
#         pg.scroll(distance)
#
#     def go_back(self, icon_path='icons/back.png'):
#         back_location = pg.locateCenterOnScreen(icon_path, confidence=0.9)
#         if back_location:
#             self.click_icon(icon_path)
#
# if __name__ == "__main__":
#     auto_browser = AutoBrowserInteraction()
#     auto_browser.click_icon('icons/chrome.png')
#     auto_browser.search_random_word()
#     auto_browser.search_url()
#     auto_browser.scroll_page()
#
#     auto_browser.go_back()
#     auto_browser.search_url()
#     auto_browser.scroll_page()
#
#     auto_browser.go_back()