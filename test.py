from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os.path
import time

#relative Path
dirname = os.path.dirname(os.path.abspath(__file__)) # python.py Directory
downloadpath=os.path.join(dirname,'Downloads')# Directory/Downloads
#Variables
mailAdress="howtogetafreeiptvl.istforlife@gmail.com"
mailPasswoard="test@test12345"
numberphone="00212620022324"



#setting the path of download file
options = webdriver.ChromeOptions()

#chrome on heroku
chrome_options.binary_location = GOOGLE_CHROME_BIN
options.add_experimental_option("prefs", {
  "download.default_directory": downloadpath,
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})
#headless mode
options.add_argument('--headless')
options.add_argument('--no-sandbox')

#declare a driver(browser)
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,options=options)

#for downlod en headless mode ( problem of replacing old downloads with the same name in the file)
driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': downloadpath}}
command_result = driver.execute("send_command", params)


#login link
driver.get("https://www.buy-iptv.shop/clientarea.php?action=services")

Email = driver.find_element_by_id("inputEmail")
Email.send_keys(mailAdress)

print("Email input")

Password = driver.find_element_by_id("inputPassword")
Password.send_keys(mailPasswoard)

print("password input")

loginbtn = driver.find_element_by_id("login")
loginbtn.click()

print("login button clicked")

Serviceslistbtn= driver.find_element_by_class_name("sorting_1")
Serviceslistbtn.click()

print("Serviceslistbtn clicked")

Servicebtn2= driver.find_element_by_css_selector("#tabOverview > div.tab-content.margin-bottom > div.row.new_custom1 > div:nth-child(2) > form > button")
Servicebtn2.click()

print("Servicebtn clicked")


m3ubtn= driver.find_element_by_id("m3u_output")
m3ubtn.click()

print("M3u button clicked")
print(" end script ")
time.sleep(5)

#driver.quit()
print("if all is well check : ./downloads for m3u file")


