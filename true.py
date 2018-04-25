from selenium import webdriver
import time
import xlrd
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
yourEmail='Your Email Address'
yourPassword='Your Password'
driver = webdriver.Chrome()
driver.get('https://www.truecaller.com/')
doc = driver.page_source
input=driver.find_element_by_xpath('//*[@id="app"]/div[5]/div[1]/div/div[2]/div[1]/input')
input.send_keys("MOBILE_NUMBER_HERE")
input.send_keys(Keys.RETURN)
window_before = driver.window_handles[0]
#I have selected gmail address here.You can go for other option just copy its XPATH hwere
sign_in=driver.find_element_by_xpath('//*[@id="app"]/div[5]/div/div[1]/button').click()
gmail_button=driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/div[1]/div[1]').click()
window_after = driver.window_handles[1]
driver.switch_to_window(window_after)
time.sleep(3)
email=driver.find_element_by_xpath('//*[@id="identifierId"]')
email.send_keys(yourEmail)
next_button=driver.find_element_by_xpath('//*[@id="identifierNext"]/content').click()
time.sleep(5)
password=driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password.send_keys(yourPassword)
next_button1=driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span').click()
driver.switch_to_window(window_before)
time.sleep(5)
output = driver.find_element_by_xpath('//*[@id="app"]/div[5]/div/div[2]/div[2]/a[1]/div[2]').text
print(output)
driver.find_element_by_class_name('searchbar__query').clear()
#driver.delete_all_cookies()
time.sleep(3)
wb=xlrd.open_workbook(r'YOUR_FILE_PATH_HERE\numbers.xlsx')
sheetname=wb.sheet_names()
first_sheet= wb.sheet_by_index(0)
i=0
while(i<3):
    driver.find_element_by_class_name('searchbar__query').clear()
    cell = first_sheet.cell(i,0)
    time.sleep(10)
    driver.find_element_by_class_name('searchbar__query').send_keys(int(cell.value))
    driver.find_element_by_xpath('//*[@id="app"]/div[3]/div[2]/div/div[1]/button[2]').click()
    try:
    	driver.find_element_by_xpath('//*[@id="app"]/div[5]/div/div[2]/div[2]/a[1]/div[2]')
    except NoSuchElementException:
    	print('no email address provided')
    test1=driver.find_element_by_xpath('//*[@id="app"]/div[5]/div/div[2]/div[2]/a[1]/div[2]').text
    print(test1)
    i=i+1

