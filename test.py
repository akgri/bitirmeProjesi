#%%
from contextlib import nullcontext
import time
import random
from bs4.builder import HTML
import pandas as pd
from bs4 import BeautifulSoup # daha ilkel bir html parse kutuphanesi
from selenium import webdriver

driver_path = "C:/webdriver/chromedriver.exe" # webdriver.exe konumunu göstermeliyiz.
driver = webdriver.Chrome(driver_path)
#
#%%
driver.get("https://www.kariyer.net/is-ilanlari/?kw=istatistik&sf=1d&is=1") #ana sayfa
#%%
nextpageXpath='//*[@id="__layout"]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[3]/div[27]/div/ul/li[14]/button'
from selenium.webdriver.common.action_chains import ActionChains
def nextpage():
    ActionChains(driver).move_to_element(driver.find_element_by_xpath(nextpageXpath)).perform()
    driver.find_element_by_xpath(nextpageXpath).click()
# %%
a=None
pageLinks=[]
driver.get("https://www.kariyer.net/is-ilanlari/?kw=istatistik&sf=1d&is=1")
while(a!=None):
    try:
        pageLinks.append(driver.current_url)
        nextpage()
    except:
        a="stop"
        break





# %%


# %%
