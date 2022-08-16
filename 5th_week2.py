def grader(s,a):
    result = [] # 결과를 담을 빈 리스트를 생성
    for i in range(len(s)):
        l = s[i].split(",") # ","로 split을해서 이름과 답을 분리
        name = l[0]
        answer = l[1]
        cnt = 0
        point = [] # 점수를 담을 빈 리스트
        for p in answer:
            if a[cnt] == int(answer[cnt]): # 정답과 제출한 정답이 일치할때 정답을 point 리스트에 넣은뒤에
                point.append(a[cnt])
            else : pass
            cnt += 1
        result.append(f"{len(point)*10},{name}") # len(point)*10 이 점수, 이름을 result에 넣고
        result.sort(reverse=True) # 역순 정렬로 점수가 높은 순으로 정렬
    grade = 1
    for i in result:
        table = i.split(",")
        score = table[0]
        name = table[1]
        print(f"학생 : {name} 점수 : {score} {grade}등")
        grade += 1
        
s = ["김갑,3242524215",
"이을,3242524223",
"박병,2242554131",
"최정,4245242315",
"정무,3242524315"]

a = [3,2,4,2,5,2,4,3,1,2]

grader(s,a)

