'''
1. 함수의 종류
    1) 파이썬 내장 함수
    2) 메서드
    3) 사용자 정의함수
2. 함수 용어 정리
    1) 함수정의 : 사용자 함수를 새로 만드는 것을 의미
    2) 인수 : 함수에 전달할 입력값
    3) 매개변수 : 인수를 받아서 저장하는 변수를 의미
    4) 반환값 / 결과값 / 리턴값 : 함수의 출력값
    5) 함수 호출 : 함수를 실제로 사용하는 것
3. (사용자) 함수의 형식 :
def 함수_이름(매개변수1, 매개변수2):
    실행문
    return
변수 = 함수_이름(argument1, argument2)
'''
# 함수정의
def display_name(name):
    print(f'당신의 이름은 {name}입니다.')

# 함수 호출
display_name('김일')

def display_name_age(name, age):
    print(f'당신의 이름은 {name}이고, 나이는  {age}살 입니다.')

display_name_age('김이', 30)
display_name_age(age=23, name='김삼') # keyword argument 방식
'''
name = input('이름을 입력하세요 >>> ')
input이라는 파이썬 내장함수를 사용했다. 파이썬 내장함수는 이미 정의가 되어있다.

사용자 정의 함수의 경우 개발자 자신이 함수를 정의한다.

내장 함수 예시
print(), type(), int(), float(), input()

2. 메서드: 특정 객체가 가지고있는 함수를 의미. 특정 자료형에 포함되어있는 함수. 사실 함수와 메서드는 동일한 개념이지만 호출 방식에 차이가 있다.

함수는 독립적으로 사용가능 / 메서드는 특정 객체를 통해서만 호출 가능
'''
# 메서드의 예시
# eng_name = input('당신의 이름을 영어로 입력하세요 >>> ')
'''
함수 호출해서 그 결과값을 변수에 담았다.
input()의 결과값의 자료형은 str이었다.
'''
# print(eng_name)
# eng_name = eng_name.upper()
# print(eng_name)
'''
그렇다면 eng_name.upper()의 경우 .upper()가 메서드에 해당하고, 해당 메서드는 str 자료형에 종속되어있다고 볼 수 있다.
함수의 유형
'''

# 매개변수 x / 리턴 x
def call1():
    print('[x|x]')

# 매개변수 o / 리턴 x
def call2(unknown_parameter):
    print('[o|x]')
    print(f'{unknown_parameter}라고 입력했다.')
# 매개변수 x | 리턴 o
def call3():
    print()
    return 1
# 매개변수 o | 리턴 o
def call4(unknown1, unknown2):
    print('[o|o]')
    return unknown1 + unknown2



# 함수 호출
call1()
call2('오늘의 날씨는 시원한 편')
call2(12345)
call3() # 결과값 [x|o] 만 나옴
print(call1())
print(call4('안녕', '하세요'))
print(call4(unknown1=1234, unknown2=5678))

'''
700원짜리 음료수를 뽑을 수 있는 자판기 프로그램
돈을 넣으면 몇 잔의 음료수를 뽑을 수 있는지, 잔돈은 얼마인지 모든 경우의 수를 출력

함수 정의
- 반환값 : 없음
- 함수이름 : vending_machine
- 매개변수 : 정수 money

코드 구성
def vending_machine():
    # 함수 구현
    
vending_machine(3000)

'''


def vending_machine(money):
    juice = 0
    while money >= 0:
        print(f'음료수={juice}개, 잔돈={money}원')
        money -= 700
        juice += 1

vending_machine(3500)

my_money = 3000
drink_price = 700
for i in range (my_money // drink_price + 1):
    print(f'음료수={i}개, 잔돈={my_money-(drink_price*i)}')



'''
예제: 구구단
함수 정의 :
함수 이름 : multifly
매개변수 : 정수 n
리턴값 : 없음

함수 호출 :
multiply(dan)
'''

# dan = input('몇 단을 출력하시겠습니까? >>> ')
# dan = int(dan)
# def multiply(dan):
#     n = 1
#     while n < 10:
#         print(f'{dan} x {n} = {dan * n}')
#         n += 1
#
# multiply(dan)
#
# def multiply2(n):
#     for i in range(1, 10):
#         print(f'{n} x {i} = {dan * i}')
#
# multiply2(dan)

'''
range함수의 parameter 적용순서
1 개만 있을 때 : 한계값
2 개 있을 때 : 시작값, 한계값
3 개 있을 때 : 시작값, 한계값, 증감값

multiply를 call2()유형으로 정의했다고 볼수있다.
call1()으로 정의했을 때
몇 단을 출력하시겠습니까? >>> 5
5 x 1
'''



def multiply():
    dan = input('몇 단을 출력하시겠습니까? >>> ')
    dan = int(dan)
    for i in range(1, 10):
        print(f'{dan} x {i} = {dan * i}')

multiply()