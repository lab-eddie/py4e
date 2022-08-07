import re

def write_guest_book(guest_book): # 방명록을 먼저 txt 파일로 만들기
    with open("guest_book.txt","w") as f:
        f.write(guest_book)
def wrong_guest_book(guest_book): 
    with open("guest_book.txt", "r") as f:
        a = f.readlines() # 한줄씩 받아와서 a에 담아줌
        for i in a :
            check = re.search("(010)-\d{4}-\d{4}",i) #전화번호 형식에 맞게 정규표현식 사용
            if not check: # 형식에 맞지 않는 방명록 찾기
                wrong = re.compile("\W+")
                result = wrong.split(i) # 정규식에 맞게 split 해준뒤
                name = result[0] # result에서 이름값만 name에 담기
                remove_name = re.findall("\w+\,", i) 
                number = i.replace(remove_name[0],"")# result 값에서 이름값만 지우고 number에 담기
                print(f"잘못 쓴 사람 : {name}\n잘못 쓴 번호 : {number}")
                
            else :
                pass

guest_book = """김갑,123456789
이을,010-1234-5678
박병,010-5678-111
최정,111-1111-1111
정무,010-3333-3333"""

write_guest_book(guest_book)
wrong_guest_book(guest_book)