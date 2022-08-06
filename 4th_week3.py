# Q3. 요즘 식당에 들어가면 방명록을 적게 되어있습니다.

# 어느 식당의 사장님이 여러분에게 방명록을 주면서 전화번호를 제대로 적었는지 검사해달라는 부탁을 했습니다.

# 아래와 같은 방명록이 있을 때 방명록을 잘 못쓴 사람의 이름과 잘 못된 번호를 출력하는 함수를 만들어 봅시다.

# 김갑,123456789
# 이을,010-1234-5678
# 박병,010-5678-111
# 최정,111-1111-1111
# 정무,010-3333-3333
 

# 함수에 방명록을 넣으면 txt 파일로 저장되게 해줍니다.
# 제대로 적은 방명록의 조건은 다음과 같습니다
# 010 으로 시작함
# 번호가 - 로 구분이 되어 있음
# -를 포함하여 길이가 13임

# wrong_guest_book(guest_book)

# 잘못 쓴 사람: 김갑
# 잘못 쓴 번호: 123456789

# 잘못 쓴 사람: 박병
# 잘못 쓴 번호: 010-5678-111

# 잘못 쓴 사람: 최정
# 잘못 쓴 번호: 111-1111-1111


import re

def wrong_guest_book(guest_book):
    p_num = re.compile("010-")
    with open("guest_book.txt","w") as f:
        f.write(guest_book)
    with open("guest_book.txt","r") as f:
        a = f.readlines()
        for i in a :
            if p_num.match(i):
                print(i)
            else:
                print("not good")
            
            

guest_book = """김갑,123456789
이을,010-1234-5678
박병,010-5678-111
최정,111-1111-1111
정무,010-3333-3333"""

wrong_guest_book(guest_book)