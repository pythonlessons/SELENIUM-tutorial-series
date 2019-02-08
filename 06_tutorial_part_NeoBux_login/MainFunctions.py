from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchFrameException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import MoveTargetOutOfBoundsException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import JavascriptException
import random

def CheckExistsById(driver, CheckId):
    try:
        DriverId = driver.find_element_by_id(CheckId)
    except NoSuchWindowException:
        return False
    return DriverId

def CheckExistsByName(driver, CheckName):
    try:
        DriverName = driver.find_element_by_name(CheckName)
    except NoSuchWindowException:
        return False
    return DriverName

def CheckExistsByXpath(driver, xpath):
    try:
        path = driver.find_element_by_xpath(xpath)
    except NoSuchWindowException:
        return False
    except WebDriverException:
        return False
    except StaleElementReferenceException:
        return False
    return path

def CheckExistsArrayByXpath(driver, xpath):
    try:
        path = driver.find_elements_by_xpath(xpath)
    except NoSuchWindowException:
        return False
    except WebDriverException:
        return False
    except StaleElementReferenceException:
        return False
    return path

def MinimizeWindow(driver):
    try:
        driver.minimize_window()
    except UnexpectedAlertPresentException:
        return False
    return True

def DriverClose(driver):
    try:
        driver.close()
    except NoSuchWindowException:
        print("NoSuchWindowException in driver.close()")
        return False
    return True

def SimpleClick(driver, ObjectToClick):
    try:
        ObjectToClick.click()
    except ElementNotInteractableException:
        return False
    except ElementClickInterceptedException:
        return False
    except TypeError:
        return False
    return True

def StartBrowser(browser=1, browser_location='', driver_path=''):
    if browser == 1:
        driver = webdriver.Firefox()
    if browser == 2:
        driver = webdriver.Chrome()        
    if browser == 3:
        options = webdriver.ChromeOptions()
        options.binary_location = browser_location
        driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
    #driver.implicitly_wait(30)
    #driver.set_window_size(1920,1080)
    #driver.maximize_window()
    return driver

def NewTab(driver, Link, default_page=0, custom=0):
    window_count = len(driver.window_handles)
    driver.execute_script('''window.open("'''+Link+'''","_blank");''')
    while len(driver.window_handles) != window_count+1:
        time.sleep(0.5)
    if custom == 0:
        driver.switch_to.window(driver.window_handles[-1])
    if custom != 0:
        driver.switch_to.window(driver.window_handles[custom])    
    time.sleep(2)
    if driver.current_url == Link:
        current_window = driver.current_window_handle
        return current_window
    if driver.current_url == "about:blank":
        time.sleep(2)
        DriverClose()
        driver.switch_to.window(driver.window_handles[default_page])
        print("current window was about:blank we closed it, trying again in 10s")
        time.sleep(10)
        NewTab(driver, Link, default_page, custom)
    if driver.current_url != Link:
        pass

def VirtualClick(driver, click_object, UseRandom=True):
    try:
        size = click_object.size
    except StaleElementReferenceException:
        print("StaleElementReferenceException")
        return False
    sizeList = list(size.values())
    height = int(sizeList[0])-1
    width = int(sizeList[1])-1
    if UseRandom == True:
        try:
            height_rand = random.randint(1,height)
        except ValueError:
            height_rand = 1
        try:
            width_rand = random.randint(1,width)
        except ValueError:
            width_rand = 1
    if UseRandom == False:
        height_rand = height
        width_rand = width
    action = webdriver.common.action_chains.ActionChains(driver)
    try:
        action.move_to_element_with_offset(click_object, width_rand, height_rand)
    except StaleElementReferenceException:
        return False
    action.click()
    try:
        action.perform()
    except MoveTargetOutOfBoundsException:
        print("MoveTargetOutOfBoundsException with action.perform()")
        return False
    except StaleElementReferenceException:
        print("StaleElementReferenceException with action.perform()")
        return False
    return True

def WaitToLoadXpath(driver, xpath, retries = 5, Quotation = False):
    DriverName = CheckExistsByXpath(driver,xpath)
    WhileRetries = 0
    if Quotation == False:
        while DriverName == False and WhileRetries < retries*2:
            DriverName = CheckExistsByXpath(driver,xpath)
            time.sleep(0.5)
            WhileRetries += 1
            #print("WhileRetries:", WhileRetries)
            #print("DriverName:", DriverName)
            if WhileRetries == retries*2:
                return False
    if Quotation == True:
        while DriverName == False and WhileRetries < retries*2:
            DriverName = CheckExistsByXpath(driver,xpath)
            time.sleep(0.5)
            WhileRetries += 1
            print("WhileRetries:", WhileRetries)
            print("DriverName:", DriverName)
            if WhileRetries == retries*2:
                return False
        if DriverName != False:
            try:
                DriverName_text = DriverName.text
            except StaleElementReferenceException:
                DriverName_text = ''
            except NoSuchWindowException:
                return False
            while DriverName_text == '' and WhileRetries < retries*2:
                DriverName = CheckExistsByXpath(driver,xpath)
                try:
                    DriverName_text = DriverName.text
                except StaleElementReferenceException:
                    DriverName_text = ''
                except AttributeError:
                    DriverName_text = ''
                print("DriverName_text == '':", DriverName_text)
                time.sleep(0.5)
                WhileRetries += 1
                if WhileRetries == retries*2:
                    return False
    return True

def DriverRefresh(driver, Link):
    try:
        driver.refresh()
    except WebDriverException:
        return False
    return True
