import random

numbers = list(range(0,100))
the_num = random.sample(range(0,100),3)
the_num.sort()
print(the_num)
round_num = 1
cnt = 0
while True:
    print(f"{round_num}차 시도")
    player = input("숫자를 입력해주세요! : ")
    try:
        player = int(player)
    except:
        print("입력값이 잘못되었습니다. 다시입력해주세요")
        continue
    
    round_num += 1
    if player < 0 or player >= 100:
        print("올바른 값을 입력해주세요\n")
        continue
    
    elif cnt <= 2:
        if player not in numbers:
            print("이미 예측에 사용한 숫자 입니다.")
            round_num -= 1
            continue
        elif player in numbers:
            if player in the_num:
                if player == the_num[0]: a = "최소"
                elif player == the_num[1]: a = "중간"
                else : a = "최대"
                print(f"숫자를 맞추셨습니다. {player}는 {a}값 입니다.")
                numbers.remove(player)
                cnt += 1
                if cnt == 3:
                    print(f"{round_num}번 시도만에 예측 성공")
                    break
            else :
                print(f"{player}는(은) 없습니다")
                numbers.remove(player)