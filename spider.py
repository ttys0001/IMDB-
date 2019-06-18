from selenium import webdriver
import time
import json
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.firefox.options import Options
driver = webdriver.Firefox(executable_path='geckodriver')
driver.maximize_window()
driver.implicitly_wait(60)

#driver.quit
driver.get('https://m.imdb.com/title/tt7605074/reviews?sort=helpfulnessScore&dir=desc&ratingFilter=0')
while 1:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    driver.find_element_by_id("load-more-trigger").click()
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

result = driver.find_elements_by_class_name("text")
text = []
for i in result:
    if i.text:
        text.append(i.text)

print(len(result))
import csv

with open("test.csv", "w") as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(["index", "text"])
    for k, v in enumerate(text):
        csv_head = [str(k), str(v)]
        writer.writerow(csv_head)
