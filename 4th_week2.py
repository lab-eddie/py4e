# Q2. 어느날 여러분이 어떤 글을 읽고 있는데, 갑자기 특정 글자가 전체 글에서 몇개 들어있는지 궁금해졌습니다. 그럼 한 번 파이썬 함수로 만들어 봅시다.

# 글은 어떤 글이 좋습니다. 인터넷에서 검색해서 복사 붙여넣기로 변수에 넣어 줍니다.

# 변수에 담긴 글을 함수에 넣어주면 txt 파일로 저장도 함께 되도록 해줍니다.

# 출력 예시

# a ="""안녕하세요. 
# 반갑습니다. 파이썬 공부는 정말 재밌습니다.
# """

# count_word(a, "습니다")
# 2

def count_word(a, word):
    with open("4th_week2.txt","w") as f:
        f.write()

    lines = f.readlines()
    for line in lines:
        print(line)

count_word(a, "습니다")
# count = 0

# for i in a :
#     if "습니다" in i :
#         count += 1
    
# print(count)