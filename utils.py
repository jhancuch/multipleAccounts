import re
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def twitter_embed(url1 = None, url2 = None, url3 = None, url4 = None):
    """
    blah blah blah
    Parameters:
    Returns:
    """
    s = Service(ChromeDriverManager().install())
    tw = webdriver.Chrome(service=s)

    html = []

    if url1 is not None:
        html.append(twitter_selenium(tw, url1))
        
    if url2 is not None:
        html.append(twitter_selenium(tw, url2))

    if url3 is not None:
        html.append(twitter_selenium(tw, url3))

    if url4 is not None:
        html.append(twitter_selenium(tw, url4))

    urls_list_temp = [re.sub(r'&gt;', '>', k) for k in html]
    urls_list = [re.sub(r'&lt;', '<', k) for k in urls_list_temp]

    return urls_list

def twitter_selenium(driver, path):
    """
    blah blah blah
    Parameters:
    Returns:
    """
    driver.get('https://publish.twitter.com/')
    time.sleep(1)
    
    url = driver.find_element(by=By.XPATH, value='//*[@id="configuration-query"]')
    url.send_keys(path)
    time.sleep(1)

    enter = driver.find_element(by=By.XPATH, value='//*[@id="top"]/div/form/section/button')
    enter.click()
    time.sleep(1)

    timeline = driver.find_element(by=By.XPATH, value='//*[@id="app-root"]/div/article[1]/ul/li[1]/span')
    timeline.click()
    time.sleep(1)

    html_content = driver.find_elements(by=By.XPATH, value='//*[@id="app-root"]/div/article[2]/div[1]/div/div/samp/code')
    html = []

    for i in html_content:
        html.append(i.get_attribute('innerHTML'))

    html = ''.join(html)

    return html


