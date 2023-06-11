from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--disable-web-security");
options.add_argument("--window-size=1920,1200")
options.add_argument('--headless')
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://www.nike.com/nl/en/t/air-force-1-07-shoes-GjGXSP/CW2288-111")

# title = driver.find_element(by=By.XPATH, value='//span[@id="productTitle"]')
# current_price = driver.find_element(by=By.XPATH, value='//div[@id="corePrice_feature_div"]//span[@data-a-color="price"]/span[1]')
# image = driver.find_element(by=By.XPATH, value='//div[@id="imgTagWrapperId"]/img')
#button = driver.find_element(by=By.XPATH, value='//*[@id="pdp-6-up"]/img[1]')
#button = driver.find_element(by=By.CSS_SELECTOR, value= '#RightRail > div > div.prl6-sm.prl0-lg > div > details:nth-child(2) > div > div > div > p > button').click()
#print(driver.page_source)
button = driver.find_element(by=By.CLASS_NAME, value = 'css-ov1ktg').click()
print(button)


# product_data = {
# 'title': title.text,
# 'current_price': current_price.get_attribute('innerHTML'),
# 'image_url': image.get_attribute('src')
# }

# print(product_data)
driver.quit()