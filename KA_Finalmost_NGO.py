from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from IPython.display import display
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
# import os


import pandas as pd
import time


options=Options()
options.headless=True
driver = webdriver.Chrome(executable_path = "C:/Users/USER/Desktop/NGO Darpan/chromedriver_win32/chromedriver.exe")
driver.implicitly_wait(10)

# options = webdriver.ChromeOptions()


prefs = {"download.default_directory" : "C:/Users/USER/Desktop/NGO Darpan/Data"}
# driver = webdriver.Chrome()
# driver.maximize_window()



df = pd.DataFrame(columns = ['Name', 'UniqueID','RegDate', 'FCRA No', 'NGO Type','Key Issues','Operational Area','Address','City','State','Telephone','Email','Mobile','Website','Member 1','Designation 1','Member 2','Designation 2'])
missing = []


try:
    for page in range(1,91):
        page_url = "https://ngodarpan.gov.in/index.php/home/statewise_ngo/9288/29/"+str(page)+"?per_page=100"
        driver.get(page_url)
        # storing the current window handle to get back to dashboard
        main_page = driver.current_window_handle
        time.sleep(2)

        # rows = 1+ len(driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[3]/div/div/div[2]/table/tbody/tr"))
        # cols = 1+ len(driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[3]/div/div/div[2]/table/tbody/tr[1]/td"))
        # print(rows)
        # print(cols)




    # body > div:nth-child(21) > div.container > div.row > div > div > div.ibox-content > table > tbody > tr:nth-child("+str(i)+") > td:nth-child(2) > a
        for i in range(1, 101):
            # for j in range(2, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                
            WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"body > div:nth-child(21) > div.container > div.row > div > div > div.ibox-content > table > tbody > tr:nth-child("+str(i)+") > td:nth-child(2) > a"))).click()
            # WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[9]/div[1]/div[3]/div/div/div[2]/table/tbody/tr["+str(i)+"]/td[2]"))).click()

            time.sleep(4)

    # <<<---------Execution using beautiful soup.................---->>>
            # soup = BeautifulSoup(driver.page_source, 'lxml')
            # tables = soup.find_all('div', id="ngo_info_modal")
            # # tables = soup.find_all('table')
            # dfs = pd.read_html(str(tables))
            # outputdata = pd.DataFrame(dfs)
            # print(outputdata)
            # outputdata.to_excel('ngo1.xlsx')
            
            #Create an empty list to store the data      
            lst = []  
            
            # Fetch, scrape, and append data to the list
            name = driver.find_element("id","ngo_name_title").text
            lst.append(name)
            uniqueID = driver.find_element("id","UniqueID").text
            lst.append(uniqueID)
            registration = driver.find_element("id","ngo_reg_date").text
            lst.append(registration)
            FCRA_reg_no = driver.find_element("id","FCRA_reg_no").text
            lst.append(FCRA_reg_no)
            ngoType = driver.find_element("id","ngo_type").text
            lst.append(ngoType)
            keyIssues = driver.find_element("id","key_issues").text
            lst.append(keyIssues)
            operationalArea = driver.find_element("id","operational_district").text
            lst.append(operationalArea)
            address = driver.find_element("id","address").text
            lst.append(address)
            city = driver.find_element("id","city").text
            lst.append(city)
            state = driver.find_element("id","state_p_ngo").text
            lst.append(state)
            telephone = driver.find_element("id","phone_n").text
            lst.append(telephone)
            email = driver.find_element("id","email_n").text
            lst.append(email)
            mobile = driver.find_element("id","mobile_n").text
            lst.append(mobile)
            website = driver.find_element("id","ngo_web_url").text
            lst.append(website)
            member1 = driver.find_element(By.XPATH, "/html/body/div[9]/div[3]/div[2]/div/div[2]/div/div/table[3]/tbody/tr[2]/td[1]").text
            lst.append(member1)
            designtation1 = driver.find_element(By.XPATH, "/html/body/div[9]/div[3]/div[2]/div/div[2]/div/div/table[3]/tbody/tr[2]/td[2]").text
            lst.append(designtation1)
            
            try:
                driver.find_element(By.XPATH, "/html/body/div[9]/div[3]/div[2]/div/div[2]/div/div/table[3]/tbody/tr[3]/td[1]").text
            except NoSuchElementException:
                member2="Not Available"
            else:
                member2=driver.find_element(By.XPATH, "/html/body/div[9]/div[3]/div[2]/div/div[2]/div/div/table[3]/tbody/tr[3]/td[1]").text
            lst.append(member2)


            try:
                driver.find_element(By.XPATH, "/html/body/div[9]/div[3]/div[2]/div/div[2]/div/div/table[3]/tbody/tr[3]/td[2]").text
            except NoSuchElementException:
                designtation2="NA"
            else:
                designtation2 = driver.find_element(By.XPATH, "/html/body/div[9]/div[3]/div[2]/div/div[2]/div/div/table[3]/tbody/tr[3]/td[2]").text
            lst.append(designtation2)
            
            
            #Print the list of all the data
            
            df.loc[len(df)] = lst
            print(df)

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#ngo_info_modal > div.modal-dialog.modal-lg > div > div.modal-header > button > span"))).click()

                
            
            ## Output as excel file
            df.to_excel("output1.xlsx")
        
except:
    missing.extend([page, i])
    pass

print("Missing elements are ", missing)
            

        # driver.close()
# except Exception as e:
#     print(e)
#     time.sleep(2)
#     driver.close()

##def back():
##        back = WebDriverWait(driver,20).until(
##        EC.element_to_be_clickable(
##            (By.XPATH, '/html/body/div[2]/main/div/div/div[2]/div/div[1]/div[2]/input'))
##    ).click()

##try:
    
##    folder1 = WebDriverWait(driver, 10).until(
##        EC.element_to_be_clickable(
##            (By.XPATH, '/html/body/div[2]/main/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[1]/img'))
##    ).click()
##
##    folder2 = WebDriverWait(driver, 10).until(
##        EC.element_to_be_clickable(
##            (By.XPATH, '/html/body/div[2]/main/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[1]/img'))
##    ).click()
      
    
##  
##    time.sleep(5)
##    driver.close()

##except:
##    time.sleep(5)  
##    driver.close()

