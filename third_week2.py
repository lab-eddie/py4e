# 📌Q2. 가위바위보 업그레이드 버젼을 함수로 만들어 봅시다. 아래와 같은 조건을 만족해 주세요.

# 조건 1: 게임을 몇 판을 진행할 것인지 입력을 받아주기

# 조건 2: 0, 1, 2, "가위", "바위", "보" 이외에 다른 입력을 받으면 재입력 받기

# 조건 3: 게임종료 후 나와 컴퓨터의 총 전적 출력하기

# 🔽 출력 예시

# # 입력
# games = int(input("몇 판을 진행하시겠습니까? : "))
# rsp_advanced(games)

# # 출력
# 가위 바위 보 : 0
# 나: 가위
# 컴퓨터: 보
# 1 번째 판 나의 승리!

# 가위 바위 보 : 1
# 나: 바위
# 컴퓨터: 가위
# 2 번째 판 나의 승리!

# 나의 전적: 2승 0무 0패
# 컴퓨터의 전적: 0승 0무 2패

import random

table_name = ["가위","바위","보"]
table_num = ["0", "1", "2"]
win_condition = ["비겼습니다","컴퓨터승리","플레이어승리"]
win_count = []

def rsp_advanced(games):
    r = 1
    while r <= games:
        print("<Round {}!> \n".format(r))
        me = input("가위(0) 바위(1) 보(2) : ")

        if me in table_num :
            me = table_num.index(me)
            
        elif me in table_name :
            me = table_name.index(me)
            
        else :
            print("입력값을 확인해주세요")
            continue
        
        com = random.randint(0,2)
        print("플레이어 : {0}\n컴퓨터 : {1}".format(table_name[me],table_name[com]))
        
        win_count.append((win_condition[com-me]))
        print("{0}번째판 {1}\n".format(r,win_condition[com-me]))
        r += 1
    
    print("플레이어 : {0}승{1}무{2}패".format(win_count.count("플레이어승리"),win_count.count("비겼습니다"),win_count.count("컴퓨터승리")))
    print("컴퓨터 : {0}승{1}무{2}패".format(win_count.count("컴퓨터승리"),win_count.count("비겼습니다"),win_count.count("플레이어승리")))

while True:
    try :
        games = int(input("몇 판을 진행하시겠습니까? : "))
    except ValueError: 
        print("입력값이 잘못되었습니다 숫자로 입력해주세요")
    else :
        rsp_advanced(games)
        break
