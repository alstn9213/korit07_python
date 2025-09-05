'''
python 대표 컬렉션 종류

1. list 리스트 : 추가 / 수정 / 삭제가 언제나 가능, 순서 있음
2. tuple 튜플 : 추가 / 수정 / 삭제가 불가능, 순서 있음
3. set 세트 : 중복된 값의 저장이 불가능, 순서 없음
4. dict 딕셔너리 : 키 + 값 으로 관리

'''


# list_example = [30, 40, '김이', [100, '김삼']]
# tuple_example = (10, 20, 30, '김사')
# set_example = {100, 200, 300, 400, '김오'}
# dictionary_example = {'이름':'김일', '나이':20, '학교':'코리아아이티'}
#
# print(list_example)
# print(tuple_example)
# print(set_example)
# print(dictionary_example)

'''
1. list
    여러값을 저장할 때 가장 많이 사용. 자료형이 서로 다르더라도 하나의 리스트에 저장가능. 하나의(파이썬에서 리스트와 비슷한 개념)에 동일한 자료형만을 저장할 수 있는 C, Java에 비해 python이 가지는 장점 중 하나(JS도 다양한 자료형이 배열에 저장된다.)
'''

# list의 선언 및 초기화
# li1 = [1,2,3, '김사']
'''
1-1. list의 index / slice
    list는 str과 동일한 방식의 index / slicing을 지원
    1) 인덱스 / 마이너스 인덱스
'''
# print(li1[0])
# print(li1[1])
# print(li1[2])
# print(li1[3])
# print(li1[-1])
# print(li1[-2])
# print(li1[-3])

'''
2) slicing
    str의 슬라이싱과 같이 '시작인덱스:종료인덱스:증감값'으로 이루어져있음
'''

# li2 = [100, 3.14, 'hello'] # list 선언 및 초기화 방법 1
# li3 = list([4,5,6,7,8,9,0]) # list 선언 및 초기화 방법 2
# print(li3[0:4:2]) # 0 번지부터 4번지 앞까지, 2씩 증가시키면서. 결과값 : [4,6]

'''
자바의
String strExample = new String("안녕하세요"); 와 같다.
    3) list element의 추가와 삭제
        list에 새로운 요소를 추가할 때는 .append()/.insert() 메서드를 사용할 수 있다.
        기존 요소를 제거할 때는 .pop() 메서드를 사용한다.
        
        .append() - 항상 마지막 인덱스에 element를 추가
        .insert() - 정해진 위치(인덱스)에 해당 값을 추가
'''

# scores = [30,40,50]
# print(scores)
# scores.append(100)
# print(scores)
# scores.insert(0,90)
# print(scores)

'''
pop()의 경우 빈 괄호로 사용하면 맨 마지막 요소가 삭제됨
pop(인덱스넘버)로 작성하면 해당 인덱스의 마지막 요소를 삭제함
'''
# print(scores.pop()) # pop()은 call3() 유형이다. 즉 return값이 있는데, 삭제한 element 가 return되기 때문에 print(scores.pop())은 현재 scores의 맨 마지막 element인 100이 콘솔에 출력된다.
#
# print(scores.pop(0)) # 결과값 90
'''
또다른 삭제 메서드 : .remove(값)을 사용하면 list내에 해당 값을 찾아 삭제함(argument로 인덱스 넘버를 요구하는 게 아니라 특정 데이터를 요구한다고 볼 수 있다.)
'''
# print(scores.remove(50)) # None / 특정 값을 바로 삭제했으니까.
# print(scores) # [30, 40]

'''
li4 리스트를 선언하고, 1부터 10까지 집어넣는다.
'''

# li4 = []
# for i in range(10):
#     li4.append(i+1)
#
# print(li4)

# for i in range(1, 11):
#     li4.append(i)

'''
각 list 내의 element들을 뽑아내서 *2씩 증가
'''

# for i in range(len(li4)):
#     li4[i] = (li4[i]*2)
# print() # 개행
# # for i in range(len(li4)):
# #     new_element = li4[i]*2
# #     li4[i] = new_element
# # print(li4)
#
# i = 0
# for element in li4:
#     li4[i] = element*2
#     i += 1
# print(li4)
# 사실상 list들에게 동일한 연산을 일괄적으로 적용하는 메서드가 있기 때문에 추후 설명한다. 백엔드보다 프론트에서 더 많이 쓰여서 예시는 이후 수업

'''
2. tuple 튜플
    저장된 값을 변경할 수 없는 list. 순서는 있기때문에 index 넘버와 slicing은 가능하지만 저장된 값 이외에는 추가 / 수정 / 삭제가 불가능
    
    소괄호를 통해서 생성
    
'''

