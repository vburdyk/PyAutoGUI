# AutoBrowserSearch

AutoBrowserSearch is a Python script designed to automate web browser actions using PyAutoGUI. This script performs automated browsing tasks, such as searching for specific URLs and random keywords in an incognito Chrome browser window.

## How to Use

### Requirements
```bash
- pip install -r requirements.txt
```

### Installation
1. Clone this repository or download the `main.py` file.
2. Install the required Python packages by running: `pip install pyautogui`

### Usage
1. Run the script in a Python environment.
2. Follow the prompts to enter the count of website visits and the website URL to search.
3. The script will open Chrome in incognito mode and search for random keywords from a predefined list.
4. It will then search for the provided URL, scrolling the page and simulating 'Enter' as necessary.

## File Structure
- `main.py`: Contains the main Python script.
- `icons/`: Directory holding the icon images used for locating elements on the screen.

## Additional Notes
Ensure that the icons used for locating elements (chrome.png, 1of1.png, back.png) are placed in the icons/ directory.
Adjust the key_words list in the script to include desired keywords for random searches.
Disclaimer
This script utilizes PyAutoGUI for browser automation. Ensure the screen resolution, browser window size, and element positions are compatible with the provided icons and script configuration.

## How to Run
```bash
python main.py
```