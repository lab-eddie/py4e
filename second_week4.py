age = int(input("나이를 입력해주세요 : "))

while True :
    bill = (input("지불유형을 선택해주세요 (현금 or 카드) : "))
    if bill not in ["현금", "카드"]:
        print("지불 유형을 확인해 주십시오")
    else:
        break
        
cash_table = [450,1000,1300]
card_table = [450,720,1200]

if age < 8 or age >= 75 :
    bus_fee = 0
elif age >= 20 :
    index = 2
elif age >= 14 :
    index = 1
elif age >= 8 :
    index = 0

if bus_fee == 0:
    bus_fee = "무료"
elif bill == "현금":
    bus_fee = cash_table[index]
else:
    bus_fee = card_table[index]

print(f"\n나이:{age}\n지불유형:{bill}\n버스요금:{bus_fee}")

# class bus_fare:
#     def __init__(self, age, bill):
#         self.age = age
#         self.bill = bill
        
#         if age >= 75:
#             card_fee = 0
#             cash_fee = 0
#         elif age >= 20:
#             card_fee = 1200
#             cash_fee = 1300
#         elif age >= 14:
#             card_fee = 720
#             cash_fee = 1000
#         elif age >= 8:
#             card_fee = 450
#             cash_fee = 450
#         else:
#             card_fee = 0
#             cash_fee = 0
        
#         if bill == "카드":
#             fee = card_fee
#         elif bill == "현금":
#             fee = cash_fee

#         return print("\n나이 : {0}\n지불유형 : {1}\n버스요금 : {2}".format(age, bill, fee))
        
            
            
# bus_fare(age,bill)