# tu1 = (1,2,3) # 튜플생성방법 1
# tu2 = tuple((4,5,6)) # 튜플생성방법 2
# tu3 = 7,8,9 # 튜플생성방법 3 / 변수 하나에 데이터 여러개
# a, b, c = 7,8,9 # 복수의 변수 선언 및 초기화 방법 -> 즉 변수 개수와 데이터 개수가 같으면 가능
# print(a)
# print(b)
# print(c)
#
# tu4 = 0 # 자료형은 int
# print(type(tu4)) # <class 'int>
# # tu4라고 해서 튜플로 생각하고 변수명을 지었지만 실제로는 그냥 int이다.
# tu5 = 0,
# print(type(tu5))

'''
element 추출 및 slicing은 동일하다
마찬가지로 tuple의 특성상 element의 추가 / 수정 / 삭제가 불가능하다.
'''

# tu6 = 'hello. ', 'good morning', 'my name is ', 'kim-il', 'i am ', '20 ', 'years old.'
# for word in tu6:
#     print(word.title(), end=' ') # Hello.  Good Morning My Name Is  Kim-Il I Am  20  Years Old.
# print()
# print(tu6)

'''
collection의 개념과 내부 element의 자료형이 서로 다르다. tuple의 정의는 내부 element의 추가 / 수정 / 삭제가 불가능한 collection이지만, element들은 가공이 가능하다.

    3. set
        수학의 집합 개념. Java랑 같다.
'''

# set1 = {1,2,3} # 세트 생성 방법 1
# set2 = set({4,5,6}) # 세트 생성 방법 2
#
# print(set1)
# print(set2)

# 굳이 # 1 , 2 를 나눈 이유 : 비어있는 list / tuple / set 생성방법
# li = []
# tu = ()
# set = {}
# print(type(li)) # <class 'list'>
# print(type(tu)) # <class 'tuple'>
# print(type(set)) # <class 'dict'>

'''
se = {}형태로 비어있는 set을 생성했을 경우 se는 사실 <class 'dict'>로 나온다. 아직 배우지 않은 dictionary 자료형으로 생성된다. 그래서 비어있는 set을 생성하기 위해서는 반드시 # 2 방식으로 만들어야한다.
'''

# se2 = set({})
# print(type(se2)) # 결과값 : <class 'set'>

'''
list / tuple은 index가 존재한다. 이 두개를 sequence라고하고 set / dictionary의 경우 index가 없어서 비시퀸스라는 표현을 쓴다. 그래서 슬라이싱이 없다.
    element 관련 메서드
        1. .add() - set에 새로운 element  추가
        2. .remove() - 기존 element 삭제
        3. .discard() - 기존 element 삭제
'''

# se3 = {10, 20, 30}
# se3.add(50)
# print(se3) # {10,20,50,30} - 순서가 없어서 매번 다르게 나올수있다.
# se3.remove(30) # 순서가 없기 때문에 '값'을 정확하게 입력해야한다.
# print(se3) # 결과값 : {10, 20, 50}

# remove() vs. discard()
# se3.remove(70) # 오류발생 - '값을 정확하게 입력'해야만 한다.

# 향상된 for문으로 element를 추출할 수는 있다. 순서는 보장안됨
# for element in se3:
#     print(element)

'''
    4. dict(ionary) - Java에서 Map / Js에서 Object / JSON과 같은 형식
'''

# dict1 = {
#     '이름': '김일',
#     '나이': 20,
#     '주소': ['서울특별시', '마포구', '목동'],
#
# }

'''
dict의 element 마지막에 콤마를 써도 오류안남.
인덱스는 존재하지 않지만 key를 인덱스와 유사하게 사용한다. key를 알면 값을 확인할 수 있는 구조
'''
# list의 element 추출 반복문 작성
# li01 = [10,20,30,40]
# for num in li01:
#     print(num)
#
# # dict에서 같은 방식의 반복문을 활용할 때
# # dict / Js Object에서 향상된 for문으로 반복문을 돌리면 key가 나온다. 그래서 딕셔너리명[key]로 작성해야 value를 조회할 수 있다.
# for key in dict1:
#     print(key)
#     print(dict[key])
#
# # key들만 추출하는 메서드
# print(dict1.keys()) # dict_keys(['이름', '나이', '주소'])
# print(type(dict1.keys())) # <class 'dict_keys'>
#
# # value들만 추출하는 메서드
# print(dict1.values()) # dict_values(['김일', 20, ['서울특별시', '마포구', '목동']])
# print(type(dict1.values())) # <class 'dict_values'>
#
# # key들만 뽑아서 list를 만든다든지 / value들만 뽑아서 list를 만들고 싶다면 형변환 함수를 사용해야한다.
# keys = list(dict1.keys())
# values = list(dict1.values())
# print(keys) # ['이름', '나이', '주소'] -> 인덱스로 추출하는 것이 가능해짐
# print(values) # ['김일', 20, ['서울특별시', '마포구', '목동']]

