Viewbot.py
=========
A Python script that generates unique, proxy-driven views for any inputted website. Uses Selenium to scrape free proxies from providers, then aggregates them and deploys an automated web driver with a rotating IP address. Designed to generate one-time views for pages on-load.

Dependencies
------------
- All code is written in Python 3.
- Relies on the 'selenium' library.
- Requires installation of Google Chrome.
- Requires installation of chromedriver, a separate executable used by Selenium.

Setup
-----
- Clone this repository to your desktop; make sure to keep viewbot.py and the included chromedriver file in the same folder.
- `python3 -m pip install selenium`
- [Download](https://chromedriver.chromium.org/downloads "https://chromedriver.chromium.org/downloads") the version of chromedriver that matches your version of Google Chrome. The one included in the repository corresponds to Chrome version 93. If this doesn't correspond to your version of Chrome, replace it.

Usage
-----
### Local ###
Execute the viewbot.py file. Input your desired website, and then the requisite amount of views. 

(Keep in mind that the providers this script scrapes proxies from may limit the amount you can extract; 100 is generally the maximum per run.)

### Replit ###
Add the following snippets beneath every initialization of the webdriver to avoid crashes:
- `options.add_argument("--no-sandbox")`
- `options.add_argument("--disable-dev-shm-usage")`

Remove every occurrence of `executable_path=driverpath`.
