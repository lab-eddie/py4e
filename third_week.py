# 📌Q1. 숫자를 입력 받고 그 숫자의 구구단을 출력하는 함수를 만들어 봅시다. 다만 아래의 조건을 만족해 주세요.

# 조건 1: 홀 수 번째만 출력하기

# 조건 2: 값이 50이하인 것만 출력하기

# 🔽 출력 예시

# # 입력
# number = int(input("몇 단? : "))
# gugudan(number)

# # 출력
# 몇 단? : 8
# 8 단
# 8 X 1 = 8
# 8 X 3 = 24
# 8 X 5 = 40

def multiple_odd(number,odd):
   for odd_num in odd:
       # 구구단 결과값을 내기위해 number는 구구단의 단수, odd_num은 홀수list, result는 결과값
        result = number * odd_num
        # 50 이하만을 출력하기 위해 if문으로 50이하로 범위를 잡고 else로 50초과시엔 함수 종료
        if result <= 50:
            print("{0} X {1} = {2}".format(number,odd_num,result))
        else :
            break

# 홀수 리스트 생성 (구구단이기 때문에 1 ~ 10 사이의 홀수만 list에 담았습니다)
odd_list = list(range(1,10,2))

number = int(input("구구단 몇단 ? : "))

multiple_odd(number,odd_list)
