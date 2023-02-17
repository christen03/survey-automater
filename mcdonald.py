from selenium import webdriver;
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random

# Needs to be cleaned up with loops, + occasional demographic question

def survey(code, surveyResult):
    global running
    running=True
    driver= webdriver.Firefox()
    url="http://mcdvoice.com"
    driver.get(url)


    for i in range(1,6):
        xpath='//*[@id="CN'+str(i)+'"]'
        driver.find_element(By.XPATH,xpath).send_keys(code[i-1])

    driver.find_element(By.XPATH,'//*[@id="NextButton"]').click()

    # How did you place your order? => Mobile app (One choice columns)
    survey=driver.find_element(By.CLASS_NAME, "rbList")
    row=survey.find_element(By.CLASS_NAME, "Opt3")
    button=row.find_element(By.XPATH, ".//input[@type='radio']")
    driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH,'//*[@id="NextButton"]').click()

    #Select your visit type => Drive-thru (One choice columns)
    survey=driver.find_element(By.CLASS_NAME, "rbList")
    row=survey.find_element(By.CLASS_NAME, "Opt2")
    button=row.find_element(By.XPATH, ".//input[@type='radio']")
    driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH,'//*[@id="NextButton"]').click()

    #Please rate overall satisfaction => Highly Satisfied (5-Choice row)
    survey=driver.find_element(By.TAG_NAME, "tbody")
    box=survey.find_element(By.CLASS_NAME, "Opt5")
    button=survey.find_element(By.XPATH, ".//input[@type='radio']")
    driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH,'//*[@id="NextButton"]').click()

    #Did your employee ask mobile app? => Yes (2-choice row)
    body=driver.find_element(By.TAG_NAME, "tbody")
    row=body.find_element(By.TAG_NAME, "tr")
    box=row.find_element(By.CLASS_NAME, "Opt1")
    button=box.find_element(By.XPATH, ".//input[@type='radio']")
    driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH,'//*[@id="NextButton"]').click()

    #Did your employee greet/thank you? => Yes (2-choice row)
    body=driver.find_element(By.TAG_NAME, "tbody")
    row=body.find_element(By.TAG_NAME, "tr")
    box=row.find_element(By.CLASS_NAME, "Opt1")
    button=box.find_element(By.XPATH, ".//input[@type='radio']")
    driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH,'//*[@id="NextButton"]').click()

    #Rate satisfaction => All highly satisfied (Multi-choice rows)
    body=driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/form/div/table/tbody")
    rows = body.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        option=row.find_element(By.CLASS_NAME, "Opt5")
        button=option.find_element(By.XPATH, ".//input[@type='radio']")
        driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH,'//*[@id="NextButton"]').click()

    #Rate satisfaction2 => All highly satisfied (Multi-choice rows)
    body=driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/form/div/table/tbody")
    rows = body.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        option=row.find_element(By.CLASS_NAME, "Opt5")
        button=option.find_element(By.XPATH, ".//input[@type='radio']")
        driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH,'//*[@id="NextButton"]').click()

    #What items did you order? => Random (Multi-choice rows)
    body=driver.find_element(By.CLASS_NAME, "cataList")
    options = body.find_elements(By.CLASS_NAME, "cataOption")
    for option in options:
        check=option.find_element(By.CLASS_NAME, "checkboxholder")
        checkbox=check.find_element(By.XPATH, ".//input[@type='checkbox']")
        if(random.randint(0,1)==1):
            driver.execute_script("arguments[0].click();", checkbox)
    driver.find_element(By.XPATH,'//*[@id="NextButton"]').click()

    #Satisfaction with your food? => All highly satisfied (Multi-choice rows)
    body=driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/form/div/table/tbody")
    rows = body.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        option=row.find_element(By.CLASS_NAME, "Opt5")
        button=option.find_element(By.XPATH, ".//input[@type='radio']")
        driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH,'//*[@id="NextButton"]').click()

    #Did you have a problem with your visit? => No (2-choice row)
    body=driver.find_element(By.TAG_NAME, "tbody")
    row=body.find_element(By.TAG_NAME, "tr")
    box=row.find_element(By.CLASS_NAME, "Opt2")
    button=box.find_element(By.XPATH, ".//input[@type='radio']")
    driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH,'//*[@id="NextButton"]').click()

    #Likelihood you return? => All highly likely (Multi-choice rows)
    body=driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/form/div/table/tbody")
    rows = body.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        option=row.find_element(By.CLASS_NAME, "Opt5")
        button=option.find_element(By.XPATH, ".//input[@type='radio']")
        driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH,'//*[@id="NextButton"]').click()

    #Why satisfied? => "food was awesome" (Text entry)
    driver.find_element(By.XPATH,'//*[@id="S081000"]').send_keys('food was awesome')
    driver.find_element(By.XPATH,'//*[@id="NextButton"]').click()

    #Were you asked to pull out of drive thru? => No (2-choice rows)
    body=driver.find_element(By.TAG_NAME, "tbody")
    row=body.find_element(By.TAG_NAME, "tr")
    box=row.find_element(By.CLASS_NAME, "Opt2")
    button=box.find_element(By.XPATH, ".//input[@type='radio']")
    driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH,'//*[@id="NextButton"]').click()

    #How much did you visit MCD in the past 30 days? => Two (One choice columns)
    survey=driver.find_element(By.CLASS_NAME, "rbList")
    row=survey.find_element(By.CLASS_NAME, "Opt2")
    button=row.find_element(By.XPATH, ".//input[@type='radio']")
    driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH,'//*[@id="NextButton"]').click()

    #Favorite fast food restaurant? => Random ;) (One choice columns)
    survey=driver.find_element(By.CLASS_NAME, "rbList")
    fun = random.randint(1,11)
    row=survey.find_element(By.CLASS_NAME, "Opt"+str(fun))
    button=row.find_element(By.XPATH, ".//input[@type='radio']")
    driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH,'//*[@id="NextButton"]').click()

    #MCD is a brand I trust => Strongly agree (5-choice row)
    survey=driver.find_element(By.TAG_NAME, "tbody")
    box=survey.find_element(By.CLASS_NAME, "Opt5")
    button=survey.find_element(By.XPATH, ".//input[@type='radio']")
    driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH,'//*[@id="NextButton"]').click()

    code=driver.find_element(By.CLASS_NAME, "ValCode").text
    surveyResult[0]=code
    driver.close()
    running=False
    print(code)
    return

def isDone():
    return (not running)



