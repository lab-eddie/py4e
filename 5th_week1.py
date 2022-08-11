# Q1. 여러분 혹시 베스킨라빈스31 게임을 아시나요? 1부터 31까지 숫자를 플레이어들끼리 번갈아 외치다가 31을 외치는 사람이 패배하는 게임인데요.

# 이번엔 이 게임을 파이썬 함수로 만들어 봅시다. 지성이 없이 숫자를 랜덤하게 외치는 컴퓨터와 대결을 해보겠습니다.

# 😲조건1 - 나의 턴에서는 숫자를 직접 입력하며 한 번 입력 후에 space 한 번으로 구분

# Ex)
# my = input("My turn - 숫자를 입력하세요: ")
# 1 2 3
# 😲조건2 - 나와 컴퓨터 모두 한 턴에 1회 ~ 3회까지만 숫자를 외칠 수 있음

# 😲조건3 - 외쳐진 숫자보다 1큰 수만 외칠수 있음 (ex: 5 다음엔 무조건 6)
# ✅ 출력 예시
# bs31()

# 베스킨라빈스 써리원 게임
# ------------------
# My turn - 숫자를 입력하세요: 1 2 3
# 현재 숫자 : 3
# 컴퓨터 : 4
# 현재 숫자 : 4

# My turn - 숫자를 입력하세요: 5
# 현재 숫자 : 5
# 컴퓨터 : 6
# 컴퓨터 : 7
# 현재 숫자 : 7

import random

game = list(range(1,32))
while True:
    my = list(map(int, input("My turn - 숫자를 입력하세요 : ").split()))
    if len(my) > 3: continue
    print(my)
    
    for i in my:
        if i == game[0]:
            game.remove(game[0])
        else :
            print("입력값을 확인해주세요")
            continue
    print(f"현재 숫자 : {game[0]-1}")
    com = random.randint(1,3)
    for n in list(range(com)):
        print(f"컴퓨터 : {game[0]}")
        game.remove(game[0])
    
    print(f"현재 숫자 : {game[0]-1}\n")