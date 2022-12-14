# Q2. 어느날 여러분이 어떤 글을 읽고 있는데, 갑자기 특정 글자가 전체 글에서 몇개 들어있는지 궁금해졌습니다. 그럼 한 번 파이썬 함수로 만들어 봅시다.

# 글은 어떤 글이 좋습니다. 인터넷에서 검색해서 복사 붙여넣기로 변수에 넣어 줍니다.

# 변수에 담긴 글을 함수에 넣어주면 txt 파일로 저장도 함께 되도록 해줍니다.


def count_word(a, word):
    with open("4th_week.txt", "w") as f: 
        f.write(a) # a변수에 들어온 글을 txt 파일로 만들어주기
    with open("4th_week.txt", "r") as f:
        lines = f.readlines() # 줄 별로 lines 변수에 넣기
        count = 0 
        for line in lines:
            if word in line : count += 1 # 찾으려는 문자를 word에 담아서 줄별로 확인 후 카운팅             
    print(f"찾으시는 \"{word}\"의 갯수는 {count}개 입니다")

a = """중국과 타이완의 군사적 긴장이 최고조에 달하고 있습니다.
중국은 타이완 상공을 가로질러 미사일을 발사했고, 예고한 군사 훈련에 최첨단 스텔스기 등 100여 대의 항공기도 동원했습니다.
이 과정에서 일본 해역에도 미사일이 떨어져 긴장은 더욱 커지고 있습니다.
국제부 뉴스룸을 연결합니다. 이승훈 기자!
중국군이 낸시 펠로시 미국 하원의장의 타이완 방문에 대한 보복으로 미사일 발사를 강행했죠?
[기자]
중국 인민해방군이 타이완의 동서남북에 장거리포와 미사일을 발사했습니다.
이른바, '중요 군사 훈련 실탄사격' 첫날 미사일이 떨어진 곳은 이미 예고한 타이완 주변 6개 구역입니다."""

count_word(a, "습니다")
