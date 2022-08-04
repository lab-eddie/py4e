# 📌Q4. 2개의 숫자를 입력하여 그 사이에 소수가 몇 개인지 출력하는 함수를 만들어 봅시다.

# 소수: 1과 자기 자신만을 약수로 가지는 수

# 🔽 출력 예시 

# # 입력
# n = int(input("첫 번째 수 입력 : "))
# m = int(input("두 번째 수 입력 : "))
# count_prime_number(n, m)

# # 출력
# 소수개수  4

def count_prime_number(n, m):
    numbers = [i for i in range(n, m+1)]
    print(numbers)   # [3, 4, 5, 6, 7, 8, 9, 10, 11] 소수는 3,5,7,11 4개
    cnt = 0
    for i in numbers:
        for j in range(2, i+1):
            if i % j == 0 and i != j:
                break
            elif i % j == 0 and i == j:
                print(j)
                cnt = cnt+1
    print(f"소수개수 {cnt}")

n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))
count_prime_number(n,m)
    
    