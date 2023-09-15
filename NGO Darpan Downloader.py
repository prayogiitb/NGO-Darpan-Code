#----------- Created by --------------#
##------- Shivanand Nalgire ---------##

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from IPython.display import display
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

# CREATE SERVICE OBJECT FOR GIVING PATH TO CHROMEDRIVER
from selenium.webdriver.chrome.service import Service



import pandas as pd
import time


options=Options()
options.headless=True
serv_obj = Service("D:\Sakshi\ChromeDriver\chromedriver-win32\chromedriver-win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# Make driver implicitly wait for 10 seconds
driver.implicitly_wait(10)
options = webdriver.ChromeOptions()


prefs = {"download.default_directory" : "D:/Sakshi/Data_Work/Scrapping"}
# driver = webdriver.Chrome()
# driver.maximize_window()



df = pd.DataFrame(columns = ['Name', 'UniqueID','RegDate', 'FCRA No', 'NGO Type','Key Issues','Operational Area','Address','City','State','Telephone','Email','Mobile','Website','Member 1','Designation 1','Member 2','Designation 2'])
missing = []

p = 24 #page number
s = 1  #NGO Number in the page


for page in range(3,4):
    page_url = "https://ngodarpan.gov.in/index.php/home/statewise_ngo/4526/32/"+str(page)+"?per_page=100"
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

        try:
            driver.find_element("id","ngo_name_title").text
        except:
            name = "NA"
        else:
            name = driver.find_element("id","ngo_name_title").text
        lst.append(name)

        try:
            driver.find_element("id","UniqueID").text
        except:
            uniqueID = "NA"
        else:    
            uniqueID = driver.find_element("id","UniqueID").text
        lst.append(uniqueID)

        try:
            driver.find_element("id","ngo_reg_date").text
        except:
            registration = "NA"
        else:
            registration = driver.find_element("id","ngo_reg_date").text
        lst.append(registration)

        try:
            driver.find_element("id","FCRA_reg_no").text
        except:
            FCRA_reg_no = "NA"
        else:
            FCRA_reg_no = driver.find_element("id","FCRA_reg_no").text
        lst.append(FCRA_reg_no)

        try:
            driver.find_element("id","ngo_type").text
        except:
            ngoType = "NA"
        else:
            ngoType = driver.find_element("id","ngo_type").text
        lst.append(ngoType)

        try:
            driver.find_element("id","key_issues").text
        except:
            keyIssues = "NA"
        else:
            keyIssues = driver.find_element("id","key_issues").text
        lst.append(keyIssues)

        try:
            driver.find_element("id","operational_district").text
        except:
            operationalArea = "NA"
        else:
            operationalArea = driver.find_element("id","operational_district").text
        lst.append(operationalArea)

        try:
            driver.find_element("id","address").text
        except:
            address="NA"
        else:
            address = driver.find_element("id","address").text
        lst.append(address)

        try:
            driver.find_element("id","city").text
        except:
            city = "NA"
        else:
            city = driver.find_element("id","city").text
        lst.append(city)

        try:
            driver.find_element("id","state_p_ngo").text
        except:
            state = "NA"
        else:
            state = driver.find_element("id","state_p_ngo").text
        lst.append(state)

        try:
            driver.find_element("id","phone_n").text
        except:
            telephone = "NA"
        else:
            telephone = driver.find_element("id","phone_n").text
        lst.append(telephone)

        try:
            driver.find_element("id","email_n").text
        except:
            email = "NA"
        else:
            email = driver.find_element("id","email_n").text
        lst.append(email)

        try:
            driver.find_element("id","mobile_n").text
        except:
            mobile = "NA"
        else:
            mobile = driver.find_element("id","mobile_n").text
        lst.append(mobile)

        try:
            driver.find_element("id","ngo_web_url").text
        except:
            website = "NA"
        else:
            website = driver.find_element("id","ngo_web_url").text
        lst.append(website)

        try:
            driver.find_element(By.XPATH, "/html/body/div[9]/div[3]/div[2]/div/div[2]/div/div/table[3]/tbody/tr[2]/td[1]").text
        except:
            member1 = "NA"
        else:
            member1 = driver.find_element(By.XPATH, "/html/body/div[9]/div[3]/div[2]/div/div[2]/div/div/table[3]/tbody/tr[2]/td[1]").text
        lst.append(member1)

        try:
            driver.find_element(By.XPATH, "/html/body/div[9]/div[3]/div[2]/div/div[2]/div/div/table[3]/tbody/tr[2]/td[2]").text
        except:
            designtation1 = "NA"
        else:
            designtation1 = driver.find_element(By.XPATH, "/html/body/div[9]/div[3]/div[2]/div/div[2]/div/div/table[3]/tbody/tr[2]/td[2]").text
        lst.append(designtation1)
        
        try:
            driver.find_element(By.XPATH, "/html/body/div[9]/div[3]/div[2]/div/div[2]/div/div/table[3]/tbody/tr[3]/td[1]").text
        except NoSuchElementException:
            member2="NA"
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
        s = df.index # Get the index number of the dataset downloaded
        

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#ngo_info_modal > div.modal-dialog.modal-lg > div > div.modal-header > button > span"))).click()

            
        ## Output as excel file
        df.to_excel("Output1.xlsx")


driver.quit()





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
