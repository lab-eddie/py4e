import random

def guess_numbers():
    numbers = list(range(1,101)) # 1~100 까지 숫자 리스트
    the_num = random.sample(range(1,101),3) # 1~100 까지 숫자들중 겹치지 않고 랜덤으로 3개 추출
    the_num.sort() # 추출한 숫자를 순서대로 정렬
    round_num = 1 # 라운드 넘버
    cnt = 0 # 최소 중간 최대 값 3개를 맞췄을 시에 완료처리를 위한 카운트
    while True:
        print(f"{round_num}차 시도")
        player = input("숫자를 입력해주세요! : ")
        try: # 입력값이 숫자가 아닐때 예외처리
            player = int(player)
        except:
            print("입력값이 잘못되었습니다. 다시입력해주세요")
            continue
        
        
        if player < 1 or player >= 101: # 1~100 까지 숫자 범위가 아닐때 걸러주기
            print("올바른 값을 입력해주세요\n")
            continue
        
        elif cnt <= 2: # 최소 중간 최대 3가지를 모두 맞추기 전일때 동작
            if player not in numbers: # 예측했던 숫자들은 numbers에서 remove하여 중복 검사 안하도록함
                print("이미 예측에 사용한 숫자 입니다.")
                continue
            elif round_num % 5 == 0: # 5배수 라운드마다 힌트를 줌
                if player > the_num[2]: print(f"최대값은 {player}보다 작습니다")
                elif player > the_num[1]: print(f"중간값은 {player}보다 작습니다")
                elif player > the_num[0]: print(f"최소값은 {player}보다 작습니다")
                else : print(f"최소값은 {player}보다 큽니다")    
            elif player in numbers: # 최소, 중간, 최대 값들 중에 맞췄을 경우에 맞춘 문구 표시
                if player in the_num:
                    if player == the_num[0]: a = "최소"
                    elif player == the_num[1]: a = "중간"
                    else : a = "최대"
                    print(f"숫자를 맞추셨습니다. {player}는 {a}값 입니다.")
                    numbers.remove(player)
                    cnt += 1
                    if cnt == 3: # 3개를 모두 맞췄을 경우에 몇번째인지 표시후에 종료
                        print(f"{round_num}번 시도만에 예측 성공")
                        break
                else : # 맞지 않는 숫자는 numbers 리스트에서 제거하여 중복 검사하지 않도록 함
                    print(f"{player}는(은) 없습니다")
                    numbers.remove(player)
        round_num += 1 # 모든 동작이 끝난후에 다음 라운드로 넘어감

guess_numbers()