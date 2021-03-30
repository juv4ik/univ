import time
from selenium import webdriver

optionsChrome = webdriver.ChromeOptions()
optionsChrome.add_argument('--user-data-dir=C:\\Users\\FUNNY\\PycharmProjects\\onliner_news')

driver = webdriver.Chrome(executable_path='chromedriver.exe',
                          options=optionsChrome)
time.sleep(5)
driver.get('https://jufc.ru/index.php')

login_input = driver.find_elements_by_xpath("/html/body/main/div/div[1]/div[1]/div/div/form/input[1]")
print(login_input)
login_input[0].send_keys('juv4ik')

password_input = driver.find_elements_by_xpath("/html/body/main/div/div[1]/div[1]/div/div/form/input[2]")
password_input[0].send_keys('******')
20
xpath = "//div/div[@class='row' and 1]/div[2]/div[@class='spec-product-middle' and 1]/div[@class='spec-product-middle-wrap-title' and 1]/h2[@class='spec-product-middle-title' and 1]/a[@class='product-link' and 1]"
elements = driver.find_elements_by_xpath(xpath)

for element in elements:
    print(element.text)