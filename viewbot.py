import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# setting up relative file path
dirname = os.path.dirname(__file__)
driverpath = dirname + "/chromedriver"
print("Running from: " + driverpath)

# gets user input
link = input("Enter your link: ")
views = int(input("How many views: "))

# configures webdriver options
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path=driverpath)

# scrapes proxies from provider
driver.get("https://sslproxies.org/")
# scrolls table with proxies into view
driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//table[@class='table table-striped table-bordered']//th[contains(., 'IP Address')]"))))
ips = []
ports = []
for i in range(views):
    try:
        # cycles through rows in table using XPATH; scrapes content
        ip = driver.find_element_by_xpath('//*[@id="list"]/div/div[2]/div/table/tbody/tr[{}]/td[1]'.format(i)).text
        port = driver.find_element_by_xpath('//*[@id="list"]/div/div[2]/div/table/tbody/tr[{}]/td[2]'.format(i)).text
        ips.append(ip)
        ports.append(port)
    except:
        print("Table entry {} not found".format(i))
driver.quit()

# formats proxies to make them usable
proxies = []
for i in range(0, len(ips)):
    proxies.append(ips[i]+':'+ports[i])
print("Proxies used: ")
print(proxies)

for i in range(0, len(proxies)):
    # visits site; configures driver to use new proxy each itme
    try:
        print("Proxy selected: {}".format(proxies[i]))
        options = webdriver.ChromeOptions()
        options.add_argument('--proxy-server={}'.format(proxies[i]))
        driver = webdriver.Chrome(options=options, executable_path=driverpath)
        driver.get(link)
        driver.execute_script("window.scrollTo(0, 1000);")
        driver.quit()
    except Exception:
        driver.quit()