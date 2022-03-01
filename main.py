from flask import Flask, render_template
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

s = Service(ChromeDriverManager().install())
tw = webdriver.Chrome(service=s)

tw.get('https://publish.twitter.com/')

url = tw.find_element(by=By.XPATH, value='//*[@id="configuration-query"]')
url.send_keys('https://twitter.com/PopularFront_')

enter = tw.find_element(by=By.XPATH, value='//*[@id="top"]/div/form/section/button')
enter.click()

timeline = tw.find_element(by=By.XPATH, value='//*[@id="app-root"]/div/article[1]/ul/li[1]/span')
timeline.click()

#html_content = tw.find_element(by=By.CLASS_NAME, value="EmbedCode-code")
# html_content = tw.find_elements_by_class_name('EmbedCode-code') -- get []
html_content = tw.find_elements(by=By.XPATH, value='//*[@id="app-root"]/div/article[2]/div[1]/div/div/samp/code/text()')
print(html_content)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
if __name__ == "__main__":
    app.run(debug=True)