from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to ChromeDriver (if not in the same folder, use absolute path)
chrome_driver_path = "C:\\Users\solai\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Set up Selenium
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run without opening browser
driver = webdriver.Chrome(service=service, options=options)

# Open TradingView Gold Page
driver.get("https://www.tradingview.com/symbols/XAGUSD/")

try:
    # Wait for the gold price element to be visible
    price_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#js-category-content > div.tv-react-category-header > div.js-symbol-page-header-root > div > div > div > div.quotesRow-pAUXADuj > div:nth-child(1) > div > div.lastContainer-JWoJqCpY > span.last-JWoJqCpY.js-symbol-last > span')))

    # Get the gold price
    silver_price = price_element.text
    print("Silver Price (USD/oz):", silver_price)

except Exception as e:
    print("Error extracting price:", e)

finally:
    # Close the browser
    driver.quit()