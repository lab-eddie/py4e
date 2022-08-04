# print(format(10000000,","))

# 이번 미션에서는 숫자를 입력 받고 3자리마다 ,를 찍어주는 함수를 만들어 봅시다.

# 출력 예시

# make_comma(1000000)
# 1,000,000

# 입력받은 숫자를 => list, index -3 마다 "," , list를 str => print


def make_comma(inp):
    a = len(inp) % 3 # 자릿수를 3으로 나눴을때 나머지값이 ","가 찍히는 index값인것을 이용
    cipher = 0 # index[0]번째에 ","가 찍히지 않도록 if문으로 index값이 0이 되지 않도록 설정
    if a == 0:
        a = 3
    for num in inp:
        if cipher % 4 == a:
            inp[cipher:cipher] = [","] # for문으로 ","가 찍혀야할 자리를 카운팅하여 list에 추가
        cipher += 1
    result = "".join(inp)# list를 하나의 문자열로 병합
    print(result)

while True: # 입력값이 int가 아닐때 입력값을 재입력 받도록 try except를 사용
    try :
        inp = int(input("숫자를 입력해주세요 : "))
        inp = [n for n in str(inp)] # 입력값 inp를 str으로 변환하여 list로 만듦
        break
    except :
        print("입력값이 잘못되었습니다. 다시 입력해주세요")
        
make_comma(inp)

# def make_comma(number):
#     number = str(number) # int를 str으로 변환
#     length = len(number) # 숫자의 길이
#     num_comma = length // 3 # 3으로 나눠서 찍어야하는 콤마의 개수 구하기
#     if length % 3 ==0: 
#         num_comma = num_comma -1 # 길이가 3으로 나눠질 경우 -1

#     new_number = "" # 새로운 숫자를 담을 변수 생성
#     n = -1 # 인덱스를 거꾸로 가야하기 때문에 -1 
#     while num_comma != 0: # 콤마를 다 찍을 때까지 반복
#         new_number = number[n] + new_number
#         if  n % 3 == 0:
#             new_number = "," + new_number
#             num_comma = num_comma - 1
#         n = n - 1
# 		# 콤마를 다 찍고 남은 앞의 숫자를 더해주면 완성
#     print(number[:n+1]+new_number)

# make_comma(1000000000000)