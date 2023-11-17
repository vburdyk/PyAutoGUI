import pyautogui as pg
import random

class AutoBrowserSearch:
    def __init__(self, count_visit, unique_url):
        """
        Initializes the AutoBrowserSearch class.

        Args:
        - count_visit (int): Number of website visits to perform.
        - unique_url (str): The URL to search for.
        """
        pg.FAILSAFE = True
        pg.PAUSE = 2
        self.count_visit = count_visit
        self.unique_url = unique_url
        self.key_words = ["hello world", "daitex software", "planes"]

    def open_chrome(self):
        """
        Opens the Chrome browser.
        """
        icon_location = pg.locateCenterOnScreen('icons/chrome.png', confidence=0.9)
        pg.click(icon_location.x, icon_location.y, duration=0.5)

    def search_random_word(self):
        """
        Searches for a random word from the predefined list.
        """
        random_word = random.choice(self.key_words)
        pg.hotkey('ctrl', 'shift', 'n')
        pg.typewrite(random_word, interval=0.2)
        pg.hotkey('enter')

    def search_url(self):
        """
        Searches for the 'https' string on the webpage.
        """
        pg.hotkey('ctrl', 'f')
        pg.typewrite('https', interval=0.2)
        pg.hotkey('ctrl', 'enter')

    def search_unique_url(self):
        """
        Searches for the unique URL specified during initialization.
        """
        if not hasattr(self, 'found_unique_url'):
            pg.hotkey('ctrl', 'f')
            pg.typewrite(self.unique_url, interval=0.2)
            try:
                one_of_one = pg.locateOnScreen('icons/1of1.png', confidence=0.9)
                if one_of_one is not None:
                    pg.hotkey('ctrl', 'enter')
                    pg.sleep(random.uniform(5 * 60, 10 * 60))
                    self.found_unique_url = True
                else:
                    raise pg.ImageNotFoundException
            except pg.ImageNotFoundException:
                self.found_unique_url = False
                self.search_url()
        else:
            self.search_url()

    def go_back_and_press_enter(self):
        """
        Simulates the action of going back and pressing 'Enter'.
        """
        back_location = pg.locateCenterOnScreen('icons/back.png', confidence=0.9)
        pg.click(back_location.x, back_location.y, duration=0.5)
        pg.hotkey('ctrl', 'f')
        pg.hotkey('enter')

    def scroll_page(self):
        """
        Scrolls the webpage and simulates 'Enter'.
        """
        pg.moveTo(0.5 * pg.size()[0], 0.5 * pg.size()[1], duration=0.5)
        pg.scroll(-500)
        pg.sleep(random.uniform(5, 15))
        self.go_back_and_press_enter()


if __name__ == "__main__":
    count_visit = int(input("Write count of visit of websites: "))
    url = input("Write website which you want to search: ")
    auto_browser = AutoBrowserSearch(count_visit, url)
    auto_browser.open_chrome()
    auto_browser.search_random_word()
    for visit in range(auto_browser.count_visit):
        auto_browser.search_unique_url()
        auto_browser.scroll_page()