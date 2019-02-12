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

    ABCDE = WaitToLoadXpath(driver, "//input[@placeholder='ABCDE']")
    if ABCDE:
        input("Press Enter to continue...")

    Send = CheckExistsByXpath(driver, "//span[starts-with(.,'send')]")
    SimpleClick(driver, Send)

def ViewAllAdds(driver):
    WaitToLoadXpath(driver, "//span[starts-with(.,'View Advertisaments')]")
    ViewAds = CheckExistsByXpath(driver, "//span[starts-with(.,'View Advertisements')]")
    SimpleClick(driver, ViewAds)

    for i in ["1","2","3"]:
        if WaitToLoadXpath(driver, "//div[@id='vCat_"+i+"']"):
            Adds = CheckExistsArrayByXpath(driver, "//div[@id='vCat_"+i+"']/div")
            if len(Adds) > 0:
                for array in range(len(Adds)):
                    array += 1
                    print("array: ",array)
                    Available = CheckExistsByXpath(driver, "//div[@id='vCat_"+i+"']/div["+str(array)+"]/div/div[3]/div[3]/i[@class='ic-ok-1']")
                    if Available == False:
                        print("Click this add")
                        CLICK = CheckExistsByXpath(driver, "//div[@id='vCat_"+i+"']/div["+str(array)+"]/div/div[1]/div[1]/a")
                        if CLICK == False:
                            continue
                        time.sleep(2)
                        VirtualClick(driver, CLICK)
                        time.sleep(2)
                        CLICK2 = CheckExistsByXpath(driver, "//div[@id='vCat_"+i+"']/div["+str(array)+"]/div/div[2]/span/a/img")
                        if CLICK2 == False:
                            continue
                        VirtualClick(driver, CLICK2)
                        time.sleep(1)
                        driver.switch_to.window(driver.window_handles[-1])
                        time.sleep(10)
                        if WaitToLoadXpath(driver, "//span[starts-with(.,'Close')]", 30, True):
                            time.sleep(1)
                            Close = CheckExistsByXpath(driver, "//span[starts-with(.,'Close')]")
                            time.sleep(1)
                            print("Close: ",Close.text)
                            VirtualClick(driver, Close)
                            driver.switch_to.window(driver.window_handles[-1])
                            time.sleep(1)

def ViewLotteryAds(driver):
    if WaitToLoadXpath(driver, "//div[@id='ap_hct']/a", 5, True):
        text = CheckExistsByXpath(driver, "//div[@id='ap_hct']/a")
        print(text.text)
        text.click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[-1])
        while True:
            if WaitToLoadXpath(driver, "//span[starts-with(.,'Next')]", 30, True):
                rmnDv = CheckExistsByXpath(driver, "//div[@id='rmnDv']")
                rmnDv_text = rmnDv.text
                print("rmnDv:",rmnDv_text)
                Next = CheckExistsByXpath(driver, "//span[starts-with(.,'Next')]")
                Next.click()
                if rmnDv_text == "1"or rmnDv_text == " 1":
                    time.sleep(15)
                    driver.close()
                    driver.switch_to.window(driver.window_handles[-1])
                    break
            else:
                print("nothing to do here anymore, bye bye")
                break
        # go HOME
        time.sleep(1)
        LOGO = CheckExistsByXpath(driver, "//div[@id='logoC']")
        LOGO.click()

driver = StartBrowser(1)
NewTab(driver, "https://www.neobux.com/")

LoginNeoBux(driver, neobux_login, neobux_pass, Captcha=False)
ViewAllAdds(driver)
ViewLotteryAds(driver)
