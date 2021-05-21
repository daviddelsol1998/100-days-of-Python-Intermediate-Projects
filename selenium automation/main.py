from selenium import webdriver

chrome_driver_path = 'C:\dev\chromedriver.exe'  # path where chromedriver is saved to be used with selenium
driver = webdriver.Chrome(
    executable_path=chrome_driver_path)  # webdriver.chrome tells the driver which browser is being used
driver.get('https://www.python.org')  # webdriver.get method opens a given website on a string
# driver.close() # webdriver.close closes active tab
# price = driver.find_element_by_id('priceblock_ourprice') # self explanatory
search_bar = driver.find_element_by_name('q')
print(search_bar)
doc_link = driver.find_element_by_css_selector('.documentation-widget a')  # self explanatory
print(doc_link.text)
bug_link = driver.find_element_by_xpath(
    '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')  # if all else fails xpath is unique
print(bug_link.text)
driver.quit()  # webdriver.quit shut down the browser
