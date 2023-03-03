from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import random

def survey(code, surveyResult):
    global running
    running = True
    driver=webdriver.Firefox()
    driver.get("http://mcdvoice.com")
    for i in range(1, 7):
        xpath = '//*[@id="CN'+str(i)+'"]'
        driver.find_element(By.XPATH, xpath).send_keys(code[i-1])
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()
    if(not driver.find_elements(By.CLASS_NAME, "rbList")):
        driver.close()
        running=False
        return
    
    #How did you place your order? (Choose 1)
    survey = driver.find_element(By.CLASS_NAME, "rbList")
    row = survey.find_element(By.CLASS_NAME, "Opt3")
    button = row.find_element(By.XPATH, ".//input[@type='radio']")
    driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    #Please select your visit type (Choose 1)
    survey = driver.find_element(By.CLASS_NAME, "rbList")
    row = survey.find_element(By.CLASS_NAME, "Opt3")
    button = row.find_element(By.XPATH, ".//input[@type='radio']")
    driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    #Rate your overall satisfaction (Satisfied table)
    body=driver.find_element(By.TAG_NAME, "tbody")
    rows=body.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        option = row.find_element(By.CLASS_NAME, "Opt5")
        button = option.find_element(By.XPATH, ".//input[@type='radio']")
        driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    #Did employee greet you by name or thank you? (y/n)
    body=driver.find_element(By.TAG_NAME, "tbody")
    rows=body.find_elements(By.TAG_NAME, "tr")
    box = rows[0].find_element(By.CLASS_NAME, "Opt2")
    button = box.find_element(By.XPATH, ".//input[@type='radio']")
    driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    #Rate satisfaction - food/service (Satisfied table)
    body=driver.find_element(By.TAG_NAME, "tbody")
    rows=body.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        option = row.find_element(By.CLASS_NAME, "Opt5")
        button = option.find_element(By.XPATH, ".//input[@type='radio']")
        driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()
    
    
    #Rate satisfaction 2 - restaurant info (Satisfied table)
    body=driver.find_element(By.TAG_NAME, "tbody")
    rows=body.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        option = row.find_element(By.CLASS_NAME, "Opt5")
        button = option.find_element(By.XPATH, ".//input[@type='radio']")
        driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    #What items did you order? (Checklist)
    body = driver.find_element(By.CLASS_NAME, "cataList")
    options = body.find_elements(By.CLASS_NAME, "cataOption")
    for option in options:
        check = option.find_element(By.CLASS_NAME, "checkboxholder")
        checkbox = check.find_element(By.XPATH, ".//input[@type='checkbox']")
        if (random.randint(0, 1) == 1):
            driver.execute_script("arguments[0].click();", checkbox)
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    #Item satisfaction (Satisfied table)
    body=driver.find_element(By.TAG_NAME, "tbody")
    rows=body.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        option = row.find_element(By.CLASS_NAME, "Opt5")
        button = option.find_element(By.XPATH, ".//input[@type='radio']")
        driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    #Did you experience a problem? (y/n)
    body=driver.find_element(By.TAG_NAME, "tbody")
    rows=body.find_elements(By.TAG_NAME, "tr")
    box = rows[0].find_element(By.CLASS_NAME, "Opt2")
    button = box.find_element(By.XPATH, ".//input[@type='radio']")
    driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()


    #Liklihood that you revist? (Satisfied table)
    body=driver.find_element(By.TAG_NAME, "tbody")
    rows=body.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        option = row.find_element(By.CLASS_NAME, "Opt5")
        button = option.find_element(By.XPATH, ".//input[@type='radio']")
        driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    #Why were you highly satisfed? (Text entry)
    driver.find_element(
    By.TAG_NAME, 'textarea').send_keys('food was awesome')
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    #How many times have you visited MCD? (Choose 1)
    survey = driver.find_element(By.CLASS_NAME, "rbList")
    row = survey.find_element(By.CLASS_NAME, "Opt3")
    button = row.find_element(By.XPATH, ".//input[@type='radio']")
    driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()


    #Favorite fast food? (Choose 1)
    survey = driver.find_element(By.CLASS_NAME, "rbList")
    row = survey.find_element(By.CLASS_NAME, "Opt3")
    button = row.find_element(By.XPATH, ".//input[@type='radio']")
    driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    #Trust MCD? (Satisfied table)
    body=driver.find_element(By.TAG_NAME, "tbody")
    rows=body.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        option = row.find_element(By.CLASS_NAME, "Opt5")
        button = option.find_element(By.XPATH, ".//input[@type='radio']")
        driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    #In case of demographic question: 
    try:
        driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()
    except NoSuchElementException:
        pass
    code=driver.find_element(By.CLASS_NAME, "ValCode").text
    surveyResult[0]=code
    driver.close()
    running=False
    return

def isDone():
    return (not running)







