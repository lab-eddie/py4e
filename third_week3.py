# 📌Q3. 2개의 숫자를 입력하여 그 사이에 짝수만 출력하는 함수를 만들어 봅시다. 그리고 중앙값도 함께 출력 해봅시다.(단, 중앙값이 짝수가 아닐 경우에는 중앙값은 출력을 하지 않고, 짝수인 수만 출력한다)

# 중앙값: 정중앙에 있는 값

# 특정 두 숫자 사이의 수들을 리스트로 만드는 법

# n = 1
# m = 10
# numbers = [ i for i in range(n,m+1)] # [1,2,3,4,5,6,7,8,9,10]
# # range(시작 숫자, 끝 숫자 + 1)
# 🔽 출력 예시

# # 입력
# n = int(input("첫 번째 수 입력 : "))
# m = int(input("두 번째 수 입력 : "))
# find_even_number(n, m)

# # 출력
# 첫 번째 수 입력 : 1
# 두 번째 수 입력 : 11
# 2 짝수
# 4 짝수
# 6 짝수
# 6 중앙값
# 8 짝수
# 10 짝수


def find_even_number(n,m):
    if n % 2 == 0:
        numbers = list(range(n,m+1,2))
    else :
        numbers = list(range(n+1,m+1,2))
    for i in numbers:
        print(i,"짝수")
        if i == (n + m) / 2 :
            print(i, "중앙값")
       
n = int(input("시작 숫자를 입력하세요 : "))
m = int(input("마지막 숫자를 입력하세요 : "))

find_even_number(n,m)
