from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

webdriver_path = '/path/to/chromedriver'
driver = webdriver.Chrome(webdriver_path)

# 해당 사이트를 띄웁니다.
driver.get('https://admin.studymoa.me/login')

# 이후에 다른 작업을 수행합니다.

id_input = driver.find_element(By.XPATH, '//*[@id="loginID"]') # 아이디 입력
id_input.send_keys('laube0104')


# 비밀번호 입력
pw_input = driver.find_element(By.XPATH, '//*[@id="loginPW"]') # 패스워드 입력
pw_input.send_keys('10180610a##')

login_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div[2]/button/span[1]') #로그인 버튼 클릭
login_button.click()

# while True:
time.sleep(2)

target_element = driver.find_element(By.XPATH, '//*[@id="nav-container"]/li[4]') # room으로 이동
target_element.click()

time.sleep(4)

target_element2 = driver.find_element(By.XPATH, '//*[@id="body-wrapper"]/div[2]')
html1 = target_element.get_attribute('innerHTML')

target_element3 = driver.find_element(By.XPATH, '//*[@id="fullscreen_view"]/div/div')
html2 = driver.page_source # time table 당일것 html전체 크롤
# print(target_element2)
# print(html2)

wait = WebDriverWait(driver, 10)
elements_xpath = '//tr[@data-id="7"]'

target_elements = wait.until(EC.visibility_of_all_elements_located((By.XPATH, elements_xpath)))

text = target_element.text
# print(text)
# print(target_element4)
for element in target_elements:
    text = element.text
    print(text)


while True:
    time.sleep(10)  # 10초간 대기합니다.



