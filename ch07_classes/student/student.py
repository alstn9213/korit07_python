class Student:
    def __init__(self, name, student_id):
        self._name = name
        self.student_id = student_id
        self._grades = {}

        # python 버전의 getter에 해당함
        @property
        def name(self):
            return self._name

        # python 버전의 setter 예시
        @name.setter
        def name(self, value):
            self._name = value

student1 = Student('김일', 2025001)
# getter의 호출예시 객체명.속성명 -> 객체명.메서드명()이 아니라는 것에 주목
print(f'학생 이름: {student1._name}')

# setter 의 호출예시
student1.name = '김영'
print(f'변경된 학생 이름: {student1.name}')

'''
이상의 코드에서 확인 가능한 것은 java를 기준으로만 python 코드를 생각할 때 의문스러운 점이 많다는 것이다.

1. _name 이라는 속성이 있는데 객체명.name을 통해서 '김일'/'김영'이라는 속성값이 출력된다는 점
2. 객체명._name ='김영' 이 아니라 객체명.name = '김영'으로 객체의 속성값을 직접 바꾼 것 처럼 보인다는 점.

그런데 이건 Java 기준을 본 것이고 python으로 풀었을 때는 애초에 _name / name은 서로 다른 개념인데 '_'가 붙으면 파이썬 언어 내부적으로 동일한 속성으로 처리해준다.

다만 더 신기한 것은 객체명.속성명 뒤에 ()가 없음에도 파이썬은 메서드처럼 처리해준다는 것이다. 그래서 '객체명.속성명'이면  getter로 처리해주고, '객체명.속성명 = 데이터' 면 setter로 처리해준다고 보면 된다.

이상의 코드라인이 성립하기 위해서 필수적인 부분이
'@property'와 '@속성명.setter'라는 '데코레이터(decorator)'때문이다.

그래서 원래는 자동 생성되기 때문에 일일이 애너테이션 달고 _속성명인지 그냥 속성명인지 따질 필요가 겂는데 지금은 쓸모가 없는 상황

python으로 백엔드를 짜지 않을 것이기 때문에 일단 이런 방식으로 setter / getter를 생성한다는 점만 유의. springboot에 대비하여 java방식의 setter / getter를 작성하겠다.
'''