'''
collections에서 매우 중요한 것은 list를 배웠을 때 list만 생각할 것이 아니라 set이나 tuple, dictionary로 자료형 변경이 가능한가, 어떤 식으로 가능한다, 어떨 때 써야하는가와 같이 종합적인 고려를 하는 역량이다.
    dictionary에서 property 추가 / 삭제
'''

# dict1['직업']='웹퍼블리셔' # 기존에 없는 key를 입력하고 = value 지정하면 된다.
# print(dict1)
# dict1['직업']='웹개발자' # key 하나당 value는 고정이기 때문에 재대입이 이루어진다.
#
# # 삭제방법
# dict1.pop('직업') # key를 알아야 삭제 가능 / .pop()의 return 특성이 중요하다.
# print(dict1)

'''
list[10,20,30,40,50,60,70,80,90,100]의 3번째 요소로부터 7번째 요소만 추출한 결과, 그리고 그 list에서 2번째 요소를 출력하는 프로그램
실행예 
3번 째 요소로 부터 7번째 요소 = [ 30,40,50,60,70]
3번 째 요소로 부터 7번째 요소 중 2번째 요소 = 40
'''
# list = [10,20,30,40,50,60,70,80,90,100]
# # 일반적인 강의에서 하는 단계별 slicing / 추출
# list_sliced = list[2:7]
# print(list_sliced)
# print(list_sliced[1])
#
# # 다른 방식
# print(list[2:7][1])

'''
사용자로부터 1에서 12사이의 월을 입력받아, 해당 월이 며칠까지 있는 지 출력하는 프로그램 (윤년은 고려 x)
실행 예
1 ~ 12 사이의 월을 입력하세요 >>> 2
2월은 28일까지 입니다.
'''

# month = input('1 ~ 12 사이의 월을 입력하세요 >>> ')
#
# # 1
# last_date_dict = {
#     '1':31,
#     '2':28,
#     '3':31,
#     '4':30,
#     '5':31,
#     '6':30,
#     '7':31,
#     '8':31,
#     '9':30,
#     '10':31,
#     '11':30,
#     '12':31,
# }
# print(f'{month}월은 {last_date_dict[month]}일까지 입니다.')
#
# # 2
# last_date_list1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# print(f'{month}월은 {last_date_dict[int(month)]-1}일까지 입니다.')
#
# # 3
# day = 0
# day_list = [28, 30, 31]
# if month == 2:
#     day = day_list[0]
# elif month == 4 or month == 6 or month == 9 or month == 11:
#     day = day_list[1]
# elif month in [1,3,5,7,8,10,12]:
#     day = day_list[2]
# else:
#     print('잘못입력하셨습니다.')
#     day = 'x'
# print(f'{month}월은 {day}일까지 입니다.')

'''
이상의 코드에서 중요한 것은 in이다
in 뒤에는 다양한 것들이 올 수 있는데, 특히 반복가능객체(iterable)이 올 수 있다.
그래서
elif month in [1,3,5,7,8,10,12]:
    day = day_list[2]
의 해석이 중요한데, in 다음에 임의의 list를 초기화하여 month가 임의의 list의 element값을 가지고 있는지 여부를 조건 검토했다고 해석 할 수 있다.
(1,3,5,7,8,10,12)처럼 tuple로 초기화하더라도 문제가 없다.

응용 예제
=
학생들이 원하는 장소를 입력받아 동일한 입력을 무시하고 모든 입력을 저장하려한다.
학생을 3명으로 가정

실행예
희망하는 수학 여행지를 입력하세요 >>> 제주 
희망하는 수학 여행지를 입력하세요 >>> 제주 
희망하는 수학 여행지를 입력하세요 >>> 민속촌

조사된 수학 여행지는 {'제주', '민속촌'}입니다. 
'''
# li_example = [1,1,2,2,3,3,3]
# se_example = set(li_example)
# li_example2 = list(li_example)
# print(li_example)
# print(se_example)
# print(li_example2)
#
# # set 사용
# field_trip = []
# num_of_students = 3
# for _ in range(num_of_students):
#     student = input('희망하는 수학여행지를 입력하세요 >>> ')
#     field_trip.append(student)
# print(f'조사된 수학여행지는 {set(field_trip)}입니다.')
#
# # dict 사용
# dict1 = {}
# for _ in range(num_of_students):
#     place = input('희망하는 수학 여행지를 입력하세요 >>> ')
#     dict1[place] = _
#
#
# place = list(dict1.keys())
# print(f'조사된 수학 여행지는 {place} 입니다.')


