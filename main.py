from flask import Flask, render_template
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import re
from utils import twitter_embed
from webdriver_manager.chrome import ChromeDriverManager

s = Service(ChromeDriverManager().install())
tw = webdriver.Chrome(service=s)

tw.get('https://publish.twitter.com/')
time.sleep(1)
url = tw.find_element(by=By.XPATH, value='//*[@id="configuration-query"]')
url.send_keys('https://twitter.com/PopularFront_')
time.sleep(1)

enter = tw.find_element(by=By.XPATH, value='//*[@id="top"]/div/form/section/button')
enter.click()
time.sleep(1)

timeline = tw.find_element(by=By.XPATH, value='//*[@id="app-root"]/div/article[1]/ul/li[1]/span')
timeline.click()
time.sleep(1)

html_content = tw.find_elements(by=By.XPATH, value='//*[@id="app-root"]/div/article[2]/div[1]/div/div/samp/code')
urls = []

for i in html_content:
    urls.append(i.get_attribute('innerHTML'))

urls_list_temp = [re.sub(r'&gt;', '>', k) for k in urls]
urls_list = [re.sub(r'&lt;', '<', k) for k in urls_list_temp]
print(urls_list)

"""

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
if __name__ == "__main__":
    app.run(debug=True)
"""