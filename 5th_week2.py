s = ["김갑,3242524215",
"이을,3242524223",
"박병,2242554131",
"최정,4245242315",
"정무,3242524315"]

a = [3,2,4,2,5,2,4,3,1,2]
result = []
for i in range(len(s)):
    l = s[i].split(",")
    name = l[0]
    answer = l[1]
    cnt = 0
    point = []
    for p in answer:
        if a[cnt] == int(answer[cnt]):
            point.append(a[cnt])
        else : pass
        cnt += 1
    result.append(f"{len(point)*10},{name}")
    result.sort(reverse=True)
grade = 1
for i in result:
    print(f"학생 : {i[3:]} 점수 : {i[:2]} {grade}등")
    grade += 1