'''
짝수만 추출하기

임의의 양의 정수를 입력받고, 그 정수만큼 숫자를 입력받아 list 작성
저장된 숫자 중 짝수만 새로운 list에 저장하여 출력

실행예
몇 개의 숫자를 입력할까요? >>> 5
1번째 숫자를 입력하세요 >>> 10
2번째 숫자를 입력하세요 >>> 15
3번째 숫자를 입력하세요 >>> 20
4번째 숫자를 입력하세요 >>> 25
5번째 숫자를 입력하세요 >>> 30
입력받은 숫자는 [10,15,20,25,30]입니다.
입력받은 숫자들 중 짝수는 [10,20,30]입니다.
'''

# list1 = []
# list2 = []
# n = input('몇 개의 숫자를 입력할까요? >>> ')
# n = int(n)
# for i in range(n):
#     num = input(f'{i+1}번째 숫자를 입력하세요. >>> ')
#     num = int(num)
#     list1.append(num)
# print(f'입력받은 숫자는 {list1}입니다.')
#
# for i in range(len(list1)):
#     if list1[i] % 2 == 0:
#         list2.append(list1[i])
# print(f'입력받은 숫자들 중 짝수는 {list2}입니다.')

'''
사용자로부터 3명의 이름과 전화번호를 입력받아 딕셔너리에 저장한 뒤, 입력한 정보를 추출

실행예
1 번째 사람의 이름을 입력하세요 >>> 김일
1 번째 사람의 연락처를 입력하세요 >>> 010-1234-5678
2 번째 사람의 이름을 입력하세요 >>> 김이
2 번째 사람의 연락처를 입력하세요 >>> 010-2345-6789
3 번째 사람의 이름을 입력하세요 >>> 김삼
3 번째 사람의 연락처를 입력하세요 >>> 010-3456-7890

입력받은 연락처는 {'김일': '010-1234-5678', '김이':'010-2345-6789'}입니다.
'''

# dict1 = {}
# for i in range(3):
#     name = input(f'{i+1}번째 사람의 이름을 입력하세요 >>> ')
#     phone = input(f'{i+1}번째 사람의 연락처를 입력하세요 >>> ')
#     dict1[name] = phone
# print(f'입력받은 연락처는 {dict1}입니다.')

'''
숫자를 입력한 횟수만큼 비어있는 list에 숫자를 추가하기
문제 : 비어있는 numbers1을 선언하고, 그 안에 입력받은 횟수만큼 숫자를 추가하시오

함수정의 : add_numbers()
매개변수 : 정수 n

함수호출 
add_numbers(last_num)
print(add_numbers2(last_num))

실행예
숫자 몇까지 입력하시겠습니까? >>> 10
[1,2,3,4,5,6,7,8,9,10]
[1,2,3,4,5,6,7,8,9,10]

'''
# list1 = []
# list2 = []
# list3 = []
#
# last_num = input('숫자 몇까지 입력하시겠습니까? >>> ')
# last_num = int(last_num)

# # call2()
# def add_numbers1(last_num):
#     for num in range(last_num):
#         list1.append(num+1)
#     print(list1)

# add_numbers1(last_num)
#
# # call4()
# def add_numbers2(last_num):
#     for num in range(last_num):
#         list2.append(num+1)
#     return list2

# print(add_numbers2(last_num))

# hello = ['안', '녕', '하', '세', '요']

# def add_numbers3(last_num, str_list):
#     for num in range(last_num):
#         list3.append(num+1)
#     for string in str_list:
#         list3.append(string)

# add_numbers3(last_num, hello)
# print(list3)

# list4 = []
# def add_numbers4(last_num, str_list):
#     for i in range(last_num):
#         list4.insert(i, i+1)
#     for string in str_list:
#         list4.insert(len(list4), string)
#
# add_numbers4(last_num, hello)
# print(list4)

'''
짝수와 홀수 개수 세기
list를 입력받아 짝수와 홀수의 개수를 세는 함수 

함수정의
count_even_odd
매개변수 : list numbers(요소는 모두 정수)

호출 
count_even_odd([1,2,3,4,5,6,7,8,9,10])

실행예
짝수의 개수:5개
홀수의 개수:5개
'''


# 1
def count_even_odd(list_numbers):
    odd_list = []
    even_list = []
    for number in list_numbers:
        if number % 2 == 0:
            even_list.append(number)
        else:
            odd_list.append(number)
    print(f'짝수의 개수: {len(even_list)}개')
    print(f'홀수의 개수: {len(odd_list)}개')

count_even_odd([1,2,3,4,5,6,7,8,9,10])

# 2
def count_even_odd2(list_numbers):
    evens = []
    for number in list_numbers:
        if number % 2 == 0:
            evens.append(number)
    print(f'짝수의 개수: {len(evens)}개')
    print(f'홀수의 개수: {len(list_numbers)-len(evens)}개')
count_even_odd2([1,2,3,4,5,6,7,8,9,10])
