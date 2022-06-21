from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


##Ignition Login Info
Username = "Input User Here"
Password = "Input Password Here"

##Url of the Ignition Test
TestUrl = "https://www.inductiveuniversity.com/challenge/installing-and-upgrading-ignition/question"


class seleniumFunctions():

    def GetCurrentHTML(driver):
        
        html = driver.page_source
        
        return html


    #Handles Logging into Ignition Site
    def IgnitionLogin(driver):

        #Username/Email Element
        user = driver.find_element_by_id("id_username")
        user.clear()
        user.send_keys(Username)

        #Password Element
        password = driver.find_element_by_id("id_password")
        password.clear()
        password.send_keys(Password)
        password.send_keys(Keys.RETURN)


    def StartWebBrowser():

        driver = webdriver.Firefox()
        driver.get(TestUrl)

        #To Login into Ignition Test
        seleniumFunctions.IgnitionLogin(driver)

        return driver

        #GrabAllQuestionsText(driver)

"""
def GrabAllQuestionsText(driver):

    try:
        myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'challenge-questions')))
        print("Page is Ready")
    except TimeoutError:
        print ("Never Found Element")

    Questions = driver.find_elements_by_class_name("row")

    
    ##for Question in Questions:
        
      ##  Text = Question.find_element_by_xpath('.//div[@class="title"]/a')
       ## /html/body/div[2]/div/div[3]/div[1]/div/div[3]/div/div/div[1]/span

   ## print(Questions)
"""
    


#Starts Program
#StartWebBrowser()


    

