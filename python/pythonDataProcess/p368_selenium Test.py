import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# filename = 'C:/Users/BIT/Downloads/chromedriver_win32/chromedriver.exe'
# driver = webdriver.Chrome(filename)
driver = webdriver.Chrome()
print(type(driver))
print('-' * 50)

print('Go Google~!! ')
url = 'http://www.google.com'
driver.get(url)

search_textbox = driver.find_element(By.NAME, 'q')
##textbox 이름이 q다.

word = '리눅스마스터'
search_textbox.send_keys(word)

search_textbox.submit()

#네트워크 영향을 받고, 데이터를 받는게 오래걸릴수있으니까~
wait=3
print(str(wait)+'동안기다립니다.')
time.sleep(wait)

imagefile = 'xx_icecream.png'
driver.save_screenshot(imagefile)
print(imagefile + '이미지저장')

wait =3
driver.implicitly_wait(wait)

driver.quit()
print('Brower Exit~!!')

