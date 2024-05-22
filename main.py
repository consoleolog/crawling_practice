from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup
출발도시="ICN"
도착도시="TAK"
출발날짜="20240914"
도착날짜="20240918"


travelUrl = "https://flight.naver.com/flights/international/"+출발도시+"-"+도착도시+ "-"+출발날짜+"/"+도착도시+ "-" +출발도시+ "-"+도착날짜+"?adult=1&fareType=Y"
driver = webdriver.Chrome()
driver.get(travelUrl)

#  .airline_text__WWkbY #출발항공사명 
#  .route_time__xWu7a #출발비행기 출발시간 
#  .route_time__xWu7a #출발비행기 도착시간 

#  .airline_name__0Tw5w #도착항공사명 
#  .route_time__xWu7a #도착비행기 출발시간 
#  .route_time__xWu7a #도착비행기 도착시간 

# driver.implicitly_wait(30)
time.sleep(20)
#price = driver.find_elements(By.CSS_SELECTOR, ".item_num__3R0Vz")[0].text

#print(price)

#file = open('test.csv','a')
#file.write(항공사,출발도시,도착도시,출발날짜,도착날짜,출발시간,도착날짜,총금액)

# concurrent_ConcurrentList__pF_Kv 리스트

travel_list = driver.find_elements(By.CSS_SELECTOR, ".concurrent_ConcurrentItemContainer__NDJda concurrent_with_labels__MWI")
# travel_list = driver.find_elements(By.CSS_SELECTOR, ".concurrent_ConcurrentItemContainer__NDJda.concurrent_with_labels__MWI")
list_num = len(travel_list)

#RoundDiffAL concurrent_item__wwwxh 분기점 0번째가 출발이고 1번째가 도착임

# for i , data in enumerate(travel_list):
    # print(i)
    # 출발항공사명 = driver.find_elements(By.CSS_SELECTOR, ".airline_text__WWkbY")[int(2*i-1)].text
    # 도착항공사명 = driver.find_elements(By.CSS_SELECTOR, ".airline_name__0Tw5w")[int(2*i)].text
    # 출발비행기출발시간 = driver.find_elements(By.CSS_SELECTOR, ".route_time__xWu7a")[int(4*i-4)].text
    # 출발비행기도착시간 = driver.find_elements(By.CSS_SELECTOR, ".route_time__xWu7a")[int(4*i-3)].text
    # 도착비행기출발시간  = driver.find_elements(By.CSS_SELECTOR, ".route_time__xWu7a")[int(4*i-2)].text
    # 도착비행기도착시간  = driver.find_elements(By.CSS_SELECTOR, ".route_time__xWu7a")[int(4*i-1)].text
    # 금액  = driver.find_elements(By.CSS_SELECTOR, ".item_num__aKbk4")[i].text
    # file = open("travel_data.csv",'a')
    # file.write(f"\n{출발도시},{도착도시},{출발날짜},{도착날짜},{출발항공사명},{도착항공사명},{출발비행기출발시간},{출발비행기도착시간},{도착비행기출발시간},{도착비행기도착시간},{금액}\n")
    # file.close()    
print(list_num)
#concurrent_ConcurrentItemContainer__NDJda concurrent_with_labels__MWI

#이게 몇개있는지 어떻게 암 



