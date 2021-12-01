seat = '''


       1     7     13     19     25

       2     8     14     20     26

       3     9     15     21     27

       4     10    16     22     28

       5     11    17     23     29

       6     12    18     24     30


'''
       
price = '''

       [가격]= 1시간당 1500원

'''

print(seat)
print(price)
print("+" * 40)


while True:
    choice1 = int(input("1번부터 30번까지의 자리 중 원하시는 자리의 숫자를 입력해 주세요:"))
    if 1<= choice1 <= 30:
        print(choice1,"번 자리가 선택되었습니다.")
        choice2 = int(input("이용하실 시간을 입력해 주세요:"))
        print(choice1, "번 자리", choice2, "시간 이용 금액은", choice2 * 1500, "원 입니다. 카드 투입구에 카드를 투입해 주세요.")
        break
    else:
        print("자리를 다시 선택해 주세요.")




menu = '''

   <음료>
   1. 아이스 아메리카노 : 1500원
   2. 아이스 카페라떼 : 2000원
   3. 아이스 바닐라라떼 : 2500원
   4. 아이스 초코라떼 : 3000원


'''

print()
print('추가로 음료를 선택하시겠습니까?')
choice3 = int(input('추가로 선택하실거면 1번, 아니면 2번의 숫자를 눌러주세요.'))
if choice3 == 1:
    print(menu)
    
    drink = { '아이스 아메리카노':'1500원', '아이스 카페라떼':'2000원', '아이스 바닐라라떼':'2500원', '초코라떼':'3000원'};
    mydrink = input(str(list(drink.keys())) + '중 선택해주세요.')
    print( '<%s> 의 가격은 <%s>입니다. 카드 투입구에 카드를 투입해 주세요.'%(mydrink, drink[mydrink]))
    print()
           
    print('영수증 출력하실건가요?')
    choice4 = int(input('영수증 필요하시다면 1번, 아니면 2번의 숫자를 눌러주세요>>>'))
    if choice4 == 1:
        print('영수증이 출력되었습니다. 맛있게 드세요.')
    if choice4 == 2:
        print('맛있게 드세요.')
    
           
        
else:
    print('감사합니다. 즐거운 시간 보내세요.')





















