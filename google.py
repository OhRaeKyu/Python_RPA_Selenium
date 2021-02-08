from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl")

elem = driver.find_element_by_name("q") # 검색 창(name = "q") 찾기
elem.send_keys("사과") # 입력 값 전송
elem.send_keys(Keys.RETURN) # 엔터 키 전송

# 스크롤 높이 제어
SCROLL_PAUSE_TIME = 1

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 스크롤 내리기
  time.sleep(SCROLL_PAUSE_TIME) # 로딩 시간 대기
  new_height = driver.execute_script("return document.body.scrollHeight") # 스크롤이 끝까지 내려갔는지 확인하기 위한 변수
  if new_height == last_height:
    try:
      driver.find_element_by_css_selector(".mye4qd").click()
    except:
      break
  last_height = new_height

xpath = "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img"
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd") # css class를 통해 찾기
count = 1
for image in images:
  try:
    image.click()
    time.sleep(3)
    # imgUrl = driver.find_element_by_css_selector(".n3VNCb"),get_attribute("src")
    imgUrl = driver.find_element_by_xpath(xpath).get_attribute("src") # css class를 통해 찾고, 속성 값인 src 받아오기    
    urllib.request.urlretrieve(imgUrl, str(count) + ".jpg") # 해당 url로 요청 보내기 (다운로드 url로 요청)
    count += 1
  except :
    continue

driver.close()