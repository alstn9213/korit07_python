print("Hello Python!")

# 주석
# 사후 주석 ctrl + /
'''다중 주석 처리'''
print(1) # 숫자 자료형
print('1')  # 문자열 자료형
print(1+2) # 3
print('1'+'2') # 12

print(type('1')) # str
print(type(1)) # int
print(type(1.1)) # float

'''
print(): 콘솔에 출력하는 '함수'
type(): 소괄호 내에 있는 데이터(argument)가 어떤 자료형인지 알려주는 명령어
    - JS에서는 typeof가 함수가 아니라 연산자였다.
'''

print('python 수업을 시작했습니다. 파이팅')
print('''
이렇게 다중으로 작성하고 싶을 때는 \'\'\'\'\'\'\'으로 작성하는 방법도 있다.
java는 줄 넘어 갈때마다 +로 연결해줘야했는데 그런 점은 편하다''')

'''
이상에서 알 수 있는 점은 print()가 System.out.println()처럼 자동 개행이 된다는 점이다.

변수(Variable) : 데이터를 저장하는 바구니
'''

# 변수 선언 및 초기화
# 변수명 = 데이터
name = '김일'
age = 20
print('안녕하세요 제 이름은' + name + '입니다. 나이는 ' + str(age) + '입니다.')

'''
python은 조건이 엄격해서 java나 js할 때처럼 처음이 str이면 뒤의 int/float을 자동 형변환해주지않는다.
그때 사용하는 형변환 함수
str(): 다른 데이털르 문자열 자료형으로 바꿔주는 함수
int(): 문자열/실수 자료형을 정수형으로 바꿔주는 함수 /java: (int)"1.3"
float(): 실수 자료형으로 바꿔주는 함수

번거로우니 f-string 개념이 도입됐다.
'''

print(f'안녕하세요 제 이름은 {name}이고, 나이는 {age}입니다.')
'''
js에서는
console.log(`안녕하세요 제 이름은 ${name}이고, 나이는 ${age}살 입니다.`);

java에서의 scanner 같은 기능을 하는 함수 : input()
'''

name2 = input('이름을 입력하세요 >>> ')
print(name2)

