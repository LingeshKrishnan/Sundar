from slelenium import webdriver

driver = webdriver.Chrome()
driver.implicity.wait(30)
driver.maximize.window()

driver.get("url")

obj = driver.findelement_by_(//id(//*anything))("locator")
obj.clear(//if txtfield)
obj.send_keys("searchkeys") *//if to enter into textfield

obj1 = driver.findelement_*****("locator")
obj1.click() *//if button or element  **to submit

driver.minimize.window()
