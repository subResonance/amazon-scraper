from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

# Initializes product URLs, the .txt is updated by version to keep src_url constant
driver = webdriver.Chrome()
src_url = 'https://drive.google.com/file/d/1Vu2e_00dniSqkHH9115DP0qeqpwMuR4C/view'
driver.get(src_url)
raw_urls = driver.find_element_by_tag_name('pre').text
URLs = raw_urls.split()
driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')

# Scrapes each URL for the desired info
current_date = date.today().strftime("%m/%d/%Y")
products = []

for url in URLs:
    driver.get(url)
    try:
        itemTitle = driver.find_element_by_id('productTitle').text
    except:
        itemTitle = None
        print("Item at: ", url, " is no longer available!")
        continue
    try:
        itemSeller = driver.find_element_by_id('bylineInfo').text
    except:
        itemSeller = None
        print("Seller name unavailable for item: ", itemTitle)
    try:
        itemPrice = driver.find_element_by_id('price_inside_buybox').text
    except:
        try:
            itemPrice = driver.find_element_by_id('priceblock_ourprice').text
        except:
            itemPrice = None
            print("Price unavailable for item: ", itemTitle)
    try:
        itemRating = driver.find_element_by_id('acrPopover').get_attribute('title')
    except:
        itemRating = None
        print("Rating unavailable for item: ", itemTitle)
    try:
        item_num_ratings = driver.find_element_by_id('acrCustomerReviewText').text
    except:
        item_num_ratings = None
        print("Number of ratings unavailable for item: ", itemTitle)

    productObject = {
    "seller": itemSeller,
    "title": itemTitle,
    "price": itemPrice,
    "rating": itemRating,
    "num_ratings": item_num_ratings,
    "date": current_date
    }

    products.append(productObject)
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
driver.quit()

# Generates .json output file
with open('product_info.json', 'w') as outfile:
    json.dump(products, outfile, sort_keys=True, indent=4, separators=(',', ': '))

print("product_info.json successfully generated . . .")
