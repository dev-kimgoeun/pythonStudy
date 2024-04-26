import time
from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=opt)
browser.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")
time.sleep(1)

#로그인하기
id = browser.find_element(By.CSS_SELECTOR, "input#id")
id.send_keys("아이디")
pw = browser.find_element(By.CSS_SELECTOR, "input#pw")
pw.send_keys("비밀번호")
browser.find_element(By.CSS_SELECTOR, "button.btn_login").click()
time.sleep(2)