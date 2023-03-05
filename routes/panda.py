from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random

def pandaSurvey(code, email, surveyResult):
    global running
    running = True
    driver=webdriver.Firefox()
    driver.get("http://pandaexpress.com/feedback")
    for i in range(1, 7):
        xpath = '//*[@id="CN'+str(i)+'"]'
        driver.find_element(By.XPATH, xpath).send_keys(code[i-1])
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    if(not driver.find_elements(By.CLASS_NAME, "Opt5")):
        driver.close()
        running=False
        return

    #Overall satisfaction (Multi column, one choice)
    option=driver.find_element(By.CLASS_NAME, 'Opt5')
    button=option.find_element(By.CLASS_NAME, "radioSimpleInput")
    driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()


    #Please rate your satisfaciton with (satisfaction table)
    body=driver.find_element(By.TAG_NAME, "tbody")
    rows=body.find_elements(By.TAG_NAME, "tr")
    for row in rows[1:]:
            option = row.find_element(By.CLASS_NAME, "Opt5")
            button = option.find_element(By.XPATH, ".//input[@type='radio']")
            driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    #Please rate your satisfaciton with #2 (satisfaction table)
    body=driver.find_element(By.TAG_NAME, "tbody")
    rows=body.find_elements(By.TAG_NAME, "tr")
    for row in rows[1:]:
            option = row.find_element(By.CLASS_NAME, "Opt5")
            button = option.find_element(By.XPATH, ".//input[@type='radio']")
            driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    #Overall satisfaction w/ price (Multi column, one choice)
    option=driver.find_element(By.CLASS_NAME, 'Opt5')
    button=option.find_element(By.CLASS_NAME, "radioSimpleInput")
    driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    #Primary reason for visiting Panda? (checklist)
    body = driver.find_element(By.CLASS_NAME, "cataList")
    options = body.find_elements(By.CLASS_NAME, "cataOption")
    for option in options:
        check = option.find_element(By.CLASS_NAME, "checkboxholder")
        checkbox = check.find_element(By.XPATH, ".//input[@type='checkbox']")
        if (random.randint(0, 1) == 1):
            driver.execute_script("arguments[0].click();", checkbox)
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    #Did you have a problem? (y/n)
    body=driver.find_element(By.TAG_NAME, "tbody")
    rows=body.find_elements(By.TAG_NAME, "tr")
    box = rows[1].find_element(By.CLASS_NAME, "Opt2")
    button = box.find_element(By.XPATH, ".//input[@type='radio']")
    driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    #What is the liklihood you will revisit? (satisfied table)
    body=driver.find_element(By.TAG_NAME, "tbody")
    rows=body.find_elements(By.TAG_NAME, "tr")
    for row in rows[1:]:
            option = row.find_element(By.CLASS_NAME, "Opt5")
            button = option.find_element(By.XPATH, ".//input[@type='radio']")
            driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    #Please tell us (txt entry)

    driver.find_element(
    By.TAG_NAME, 'textarea').send_keys('food was awesome')
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    #Satisfied with the health changes? (Multi column, 1)
    option=driver.find_element(By.CLASS_NAME, 'Opt5')
    button=option.find_element(By.CLASS_NAME, "radioSimpleInput")
    driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    #Satisfied with health and safety? (Multi column, 1)
    option=driver.find_element(By.CLASS_NAME, 'Opt5')
    button=option.find_element(By.CLASS_NAME, "radioSimpleInput")
    driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    #Recognize an employee? (y/n)
    body=driver.find_element(By.TAG_NAME, "tbody")
    rows=body.find_elements(By.TAG_NAME, "tr")
    box = rows[1].find_element(By.CLASS_NAME, "Opt2")
    button = box.find_element(By.XPATH, ".//input[@type='radio']")
    driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    #Hw many times have you visited? (Table of MCQ)
    option=driver.find_element(By.CLASS_NAME, 'Opt3')
    button=option.find_element(By.CLASS_NAME, "radioSimpleInput")
    driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    #Demographics, dragdown menu
    items=driver.find_elements(By.CLASS_NAME, 'rbList')
    for i in range(0,len(items)):
        choiceList=Select(items[i].find_element(By.ID, "R00013"+str(i)))
        choiceList.select_by_value('2')
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    #input email
    driver.find_element(By.XPATH, '//*[@id="S000057"]').send_keys(email)
    driver.find_element(By.XPATH, '//*[@id="S000064"]').send_keys(email)
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    surveyResult[0]="done"
    driver.quit()    
    running=False
    return

def isDone():
    return (not running)