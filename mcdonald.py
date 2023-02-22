from selenium import webdriver
from selenium.webdriver.common.by import By
from surveyfunctions import multiple_columns_one_choice_each, textbox, satisfied_table, yes_no, checklist, driver


def survey(code, surveyResult):
    global running
    running = True
    driver.get("http://mcdvoice.com")

    for i in range(1, 7):
        xpath = '//*[@id="CN'+str(i)+'"]'
        driver.find_element(By.XPATH, xpath).send_keys(code[i-1])
    driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()
    if(not driver.find_elements(By.CLASS_NAME, "rbList")):
        driver.close()
        running=False
        return

    while(driver.find_elements(By.XPATH, '//*[@id="NextButton"]')):
        if(driver.find_elements(By.CLASS_NAME, "rbList")):
            if(driver.find_elements(By.TAG_NAME, "textarea")):
                textbox()
                continue
            else:
                multiple_columns_one_choice_each()
                continue
        if(driver.find_elements(By.TAG_NAME, "tbody")):
            body=driver.find_element(By.TAG_NAME, "tbody")
            rows=body.find_elements(By.TAG_NAME, "tr")
            if(len(rows)>1 or rows[0].find_elements(By.CLASS_NAME,"Opt5")):
                satisfied_table(rows)
                continue
            else:
                yes_no(rows)
                continue
        if(driver.find_elements(By.CLASS_NAME, "cataList")):
            checklist()
            continue
        driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    code=driver.find_element(By.CLASS_NAME, "ValCode").text
    surveyResult[0]=code
    driver.close()
    running=False
    return

def isDone():
    return (not running)







