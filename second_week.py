import random
# 가위바위보는 3가지 중에서만 낼수 있으므로 테이블을 만들었어요
table = ["가위","바위","보"]
# 잘못된 입력값을 처리하는 while문 입니다.
while True:
    my = str(input("가위 바위 보! : "))
    if my not in table:
        print("가위 바위 보 중에서만 입력해주세요!")
    else:
        break        
# 랜덤으로 숫자를 테이블의 번호로 바로 호출하여 '가위,바위,보'중에 바로 값 설정
com = table[random.randint(0,2)]
# 플레이어가 이기는 조건은 단 3가지 이므로 이길 수 있는 조건을 설정
win_condition = [["가위", "보"], ["바위", "가위"], ["보", "바위"]]

this_game = [my, com]

class rsp:
    def __init__(self, my, com):
        self.my = my
        self.com = com
        print("\n플레이어 : {0}\n컴퓨터 : {1}".format(my, com))
        if my == com :
            print("비겼습니다")
        elif this_game in win_condition:
            print("플레이어 승리!")
        else:
            print("컴퓨터 승리ㅠㅠ")
            
rsp(my, com)