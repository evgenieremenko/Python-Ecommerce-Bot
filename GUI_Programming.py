# from tkinter import *
#
# top = Tk()
# # Code to add widgets will go here...
# label = Label(top,text="Add New Account")
# label.pack()
# top.mainloop()
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.bestbuy.com")
driver.find_element_by_link_text("United States").click()
time.sleep(4)
driver.find_element_by_xpath("//html").click()
time.sleep(4)
driver.find_element_by_xpath("//*[@id='header-block']/div[2]/div[2]/div/nav[2]/ul/li[1]/button/div[2]/span").click()
time.sleep(4)
driver.find_element_by_link_text("Sign In").click()
time.sleep(4)
driver.find_element_by_xpath("//*[@id='fld-e']").send_keys("aarthifnawaz@gmail.com")
driver.find_element_by_xpath("//*[@id='fld-p1']").send_keys("Virtusatechp0010$")
driver.find_element_by_xpath("/html/body/div[1]/div/section/main/div[1]/div/div/div/div/form/div[3]/button").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='gh-search-input']").send_keys("paper") # Since action man was out of stock should buy from paper
driver.find_element_by_xpath("//*[@id='header-block']/div[2]/div[1]/div/div[2]/div/div[1]/div/div/form/button[2]").click()
wait = WebDriverWait(driver, 10)
time.sleep(12)
driver.find_element_by_css_selector("#fulfillment-add-to-cart-button-22f94f40-3b6c-4b57-bf6a-4eb6fbaf3170 > div > div > button").click()
wait = WebDriverWait(driver, 10)
time.sleep(12)
driver.find_element_by_link_text("Go to Cart").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='cartApp']/div[2]/div[1]/div/div/span/div/div[1]/div[1]/section[2]/div/div/div[3]/div/div[2]/button").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='email']").send_keys("a@gmail.com")
driver.find_element_by_xpath("//*[@id='btnNext']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='password']").send_keys("mass")
driver.find_element_by_xpath("//*[@id='btnLogin']").click()
