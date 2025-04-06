import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to ChromeDriver (if not in the same folder, use absolute path)
chrome_driver_path = "C:\\Users\solai\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Set up Selenium
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run without opening browser
driver = webdriver.Chrome(service=service, options=options)

# Open TradingView Gold Page
driver.get("https://www.tradingview.com/symbols/XAUUSD/")

try:
    # Wait for the gold price element to be visible
    price_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#js-category-content > div.tv-react-category-header > div.js-symbol-page-header-root > div > div > div > div.quotesRow-pAUXADuj > div:nth-child(1) > div > div.lastContainer-JWoJqCpY > span.last-JWoJqCpY.js-symbol-last > span'))
    )

    # Get the gold price
    gold_price = price_element.text
    print("Gold Price (USD/oz):", gold_price)

except Exception as e:
    print("Error extracting price:", e)

# Open TradingView Gold Page
driver.get("https://www.tradingview.com/symbols/XAGUSD/")

try:
    # Wait for the gold price element to be visible
    price_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#js-category-content > div.tv-react-category-header > div.js-symbol-page-header-root > div > div > div > div.quotesRow-pAUXADuj > div:nth-child(1) > div > div.lastContainer-JWoJqCpY > span.last-JWoJqCpY.js-symbol-last > span')))

    # Get the gold price
    silver_price = price_element.text
    print("Silver Price (USD/oz):", silver_price)

finally:
    # Close the browser
    driver.quit()

# Authorize the API using the downloaded credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

# Path to your downloaded credentials JSON file
creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\Users\solai\Downloads\chromedriver-win64\chromedriver-win64\skillful-radar-360717-6371572bc472.json", scope)

# Authorize gspread client
client = gspread.authorize(creds)

# Open the Google Sheet (use the sheet name or URL)
sheet = client.open_by_key('18XY2LOMgtWWszcsRVgXmd_qAvZJolrLDGkAaSg4xwa4').sheet1  # Use the appropriate sheet name

# Write gold and silver prices into the sheet
# Update header row with titles
sheet.update(range_name='A1', values=[['Gold Price (USD/oz)']])
sheet.update(range_name='B1', values=[['Silver Price (USD/oz)']])

# Update with the actual prices in the second row
sheet.update(range_name='A2', values=[[gold_price]])  # Wrap gold_price in a list inside a list
sheet.update(range_name='B2', values=[[silver_price]])  # Wrap silver_price in a list inside a list

response = sheet.update(range_name='A2', values=[[gold_price]])
print("Response from Google Sheets:", response)

response = sheet.update(range_name='B2', values=[[silver_price]])
print("Response from Google Sheets:", response)

print("Prices successfully updated to Google Sheets!")