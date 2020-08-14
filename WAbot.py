from selenium import webdriver
import time
import random


comps = ['nice', 'cool', 'amusing', 'pleasant', 'cheerful', 'friendly', 'marvellous', 'attractive', 'lovely', 'charming', 'benevolent']
compsvalue = random.choice(comps)
print(compsvalue)


driver = webdriver.Opera(executable_path = "C:\Drivers\operadriver.exe")
driver.get('https://web.whatsapp.com/')
driver.minimize_window()


name = input('Enter the name of user or group : ')
testmsg = input("Test msg: ")
count = int(input('Enter the count : '))
input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
user.click()


msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")

j =1 
while j < 2:
    msg_box.send_keys(testmsg)
    button = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button")
    button.click()
    j += 1

time.sleep(10)

for i in range(count):
    compsvalue = random.choice(comps)
    print(compsvalue)
    msg_box.send_keys("You are ", compsvalue)
    button = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button")
    button.click()

time.sleep(10)
driver.quit()
