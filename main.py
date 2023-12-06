from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time


def getResearcherName():
    name = input("Enter Professor Name: ")
    return name


def searchProfessor(name):
    browser = webdriver.Chrome()
    browser.get('https://www.google.com/')

    m = browser.find_element(By.NAME, "q")
    m.send_keys(name + " google scholar")
    time.sleep(0.2)
    m.send_keys(Keys.ENTER)
    time.sleep(1.2)

    try:
        css_selector = 'div.yuRUbf a[jsname="UWckNb"]'
        element = browser.find_element(By.CSS_SELECTOR, css_selector)
        element.click()
        time.sleep(1.0)
        css_selector = 'span.gsc_a_h a.gsc_a_a'
        element = browser.find_element(By.CSS_SELECTOR, css_selector)
        element.click()
        time.sleep(1.0)
    except NoSuchElementException:
        print("Element not found")

    try:
        anchor_tags = browser.find_elements(By.CSS_SELECTOR, 'tbody#gsc_a_b tr.gsc_a_tr td.gsc_a_t a.gsc_a_at')
        year_tags = browser.find_elements(By.CSS_SELECTOR, 'td.gsc_a_y span.gsc_a_h.gsc_a_hc.gs_ibl')
        time.sleep(1.0)
        latest_pubications_link = [tag.get_attribute('href') for tag in anchor_tags]
        latest_pubications_name = [tag.get_attribute('text') for tag in anchor_tags]
        latest_pubications_year = [tag.text for tag in year_tags]
        time.sleep(2.0)
    except NoSuchElementException:
        print("Elements not found")
    return [latest_pubications_name, latest_pubications_link, latest_pubications_year]



if __name__ == "__main__":
    name = getResearcherName()
    res = searchProfessor(name)
    df = pd.DataFrame(list(zip(name, res[0], res[1], res[2])), columns=['Author', 'Publication Title','Publication Link', 'Year'])
    df["Author"] = name
    print(df)