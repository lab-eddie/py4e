import re

def wrong_num(): # 잘못입력되었을 경우가 많아서 함수로 따로 분류하여 호출
    print("잘못된 번호입니다.\n올바른 번호를 넣어주세요.")
    check_id() # 재귀함수로 올바른 값을 다시 입력하도록함

def check_id():
    id_num = input("주민등록번호를 입력해주세요 (예: 123456-1234567) : ")
    check_num = re.fullmatch("\d{6}-\d{7}", id_num) # 주민번호 형식에 올바른지 여부 체크
    if check_num != None:
        if int(id_num[2:4]) > 12 or int(id_num[4:6]) > 31: # 생년월일이 올바른지 체크
            wrong_num()
        
        elif int(id_num[0:2]) <= 22 : # 2000년 이후의 주민번호인지 확인 후에 s값에 성별 값 입력
            millennium = input("당신은 2000년 이후 출생자 입니까? 맞으면 o 틀리면 x : ")
            if millennium == "o":
                if int(id_num[7]) == 3:
                    s = "남자"
                elif int(id_num[7]) == 4:
                    s = "여자"
                else :
                    wrong_num()    
                year = f"20{id_num[0:2]}" # 출생년도 변환
            else :
                wrong_num()
        else: # 2000년 이전 출생자의 성별값 s에 담기
            if int(id_num[7]) == 1:
                s = "남자"
            elif int(id_num[7]) == 2:
                s = "여자"
            else :
                wrong_num()
            year = f"19{id_num[0:2]}" # 출생년도 변환

        month = id_num[2:4] # 출생월 month 변수에 담기
        print(f"당신은 {year}년 {month}월생이고 {s}입니다")    
    
    else:
        wrong_num()

check_id()