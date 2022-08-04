a = 1
name = input("이름을 적어주세요 : ")
# while문과 try로 점수입력이 잘못되었을시 다시 입력값을 받도록 했습니다
while a:
    try:
        point = int(input("점수를 적어주세요(숫자만 입력해주세요) : "))
          
        if point > 100 or point < 0:
            print("점수를 다시 입력해주세요")
        else:
            a = 0
    except:
        print("입력값이 잘못되었습니다.")
# 점수는 구간별로 학점값을 입력해주었습니다
class grader:
    def __init__(self, name, point):
        self.name = name
        self.point = point
                            
        if  point >= 95:
            grade = "A+"
        elif point >=90:
            grade = "A"
        elif point >= 85:
            grade = "B+"
        elif point >= 80:
            grade = "B"
        elif point >= 75:
            grade = "C+"
        elif point >= 70:
            grade = "C"
        elif point >= 65:
            grade = "D+"
        elif point >= 60:
            grade = "D"
        else:
            grade = "F"

        return print("\n학생이름 : {0}\n점수 : {1}점\n학점 : {2}".format(name, point, grade))

grader(name, point)
