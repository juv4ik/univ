import time
from selenium import webdriver

optionsChrome = webdriver.ChromeOptions()
#optionsChrome.add_argument('--user-data-dir=C:\\Users\\FUNNY\\PycharmProjects\\onliner_news\onl1')

driver = webdriver.Chrome(executable_path='chromedriver.exe',
                          options=optionsChrome)
time.sleep(5)
driver.get('https://people.onliner.by')

#xpath = "//a[1]/@href"
xtst1 = "/html/body/div[1]/div/div/div[2]/div/div/div[3]/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/a/@href"
xtst2 = "/html/body/div[1]/div/div/div[2]/div/div/div[3]/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[1]/div/div/a"
#elements = driver.find_elements_by_xpath(xpath)
tst1 = driver.find_elements_by_xpath(xtst1)
tst2 = driver.find_elements_by_xpath(xtst2)

for element in tst1:
    print(element.text)

for element in tst2:
    print(element.text)

#for element in elements:
#    print(element.text)


