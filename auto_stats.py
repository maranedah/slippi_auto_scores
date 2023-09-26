from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options


def getStatsUrl(slp_paths):
    paths = "\n".join(slp_paths)
    stats_url = "https://vince.id.au/slippi-stats/"

    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Firefox(firefox_binary=FirefoxBinary(), options=options)
    browser.get(stats_url)
    browser.find_element_by_xpath(".//input").send_keys(paths)
    button = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "css-1fgnl9k"))
    )
    button.click()

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "css-uso7ts"))
    )
    url = browser.current_url
    browser.quit()
    print(url)
    return url


# slp_paths = ["C:\\Users\\mauri\\Documents\\Slippi\\vs YingLing\\Game_20210314T131439.slp", "C:\\Users\\mauri\\Documents\\Slippi\\vs YingLing\\Game_20210314T131759.slp", "C:\\Users\\mauri\\Documents\\Slippi\\vs YingLing\\Game_20210314T132157.slp"]
# getStatsUrl(slp_paths)
