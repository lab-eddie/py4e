# Q3. 숫자 맞추기 게임을 만들어 볼게요. 컴퓨터가 임의의 숫자를 3개 만들고 우리가 그것을 맞춰보겠습니다.

# 😲조건1 - 숫자는 0 ~ 100까지 숫자를 3개 만듭니다(중복 불가).
# 😲조건2 - 5회, 10회까지 정답을 못맞추면 최솟값, 최대값에 대한 힌트를 줍니다.
# 😲조건3 - 정답을 맞추면, 맞춘 정답이 최솟값인지, 중간값인지, 최댓값인지 알려줍니다.
# import random
# number = random.randint(0, 100)
# ✅출력 예시
# guess_numbers()

# 1차 시도
# 숫자를 예측해보세요 : 39
# 숫자를 맞추셨습니다! 39는 최솟값입니다.
# 2차 시도
# 숫자를 예측해보세요 : 48
# 숫자를 맞추셨습니다! 48는 최댓값입니다.
# 3차 시도
# 숫자를 예측해보세요 : 100
# 숫자를 맞추셨습니다! 100는 최댓값입니다.
# 게임종료
# 3번 시도만에 예측 성공

# ...
# 5차 시도
# 숫자를 예측해보세요 : 9
# 9는 없습니다
# 최솟값은 9보다 작습니다
# 6차 시도
# 숫자를 예측해보세요 : 9
# 이미 예측에 사용한 숫자입니다
# 6차 시도

# 플레이어는 0~100 까지 리스트 안에서 먼저 검사를 하고 부르는 숫자를 리스트에서 제외시키기

import random
numbers = list(range(0,100))
the_number = random.sample(range(0,100),3)
the_number.sort()
print(the_number)
maximin = "최소","중간","최대"
result = dict(zip(the_number,maximin))
print(result)

round_num = 0
while True:
    round_num += 1
    print(f"{round_num}차 시도")
    player = int(input("숫자를 입력해주세요! : "))
    if player not in the_number:
        print(f"{numbers.pop(player)} 은(는) 없습니다.")
    else :
        for i in result.keys():
            if player == i:
                print(f"{player}는 {result[i]}값 입니다")
                