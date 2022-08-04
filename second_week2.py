# monthly_payment = int(input("월급을 입력해주세요 : "))

# before_tax = monthly_payment * 12

# class yearly_payment():
#     def __init__(self, monthly_payment):
#         self.monthly_payment = monthly_payment
#         if before_tax > 50000:
#             tax_rate = 0.42
#         elif before_tax > 30000:
#             tax_rate = 0.40
#         elif before_tax > 15000:
#             tax_rate = 0.38
#         elif before_tax > 8800:
#             tax_rate = 0.35
#         elif before_tax > 4600:
#             tax_rate = 0.24
#         elif before_tax > 1200:
#             tax_rate = 0.15
#         else:
#             tax_rate = 0.06
            
      
#         after_tax = int(before_tax * (1 - tax_rate))
#         print("세율 {}% 적용".format(tax_rate * 100))
#         print("\n세전 연봉 : {0}\n세후 연봉 : {1}".format(before_tax, after_tax))
        

# yearly_payment(monthly_payment)

tax_table = {1200 : 6, 4600 : 15, 8800 : 24, 15000 : 35, 30000 : 38, 50000 : 40}
while True:
    try:
        salary = int(input("월급을 입력해주세요 (단위 : 만원) : ")) * 12
        if salary < 0 :
            print("입력값이 잘못되었습니다")
        else:
            break
    except:
        print("입력값이 잘못되었습니다")
    
if salary == 0:
    print("당신은 백수입니다")
    quit()
    
flag = False
for i in tax_table.keys() : 
    if salary - i <= 0:
        print ("세 율 : {}%".format(tax_table[i]))
        print ("세전 연봉 : {}".format(salary))
        print ("세후 연봉 : {}".format(int(salary * ((100-tax_table[i]) / 100))))
        flag = True
        break

if flag == False :
    print ("세 율 : 42%")
    print ("세전 연봉 : {}".format(salary))
    print ("세후 연봉 : {}".format(int(salary * 0.58)))
