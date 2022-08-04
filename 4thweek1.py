# print(format(10000000,","))

# 이번 미션에서는 숫자를 입력 받고 3자리마다 ,를 찍어주는 함수를 만들어 봅시다.

# 출력 예시

# make_comma(1000000)
# 1,000,000

# 입력받은 숫자를 => list, index -3 마다 "," , list를 str => print

# inp = input("숫자를 입력하세요")
# convert_inp = [x for x in str(inp)]
# print(convert_inp)

# cipher = 0
# a = len(convert_inp) % 3
# if a == 0:
#     a = 3
# for i in convert_inp:
    
#     if cipher % 4 == a:
                   
#         convert_inp[cipher:cipher] = [","]
#     cipher += 1

# s = "".join(convert_inp)
# print(s)

def make_comma(inp):
    # 자릿수를 3으로 나눴을때 나머지값이 ","가 찍히는 index값인것을 이용
    a = len(inp) % 3
    cipher = 0
    # index[0]번째에 ","가 찍히지 않도록 if문으로 index값이 0이 되지 않도록 설정
    if a == 0:
        a = 3
    for num in inp:
        if cipher % 4 == a:
            # for문으로 ","가 찍혀야할 자리를 카운팅하여 list에 추가
            inp[cipher:cipher] = [","]
        cipher += 1
    # list를 하나의 문자열로 병합
    result = "".join(inp)
    print(result)

# 입력값이 int가 아닐때 입력값을 재입력 받도록 try except를 사용
while True:
    try :
        inp = int(input("숫자를 입력해주세요 : "))
        # 입력값 inp를 str으로 변환하여 list로 만듦
        inp = [n for n in str(inp)]
        break
    except :
        print("입력값이 잘못되었습니다. 다시 입력해주세요")
        
make_comma(inp)