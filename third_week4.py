# πQ4. 2κ°μ μ«μλ₯Ό μλ ₯νμ¬ κ·Έ μ¬μ΄μ μμκ° λͺ κ°μΈμ§ μΆλ ₯νλ ν¨μλ₯Ό λ§λ€μ΄ λ΄μλ€.

# μμ: 1κ³Ό μκΈ° μμ λ§μ μ½μλ‘ κ°μ§λ μ

# π½ μΆλ ₯ μμ 

# # μλ ₯
# n = int(input("μ²« λ²μ§Έ μ μλ ₯ : "))
# m = int(input("λ λ²μ§Έ μ μλ ₯ : "))
# count_prime_number(n, m)

# # μΆλ ₯
# μμκ°μ  4

def count_prime_number(n, m):
    numbers = [i for i in range(n, m+1)]
    print(numbers)   # [3, 4, 5, 6, 7, 8, 9, 10, 11] μμλ 3,5,7,11 4κ°
    cnt = 0
    for i in numbers:
        for j in range(2, i+1):
            if i % j == 0 and i != j:
                break
            elif i % j == 0 and i == j:
                print(j)
                cnt = cnt+1
    print(f"μμκ°μ {cnt}")

n = int(input("μ²« λ²μ§Έ μ μλ ₯ : "))
m = int(input("λ λ²μ§Έ μ μλ ₯ : "))
count_prime_number(n,m)
    
    