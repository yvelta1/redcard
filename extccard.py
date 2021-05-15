from selenium import webdriver
import time
import sys

#a: 클래스카드 아이디, b: 클래스카드 비번, c: 클래스카드 URL 뒤에 붙는 숫자, d: 단어 개수, e: 마지막 세트의 단어 개수(단어 수의 일의자리가 1,2,3인경우 해당)
def startex(a,b,c,d,e):
    print('작업을 시작합니다.')
    #로그인 화면으로 이동
    driver = webdriver.Chrome('chromedriver')
    driver.implicitly_wait(10)
    driver.get('http://www.classcard.net/Login')

    #user.txt에서 가져온 아이디, 비밀번호 정보로 로그인 시도
    logme = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/form/div[1]/input[1]'); logme.send_keys(a)
    logme = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/form/div[1]/input[2]'); logme.send_keys(b)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/form/div[2]/button').click()
    #sleep으로 지연시키지 않으면 이후 과정들이 비로그인 상태로 진행됩니다.
    time.sleep(1)

    #리콜 시작
    driver.execute_script('window.open("{0}");'.format(f'https://www.classcard.net/Recall/{c}/1'))
    driver.switch_to.window(driver.window_handles[1])
    num = 0

    while num < (d - e):
        driver.implicitly_wait(3)
        #sleep을 하지 않으면 에러 발생
        time.sleep(2.5) #네트워크 환경이나 컴퓨터의 사양에 따라 달라질 수 있습니다. 적절한 숫자로 조절하세요.

        #정답과 각 카드의 글자 확인
        answer = driver.find_element_by_css_selector('#wrapper-learn > div > div > div.study-content.cc-table.middle > div.study-body.fade.in > div.CardItem.current.showing > div.card-bottom > div > div > div > div.text-normal > span').get_attribute('textContent')
        card1 = driver.find_element_by_css_selector('#wrapper-learn > div > div > div.study-content.cc-table.middle > div.study-body.fade.in > div.CardItem.current.showing > div.card-quest.card-quest-front > div:nth-child(1) > div.card-quest-list > div').get_attribute('textContent')
        card2 = driver.find_element_by_css_selector('#wrapper-learn > div > div > div.study-content.cc-table.middle > div.study-body.fade.in > div.CardItem.current.showing > div.card-quest.card-quest-front > div:nth-child(2) > div.card-quest-list > div').get_attribute('textContent')
        card3 = driver.find_element_by_css_selector('#wrapper-learn > div > div > div.study-content.cc-table.middle > div.study-body.fade.in > div.CardItem.current.showing > div.card-quest.card-quest-front > div:nth-child(3) > div.card-quest-list > div').get_attribute('textContent')

        #정답과 일치하는 카드 클릭
        if answer == card1: driver.find_element_by_css_selector('#wrapper-learn > div > div > div.study-content.cc-table.middle > div.study-body.fade.in > div.CardItem.current.showing > div.card-quest.card-quest-front > div:nth-child(1) > div.card-quest-list > div').click()
        if answer == card2: driver.find_element_by_css_selector('#wrapper-learn > div > div > div.study-content.cc-table.middle > div.study-body.fade.in > div.CardItem.current.showing > div.card-quest.card-quest-front > div:nth-child(2) > div.card-quest-list > div').click()
        if answer == card3: driver.find_element_by_css_selector('#wrapper-learn > div > div > div.study-content.cc-table.middle > div.study-body.fade.in > div.CardItem.current.showing > div.card-quest.card-quest-front > div:nth-child(3) > div.card-quest-list > div').click()
        num += 1

        #다음 세트로 가기
        if num % 10 == 0:
            driver.find_element_by_css_selector('#study_end > div > div.step.step2 > div.study-bottom > div.btn-text.m-l-sm > a').click()

    for i in range(e):
        time.sleep(1.9)

        #정답과 각 카드의 글자 확인
        answer = driver.find_element_by_css_selector('#wrapper-learn > div > div > div.study-content.cc-table.middle > div.study-body.fade.in > div.CardItem.current.showing > div.card-bottom > div > div > div > div.text-normal > span').get_attribute('textContent')
        card1 = driver.find_element_by_css_selector('#wrapper-learn > div > div > div.study-content.cc-table.middle > div.study-body.fade.in > div.CardItem.current.showing > div.card-quest.card-quest-front > div:nth-child(1) > div.card-quest-list > div').get_attribute('textContent')
        card2 = driver.find_element_by_css_selector('#wrapper-learn > div > div > div.study-content.cc-table.middle > div.study-body.fade.in > div.CardItem.current.showing > div.card-quest.card-quest-front > div:nth-child(2) > div.card-quest-list > div').get_attribute('textContent')
        card3 = driver.find_element_by_css_selector('#wrapper-learn > div > div > div.study-content.cc-table.middle > div.study-body.fade.in > div.CardItem.current.showing > div.card-quest.card-quest-front > div:nth-child(3) > div.card-quest-list > div').get_attribute('textContent')

        #정답과 일치하는 카드 클릭
        if answer == card1: driver.find_element_by_css_selector('#wrapper-learn > div > div > div.study-content.cc-table.middle > div.study-body.fade.in > div.CardItem.current.showing > div.card-quest.card-quest-front > div:nth-child(1) > div.card-quest-list > div').click()
        if answer == card2: driver.find_element_by_css_selector('#wrapper-learn > div > div > div.study-content.cc-table.middle > div.study-body.fade.in > div.CardItem.current.showing > div.card-quest.card-quest-front > div:nth-child(2) > div.card-quest-list > div').click()
        if answer == card3: driver.find_element_by_css_selector('#wrapper-learn > div > div > div.study-content.cc-table.middle > div.study-body.fade.in > div.CardItem.current.showing > div.card-quest.card-quest-front > div:nth-child(3) > div.card-quest-list > div').click()
    
    driver.find_element_by_css_selector('#study_end > div > div.step.step2 > div.study-bottom > div.btn-text.m-l-sm > a').click()

    #스펠 시작

    driver.execute_script('window.open("{0}");'.format(f'https://www.classcard.net/Spell/{c}/1'))
    driver.switch_to.window(driver.window_handles[2])
    num = 0

    while num < (d - e):
        time.sleep(1.9)
        #스펠 정답 찾기
        word = driver.find_element_by_css_selector('#wrapper-learn > div > div > div.study-content.cc-table.middle > div.study-body.fade.in > div.CardItem.current.showing > div.card-bottom > div > div > div > div.text-success.spell-answer.hidden > span.spell-content').get_attribute('textContent')

        #스펠 정답 입력
        ans = driver.find_element_by_css_selector('#wrapper-learn > div > div > div.study-content.cc-table.middle > div.study-body.fade.in > div.CardItem.current.showing > div.card-bottom > div > div > div > div.text-normal.spell-input > input')
        ans.send_keys(word)

        #버튼 클릭 후 다음 단어로
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/a').click()
        driver.find_element_by_css_selector('#wrapper-learn > div > div > div.study-bottom.down > div.btn-text.btn-next-box > a').click()
        num += 1

        if num % 10 == 0:
            driver.find_element_by_css_selector('#study_end > div > div.step.step2 > div.study-bottom > div.btn-text.m-l-sm > a').click()

    for i in range(e):
        time.sleep(1.9)
        #스펠 정답 찾기
        word = driver.find_element_by_css_selector('#wrapper-learn > div > div > div.study-content.cc-table.middle > div.study-body.fade.in > div.CardItem.current.showing > div.card-bottom > div > div > div > div.text-success.spell-answer.hidden > span.spell-content').get_attribute('textContent')

        #스펠 정답 입력
        ans = driver.find_element_by_css_selector('#wrapper-learn > div > div > div.study-content.cc-table.middle > div.study-body.fade.in > div.CardItem.current.showing > div.card-bottom > div > div > div > div.text-normal.spell-input > input')
        ans.send_keys(word)

        #버튼 클릭 후 다음 단어로
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/a').click()
        driver.find_element_by_css_selector('#wrapper-learn > div > div > div.study-bottom.down > div.btn-text.btn-next-box > a').click()
    
    driver.find_element_by_css_selector('#study_end > div > div.step.step2 > div.study-bottom > div.btn-text.m-l-sm > a').click()

    #암기 실행하기

    driver.execute_script('window.open("{0}");'.format(f'http://www.classcard.net/Memorize/{c}/1'))
    driver.switch_to.window(driver.window_handles[3])

    num = 0

    while num < (d - e):
        #암기 버튼 입력
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div[1]/a").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div[2]/a").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[4]/a").click()
        num += 1
        if num % 10 == 0:
            driver.find_element_by_css_selector('#study_end > div > div.step.step2 > div.study-bottom > div.btn-text.m-l-sm > a').click()
    
    for i in range(e):
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div[1]/a").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div[2]/a").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[4]/a").click()

    driver.find_element_by_css_selector('#study_end > div > div.step.step2 > div.study-bottom > div.btn-text.m-l-sm > a').click()      

    print('완료되었습니다. 2초 후에 종료합니다.')
    time.sleep(2); driver.close(); sys.exit()


        
    

    
