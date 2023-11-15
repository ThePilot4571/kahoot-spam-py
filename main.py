from selenium import webdriver
from selenium.webdriver.common.by import By

# enter desired values below
code = 1872639
bots = 3

# main

stg = [0, 0]  # [index, total spaces after]

z = "@"  # "‌"


def space(name):
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
    driver = webdriver.Chrome()
    basename = input("Root name: ")
    for i in range(bots):
        driver.get(f"https://kahoot.it/?pin={code}")
        while True:
            try:
                nicknameInput = driver.find_element(By.ID, "nickname")
                nicknameInput.send_keys(space(basename))
                driver.find_element("xpath", '//button[normalize-space()="OK, go!"]').click()
                break
            except:
                pass
        driver.switch_to.new_window('tab')

    driver.quit()


for x in range(150):
    print(space("test"))
