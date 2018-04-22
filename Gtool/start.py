import selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

print("Versie 1.0 : Auteur stephanboscu.nl : © 2018 ")

# Input gebruiker 
beheerder = input('Gebruikersnaam : ')
Wachtwoord = input('Wachtwoord : ')
OU = input ('OU ID : ')
                   
chromedriver = '.\driver\chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
driver.get('https://admin.google.com/Dashboard')


driver.find_element_by_css_selector("#identifierId").send_keys(beheerder)
button_email_next = driver.find_element_by_css_selector("#identifierNext")
button_email_next.click()
time.sleep(1)

driver.find_element_by_name('password').send_keys(wachtwoord)
button_wachtwoord_next = driver.find_element_by_css_selector("#passwordNext")
button_wachtwoord_next.click()
time.sleep(15)

# Admin console navigeer naar Crome-OS setting pagina
# driver.find_element_by_css_selector("#gb").click()
# driver.find_element_by_class_name('gb_yc').click()
# driver.find_element_by_class_name('gb_yc').click()

# Ga naar gebruikersinstellingen 
driver.get('https://admin.google.com/AdminHome?fral=1#ServiceSettings/notab=1&service=chrome+os&subtab=usersettings')
time.sleep(10)

#selecteer de OU /sub OU
ou_dropdown = driver.find_element_by_class_name('orgTree')

                                           
print(ou_dropdown)
time.sleep(5)
