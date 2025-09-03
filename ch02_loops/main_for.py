'''
for 반복문:
원래 python의 default for문의 경우 enhenced for가 기본이다.
이때 중요한 것이 rang()함수이다.
1
2
3
...
10
출력하는 for문 작성
'''
for i in range(10):
    print(i+1)

'''
파이썬은 자바와 마찬가지로 i가 0부터 시작
자바나 js의
for(int i=0;i<10;i++) {
    System.out.print(i);
    }
    과 같다.
range(): 몇 번 반복할 것인가를 지정하는 함수 -> 특히 for문과 함께 연계돼서 쓰이는 편

range()함수의 응용:
    range((시작값),종료값,(증감값))
    
시작값 : 생략가능, 생략하면 0부터 시작
종료값 : 명시하지않으면 끝까지 진행
증감값 : 생략가능, 생략할 경우에 1씩 증가

for 반복문
형식
for i(아무거나 사용가능) in range(시작값, 종료값, 증감값):
    반복실행문
'''

for i in range(1, 10, 1): # 중요한 점은 종료값의 '미만'으로 적용된다는 점이다.
    print(i)

'''
range() 내에 있는 부분이 
java상에서의 for()의 ()내에 있는 부분을 지정하는 것이라고 볼 수 있다.
'''
str_example = '안녕하세요'
for i in str_example:
    print(i)
'''
range는 필수가 아니라서  default로 작성하면

for 변수명 in iterable(반복가능객체)
    반복실행문
    
range()함수를 쓸 필요없이 반복가능 객체(list / tuple / string / set 등)의 처음부터 끝까지 돌아간다. 향상된 for문과 유사하다.
'''

num_list = [1,2,3,4,5]
for i in num_list:
    print(i, end=' / ') # println이 아니라 한 줄에 쓰기위해 사용하는 방식

# print() 함수는 자동 개행이기 때문에 마무리를 사용자화하고 싶다면 end키워드를 쓸 수 있다.

