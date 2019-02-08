from accounts import *
from MainFunctions import *

def LoginNeoBux(driver, neobux_login, neobux_pass, Captcha=False):
    login = CheckExistsByXpath(driver, "//span[starts-with(.,'Login')]")
    SimpleClick(driver, login)

    WaitToLoadXpath(driver, "//input[@placeholder='Username']")
    usernameTab = CheckExistsByXpath(driver, "//input[@placeholder='Username']")
    usernameTab.send_keys(neobux_login)

    passwordTab = CheckExistsByXpath(driver, "//input[@placeholder='Password']")
    passwordTab.send_keys(neobux_pass)

    passwordTab2 = CheckExistsByXpath(driver, "//input[@placeholder='Secondary Password']")
    passwordTab2.send_keys(neobux_pass)

    ABCDE = WaitToLoadXpath(driver, "//input[@placeholder='ABCDE']",2)
    if ABCDE:
        input("Press Enter to continue...")

    Send = CheckExistsByXpath(driver, "//span[starts-with(.,'send')]")
    SimpleClick(driver, Send)


driver = StartBrowser(1)
driver.get("https://www.neobux.com/?r=pythonlessons")

LoginNeoBux(driver, neobux_login, neobux_pass, Captcha=False)
