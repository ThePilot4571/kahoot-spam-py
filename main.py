from selenium import webdriver
from selenium.webdriver.common.by import By

# enter desired values below
code = 1872639 # Kahoot game code
bots = 3 # Bot count

# main

stg = [0, 0]  # [index, total spaces after]

z = "@"  # "‌"


def space(name): # Creating ZWNJ for putting the same username multiple times. Needs improvement
    global stg
    global z
    if stg[0] > len(name):
        z = ";"  # "‍"
        stg[0] = 0
    if stg[1] <= (15 - len(name)):
        pos = stg[0]
        stg[1] += 1
        return name[:pos] + (z * (stg[1] - 1)) + name[pos:]
    else:
        stg[1] = 0
        stg[0] += 1


def spam():
    driver = webdriver.Chrome() # Selenium setup
    basename = input("Username for bots: ")
    for i in range(bots): 
        driver.get(f"https://kahoot.it/?pin={code}") # Use join link to make bot run faster than it would by typing the code in
        while True:
            try:
                nicknameInput = driver.find_element(By.ID, "nickname") # Refers to the input field for the username
                nicknameInput.send_keys(space(basename))
                driver.find_element("xpath", '//button[normalize-space()="OK, go!"]').click() # Refers to the enter button
                break
            except:
                pass
        driver.switch_to.new_window('tab') # New tab

    driver.quit() # REMOVE THIS LINE IF YOU WANT THE BOTS TO STAY IN AFTE JOINING. They will leave after about 20 seconds after the for loop terminates (Bots take a while to leave after the browser is closed.)

spam()
