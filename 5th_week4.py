def after_100():
    while True:
        
        week_day = ["월","화","수","목","금","토","일"] 
        days = [31,28,31,30,31,30,31,31,30,31,30,31] # 월별 날짜 갯수를 리스트로 미리 만들기
        try:
            month,day,week = input("시작하는 날을 입력해주세요 (예: 6월21일,월요일 => 6 21 월) : ").split()
            month = int(month)
            day = int(day)
        except :
            print("입력값이 잘못되었습니다")
            continue
        if (1 <= month <= 12) and (days[month-1] >= day) and (week in week_day):
            break
        else : print("입력값이 잘못되었습니다 예시에 따라 다시 입력해주세요")
            
    week_100 = week_day[(week_day.index(week)+1)%7] # 100일 뒤의 요일 계산
    now_day = 0 
    # 1월 1일부터 시작하는 날짜까지의 총 날짜수 구하기
    for i in range(month-1): # 월별 전체 날짜가 계산되는 날 더하기
        now_day += days[i]
    now_day += day # 잔여날 따로 더해주기
    
    day_100 = (now_day + 99) % 365 # 10월 이후에는 다음해로 넘어가서 365일이 넘어감으로 365로 나눈 나머지로 계산
    month_100 = 0 # 100일뒤에 월 계산을 위해 0부터 시작
    for n in days:
        month_100 += 1 # 전체 날짜가 계산될때마다 month 카운팅
        if day_100 > n:
            day_100 -= n
        else : 
            break
    print(f"{month_100}월 {day_100}일 {week_100}요일")


after_100()