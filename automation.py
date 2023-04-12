# # from selenium import webdriver
# # chrome_browser = webdriver.Chrome('./chromedriver')
# # print(chrome_browser)

# from selenium import webdriver

# from selenium.webdriver.chrome.service import Service



# service = Service(executable_path='./chromedriver')

# chrome_browser = webdriver.Chrome(service=service)



# # chrome_browser.get("http://www.google.com")

# chrome_browser.maximize_window()



# while True:

#     pass


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
 
# service = Service(executable_path='./chromedriver')
 
# chrome_browser = webdriver.Chrome(service=service)

# chrome_browser.maximize_window()
# chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

# button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')
# print(button)


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
 
chrome_browser = webdriver.Chrome()
chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
 
# This solves the issue with the Popup for those that encounter it:
chrome_browser.implicitly_wait(2)
popup =chrome_browser.find_element(By.ID, 'at-cv-lightbox-close')
popup.click()
 
 
 
user_message = chrome_browser.find_element(By.ID, 'user-message')
user_message.clear()
user_message.send_keys('I AM EXTRA COOOOL')
 
time.sleep(2)
show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')
show_message_button.click()
 
output_message = chrome_browser.find_element(By.ID, 'display')
assert 'I AM EXTRA COOOOL' in output_message.text

print("Hello World. This is Esmeralda")