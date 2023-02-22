from selenium import webdriver
from selenium.webdriver.common.by import By
import random

driver=webdriver.Firefox()


def multiple_columns_one_choice_each():
    survey = driver.find_element(By.CLASS_NAME, "rbList")
    row = survey.find_element(By.CLASS_NAME, "Opt3")
    button = row.find_element(By.XPATH, ".//input[@type='radio']")
    driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()

def satisfied_table(rows):
    for row in rows:
        option = row.find_element(By.CLASS_NAME, "Opt5")
        button = option.find_element(By.XPATH, ".//input[@type='radio']")
        driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()

def yes_no(rows):
    box = rows[0].find_element(By.CLASS_NAME, "Opt2")
    button = box.find_element(By.XPATH, ".//input[@type='radio']")
    driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()

def checklist():
    body = driver.find_element(By.CLASS_NAME, "cataList")
    options = body.find_elements(By.CLASS_NAME, "cataOption")
    for option in options:
        check = option.find_element(By.CLASS_NAME, "checkboxholder")
        checkbox = check.find_element(By.XPATH, ".//input[@type='checkbox']")
        if (random.randint(0, 1) == 1):
            driver.execute_script("arguments[0].click();", checkbox)
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()

def textbox():
    driver.find_element(
    By.TAG_NAME, 'textarea').send_keys('food was awesome')
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()