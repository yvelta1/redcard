from selenium import webdriver
import time
import ccard
import extccard

#user.txt 필요
user = open('user.txt', 'r', encoding='UTF8').read(); userdata = user.split(',')
u_id = userdata[0]
u_pw = userdata[1]
u_code = userdata[2]

#클래스카드 세트 정보 분석
webdriver_options = webdriver.ChromeOptions()
webdriver_options.add_argument('headless')
sett = webdriver.Chrome('chromedriver', options=webdriver_options)
sett.get(f'https://www.classcard.net/set/{u_code}')

#단어 개수와 세트 제목 출력
word = sett.find_element_by_xpath('/html/head/meta[9]').get_attribute('content'); word_num = word.split(); words = int(word_num[0])
title = sett.find_element_by_xpath('/html/head/title').get_attribute('textContent')
print(words); print(title) 

#마지막 세트 단어 개수 확인
f_word = words % 10

#로그인 시도
#마지막 세트 단어 개수에 따른 분기점 생성
if f_word == 1:
    print('마지막 세트의 단어가 11개입니다.')
    extccard.startex(u_id, u_pw, u_code, words, 11)
    #이후 과정은 extccard.py에서 진행
elif f_word == 2:
    print('마지막 세트의 단어가 12개입니다.')
    extccard.startex(u_id, u_pw, u_code, words, 12)
    #이후 과정은 extccard.py에서 진행
elif f_word == 3:
    print('마지막 세트의 단어가 13개입니다.')
    extccard.startex(u_id, u_pw, u_code, words, 13)
    #이후 과정은 extccard.py에서 진행
else:
    print('작업을 시작합니다.')
    ccard.start(u_id, u_pw, u_code, words)
    #이후 과정은 ccard.py에서 진행
