try:
    num=str(input('enter number'))
except:
    print('invalid number')
##문자열 길이를 세서 앞에서부터 바로 콤마 적용하자.
##그다음은 콤마를 넣게 하기
def make_comma(num):
    cnt=0
    remainer=len(num)%3
    for s in num:
        print(s,end='')           
        cnt=cnt+1
        if cnt==remainer:
            print(',',end='')
        elif cnt==len(num):
            break
        elif cnt%3==remainer:
            print(',',end='')
make_comma(num)