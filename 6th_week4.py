# Q4. 여러분은 어떤 상품을 판매하고 있습니다. 매월 상품을 많이 구매해준 VIP회원에게 할인 쿠폰을 제공해주려고 합니다. 아래와 같은 회원 정보가 있을 때 회원 정보를 출력하고 할인 쿠폰을 받을 회원이 누구인지 출력하는 함수를 만들어 주세요.

# 😲조건1 - 8회 이상 구매한 회원이 VIP대상
# 😲조건2 - 전화번호가 없으면 쿠폰을 받을 수 없음
# 😲조건3 - 전화번호가 없으면 000-0000-0000으로 출력할 것

# # 6명의 회원이고 "아이디,나이,전화번호,성별,지역,구매횟수" 순서로 입력되어 있음
# info = "abc,21세,010-1234-5678,남자,서울,5,cdb,25세,x,남자,서울,4,bbc,30세,010-2222-3333,여자,서울,3,ccb,29세,x,여자,경기,9,dab,26세,x,남자,인천,8,aab,23세,010-3333-1111,여자,경기,10"
# ✅출력 예시
# good_customer(info)
# {'아이디': ['abc', 'cdb', 'bbc', 'ccb', 'dab', 'aab'], '나이': ['21세', '25세', '30세', '29세', '26세', '23세'], '전화번호': ['010-1234-5678', '000-0000-0000', '010-2222-3333', '000-0000-0000', '000-0000-0000', '010-3333-1111'], '성별': ['남자', '남자', '여자', '여자', '남자', '여자'], '지역': ['서울', '서울', '서울', '경기', '인천', '경기'], '구매횟수': [5, 4, 3, 9, 8, 10]}
# 할인 쿠폰을 받을 회원정보 아이디:aab, 나이:23세, 전화번호:010-3333-1111, 성별:여자, 지역:경기, 구매횟수: 10

import re

info = "abc,21세,010-1234-5678,남자,서울,5,cdb,25세,x,남자,서울,4,bbc,30세,010-2222-3333,여자,서울,3,ccb,29세,x,여자,경기,9,dab,26세,x,남자,인천,8,aab,23세,010-3333-1111,여자,경기,10"

inform = info.split(",")
id_list, age, phone, sex, location, num = [],[],[],[],[],[]

for i in range(len(inform)):
    if i % 6 == 0:
        id_list.append(inform[i])
    elif i % 6 == 1:
        age.append(inform[i])
    elif i % 6 == 2:
        if inform[i] == "x":
            phone.append("000-0000-0000")
        else:
            phone.append(inform[i])
    elif i % 6 == 3:
        sex.append(inform[i])
    elif i % 6 == 4:
        location.append(inform[i])
    elif i % 6 == 5:
        num.append(int(inform[i]))
cnt = 0
for n in num:
    if n >= 8 and phone[cnt] is not "000-0000-0000":
        print(f"할인 쿠폰을 받을 회원정보 -> 아이디 : {id_list[cnt]}, 나이 : {age[cnt]}, 전화번호 : {phone[cnt]}, 성별 : {sex[cnt]}, 지역 : {location[cnt]}, 구매횟수 : {num[cnt]}")
    cnt += 1