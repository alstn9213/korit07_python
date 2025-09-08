'''
아까는 일종의 setter를 활용하여 속성에 속성값을 넣어줬다.
Java에서 수업한 것처럼 속성값이 대입되지 않은 객체를 생성한 다음에 속성값을 집어넣어준느 과정을 거쳐야한다.

그런데 매개변수 생성자를 정의해버리면 객체 생성시에 속성값을 넣을 수 있다.

'''

# class Candy:
#     def set_info(self, shape, color):
#         self.shape = shape
#         self.color = color
#
#     def show_info(self):
#         print(f'사탕의 모양은 {self.shape}이고, 색깔은 {self.color}입니다.')
#
#
# satang = Candy()
# satang.set_info('구형', '갈색')
# satang.show_info()

''' 
속성값에 대한 제한이 있지 않다면 빈 객체를 만들고 거기에 값을 대입하는 것이 비효율적으로 느껴진다. 그래서 생성자를 도입한다.

Java / Js 등에서는 생성자명은 클래스명과 동일하거나 constructor인데, python만 다르다.
'''

# class Candy2:
#     def __init__(self, shape, color):
#         self.shape = shape
#         self.color = color
#
#     def show_info(self):
#         print(f'사탕의 모양은 {self.shape}이고, 색깔은 {self.color}입니다.')
#
# # 객체 생성 방식에서 차이가 있다.
# satang2 = Candy2('정육면체', '흰색')
# satang2.show_info()
#
# class Sample:
#      # 생성자 정의
#     def __init__(self):
#         print('인스턴스가 생성되었습니다.')
#     def __del__(self):
#         print('인스턴스가 소멸되었습니다.')
#
# # 객체 생성
# sample = Sample()
# print()
# # 객체 소멸자 호출 방법
# # del sample # del 객체명
# print('객체 지운 후의 코드라인입니다.')

'''
굳이 소멸자를 학습하는 이유 -> 객체가 생성되면 메모리 공간을 차지해서, 객체가 호출될때마다 그곳에서 불려나오게 된다.
하지만 특정 객체가 일정 코드라인이후로 전혀 사용되지않을 때도 여전히 메모리를 차지하기 때문에 소멸자를 통해서 강제로 객체를 삭제해주면 메모리 관리가 편하다.
그럴때 쓰지만 프로젝트때는 안쓸듯.

기본 예제

생성자를 이용해서 용량을 가진 usb 인스턴스를 만드는 프로그램
지시사항
1. 클래스 USB를 정의할 것
2. 생성자를 정의하여 매개변수로 capacity를 받을 것
3. get_info() 메서드 정의

main 단계 코드
usb = USB(64)
usb.get_info()

실행예
USB객체가 생성되었습니다.
64GB USB
'''

# class USB:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         print('USB객체가 생성되었습니다.')
#
#     def get_info(self):
#         print(f'{self.capacity}GB USB')
#
# usb = USB(64)
# usb.get_info()

'''
man = Person('james')
woman = Person('emily')

james is born
emily is born

del man

james is dead
'''

# class Person:
#     def __init__(self, name):
#         self.name = name
#         print(f'{name} is born')
#
#     def __del__(self):
#         print(f'{self.name} is dead')
#
# man = Person('james')
# woman = Person('emily')
#
# del man
'''
james is born
emily is born
james is dead
emily is dead

모든 코드블럭이 읽어지면 메모리에 할당된 객체는 자동 소멸한다.
강제로 emily is dead를 출력하고싶지않다면 꼼수가 필요하다.
'''

# input('소멸자가 호출되는 것을 막는 중입니다.')

'''
python판 getter / setter
setter는 call2() -> 매개변수 o / 리턴 x
getter는 call3() -> aoroqustn x / 리턴 o
'''

class Student:

    # setter
    def set_name(self, name):
        self.name = name
    # getter
    def get_name(self):
        return self.name


    def set_age(self, age):
        if age < 0 or age > 200:
            print('불가능한 나이 입력입니다.')
            # return # 메서드에 return하고 비워두면 메서드 종료
        else:
            self._age = age


    def get_age(self):
        return self._age

    def set_score(self, score):
        if score < 0 or score > 4.5:
            print('불가능한 점수 입력입니다.')
        else:
            self.score = score

    def get_score(self):
        return self.score




student1 = Student()
student1.set_name('김일')
student1.set_age(20)
student1.set_score(4.5)
print(f'{student1.get_name()} 학생의 나이는 {student1.get_age()}살로 파이썬 과목의 점수는 {student1.get_score()}점 입니다.')

'''
age / address / score 속성을 setter를 통해 추가
이상의 속성에 맞는 getter 추가

student1 객체를 생성
김일, 20, 4.5를 각각 이름/나이/점수에 대입

getter만을 활용하여,
김일 학생의 나이는 20살로, 파이썬 과목의 점수는 4.5점입니다.


java를 기준으로 setter 내부에는 비지니스 로직이 들어갈 수 있었다.

set_age()의 경우 내부에 로직으로 0살 미만과 200살 초과의 나이는 입력이 불가능하게끔 제한

set_score()의 경우에도 0.0미만과 4.5 초과는 입력이 불가능하게끔 비지니스 로직 작성

매개변수 생성자를 통해서 생성했는데 객체 생성 시점에 -102살을 입력하면 되는 것아니냐하는 문제가 있는데 추후 설명
'''


student1.set_age(300)
print(f'{student1.get_age()}')
student1.set_score(5)
