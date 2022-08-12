import random

def bs31():
    game = list(range(1,32)) # 31까지 범위 list만들기
    
    while True:
        my = list(map(int, input("My turn - 숫자를 입력하세요(최대 3개): ").split())) # 입력값을 int ,list 로 바로 변환
        
        if game[0] == 31:
            print("컴퓨터 승리") # 플레이어가 31을 부르면 패배
            quit()
        elif len(my) <= 3 and my == game[:len(my)]: # 입력값이 3개 이하이고 입력값과 남은 숫자들을 매치해서 잘못된 숫자가 없는지 체크
            for i in my:
                game.remove(i) # 차례로 남은 숫자들을 제거
            try:
                print(f"현재 숫자 : {game[0]-1}") # 현재숫자는 마지막으로 제거한 숫자임으로 -1을 해준다
            except:
                print("컴퓨터 승리") # 위의 elif 조건식에서 error가 발생하면 플레이어의 패배 조건임으로 try문으로 컴퓨터 승리 출력
                quit()
            com = random.randint(1,3) # 1~3까지 3가지의 랜덤한 숫자를 생성
            while com: # com 값이 0일때 while문을 탈출하도록 함
                if game[0] == 31: # 31을 불렀는지 먼저 체크 한뒤 컴퓨터가 31을 부르면 플레이어 승리
                    print("플레이어 승리!")
                    quit()
                else:
                    print(f"컴퓨터 : {game[0]}")
                    game.remove(game[0])
                    com -= 1
            print(f"현재 숫자 : {game[0]-1}\n")
        else :
            print("입력값이 잘못되었습니다\n")
            continue
        
bs31()