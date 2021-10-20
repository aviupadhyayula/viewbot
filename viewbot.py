import os
import time
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

def get_input():
    global link
    global views
    global delay
    link = input("Link: ")
    views = int(input("Views: "))
    delay = int(input("Delay: "))

def init_driver():
    dirname = os.path.dirname(__file__)
    global driverpath
    driverpath = r'%s' % dirname + r'/chromedriver'
    print("Running Selenium from: " + driverpath)
    options = webdriver.ChromeOptions()
    global driver
    driver = webdriver.Chrome(options=options, executable_path=driverpath)

def scrape_proxies():
    driver.get("https://sslproxies.org/")
    try:
        driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//table[@class='table table-striped table-bordered']//th[contains(., 'IP Address')]"))))
    except TimeoutException:
        print('Proxy table not found.')
    else:
        ips = []
        ports = []
        for i in range(1, views + 1):
            try:
                ip = driver.find_element(By.XPATH, '//*[@id="list"]/div/div[2]/div/table/tbody/tr[{}]/td[1]'.format(i))
                port = driver.find_element(By.XPATH, '//*[@id="list"]/div/div[2]/div/table/tbody/tr[{}]/td[2]'.format(i))
            except NoSuchElementException:
                print('Table entry {} not found'.format(i))
            else:
                ips.append(ip.text)
                ports.append(port.text)
        proxies = format_proxies(ips, ports)
        driver.quit()
        return proxies

def format_proxies(ips, ports):
    proxies = []
    for i in range(0, len(ips)):
        proxies.append(ips[i] + ':' + ports[i])
    return proxies

def create_traffic(proxies):
    for i in range(0, len(proxies)):
        print('Proxy selected: ' + str(proxies[i]))
        options = webdriver.ChromeOptions()
        options.add_argument('--proxy-server={}'.format(proxies[i]))
        driver = webdriver.Chrome(options=options, executable_path=driverpath)
        driver.get(link)
        try:
            elem = driver.find_element(By.NAME, 'body')
            element.send_keys(Keys.ARROW_DOWN, Keys.ARROW_UP, ' ')
            time.sleep(delay)
            driver.quit()
        except NoSuchElementException:
            driver.quit()

def main():
    get_input()
    init_driver()
    proxies = scrape_proxies()
    create_traffic(proxies)

if __name__ == "__main__":
    main()