'''
클래스의 정의 형식 :

class 클래스명(파스칼케이스):
    본문
객체 생성 형식 :
객체이름 = 클래스명() # new없음

'''
# 클래스 정의 형식 예시
class WaffleMachine:
    pass

# 객체 생성예시
waffle = WaffleMachine()
print(waffle) # <__main__.WaffleMachine object at 0x000001BF1B1352B0>

'''
클래스의 구성
1. 클래스의 기본 구성
    객체를 만들어 내는 클래스는 객체가 가져야할 구성요소를 지닌다.
    객체를 생성하기 위해서는 객체가 가져야할 값과 기능을 지녀야한다.
    
    값 = 속성(attribute)
    기능 = 메서드(method)
    
    클래스를 구성하는 속성은 두 가지로 구분된다.
        1) 클래스 변수 : 클래스를 기반으로 생성된 모든 인스턴스들이 공유하는 변수 (Java의 static 변수)
        2) 인스턴스 변수 : 인스턴스들이 개별적으로 가지는 변수
        
    메서드는 특징에 따라서
        1) 클래스 메서드
        2) 정적 메서드
        3) 인스턴스 메서드
    Java에서 정적 메서드라고 하던게 클래스 메서드에 해당하고, 정적 메서드는 따로 있다고 볼수도 있고 
    Java의 정적 메서드가 파이썬의 클래스메서드 + 정적메서드라고도 볼수있다.
    
    Java에서 this를 썼는데 python에서는 self를 쓴다.
    
    self 키워드
    인스턴스 변수에서 각각의 객체를 의미하기위해서 self 키워드를 보여준다.
    인스턴스 메서드의 첫번째 매개변수로 항상 self르 추가해야한다.
'''

class Person:
    # 메서드 정의(함수가 클래스 내에 있다.)
    def set_info(self, name, age, tel, address): # call2() / setter
        self.name = name
        self.age = age
        self.tel = tel
        self.address = address

    def show_info(self): # call1()
        print(f'이름 : {self.name}')
        print(f'나이 : {self.age}')
        print(f'연락처 : {self.tel}')
        print(f'주소 : {self.address}')

    def show_info2(self): # call3()
        return f'제 이름은 {self.name}이고, {self.age}살 입니다.\n연락처는 {self.tel}인데, {self.address}에 살고있습니다.'


# 객체 생성
person01 = Person()

# Person 메서드의 메서드 호출
person01.set_info('김일', 20,'010-1234-5678', '서울특별시 마포구')
person01.show_info()

# 객체 생성
person02 = Person()
person02.set_info('김민수', 27,'010-8384-9213', '부산시 북구')
print(person02.show_info2())

