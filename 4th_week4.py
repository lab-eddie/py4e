# Q4.  주민등록번호의 앞 6자리는 생년월일이고 뒷자리의 시작번호는 성별을 나타냅니다. 주민등록번호를 입력하면 몇년 몇월 생인지 그리고 남자인지 여자인지 출력하는 함수를 만들어 봅시다.


# 주민등록번호는 6자리 이후에 -로 구분되어야 하고 길이는 -포함 14임
# 뒷자리는 1,3 은 남자 2,4는 여자
# 00 ~ 21로 시작할 경우 2000년 이후 출생자인지 물어 볼 것 (맞으면 o 틀리면 x)
# 뒷자리 3, 4를 가질 수 있는 사람은 00년생 이후 출생자 밖에 없음

# 주민등록번호 조건을 만족하지 않는 수가 입력되면 "잘 못된 번호입니다"를 출력해주세요.

def wrong_num():
    print("잘못된 번호입니다.\n올바른 번호를 넣어주세요.")
    check_id() # 잘못된 번호입력시 다시 입력받기
    
month_check = list(range(1,13))
date_check = list(range(1,32))

import re
def check_id():
    id_num = input("주민등록번호를 입력해주세요 (예: 123456-1234567) : ")
    check_num = re.fullmatch("\d{6}-[1-4]\d{6}", id_num) # 주민번호형식이 올바른지 여부
    if check_num is not None: 
        month = int(id_num[2:4]) 
        date = int(id_num[4:6])
        year = int(id_num[0:2])
        if month not in month_check or date not in date_check: #생년월일이 올바른지 체크
           wrong_num() 
        else: pass
    else: wrong_num()
    
    s = int(id_num[7]) # 성별 값 s에 담기
    
    if year < 22:
        while True: # 2000년 이후 출생인지 여부 판단
            y2k = input("당신은 2000년 이후 출생자입니까? 맞으면 'o' 틀리면 'x' : ")
            if y2k == "o" :
                if s == 3 or s == 4 :
                    year = f"20{year}" # 2000년 이후 출생자 년도 표시
                    break
                else :
                    print("입력값을 확인해주세요")
                    continue
            elif y2k =="x" :
                if s == 1 or s == 2 :
                    year = f"19{year}"
                    break
                else : 
                    print("입력값을 확인해주세요")
                    continue
            else : print("입력값을 확인해주세요") # 입력값이 o,x가 아닐때 다시 묻기
    else : 
        if s == 1 or s == 2 : # 주민번호 앞 두자리가 22보다 클때 성별은 1,2 만 올수있기때문에 마지막 체크
            year = f"19{year}"
        else : wrong_num()
    s = "남자" if s == 1 or s == 3 else "여자" # s를 성별에 맞게 "남자","여자"로 표시
    
    print(f"당신은 {year}년 {month}월생이고 {s}입니다")

check_id()



# import re

# def wrong_num():
#     print("잘못된 번호입니다.\n올바른 번호를 넣어주세요")
#     quit()
    
# def check_id(id_num):
#     if int(id_num[0:2]) <= 22 :
#         millennium = input("당신은 2000년 이후 출생자 입니까? 맞으면 o 틀리면 x : ")
#         if millennium == "o":
#             if int(id_num[7]) == 3:
#                 s = "남자"
#             elif int(id_num[7]) == 4:
#                 s = "여자"
#             else :
#                 wrong_num()
                
#             year = f"20{id_num[0:2]}"
#         else :
#             wrong_num()
#     else:
#         if int(id_num[7]) == 1:
#             s = "남자"
#         elif int(id_num[7]) == 2:
#             s = "여자"
#         else :
#             wrong_num()
#         year = f"19{id_num[0:2]}"

#     month = id_num[2:4]
        
#     print(f"당신은 {year}년 {month}월생이고 {s}입니다")
    
# id_num = input("주민등록번호를 입력해주세요 (예 : 123456-1234567) : " )

# check = re.compile("[0-9]{6}-[0-9]{7}")
# if check.match(id_num):
#     check_id(id_num)
# else:
#     print("주민등록번호 형식이 잘못되었습니다.")