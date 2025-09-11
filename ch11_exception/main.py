"""
ch11_exception
main

1. 예외처리의 필요성
    1) 예외(exception) : 개발자가 직접 처리할 수 있는 문제
    2) 오류(error) : 개발자가 처리할 수 없는 문제

    3) 예외 처리의 목적:
        어떤 문제가 발생했을 때 그 문제를 해결해주는 것이 아니라, 발생된 문제로 인해 프로그램이 비정상 적으로 종료되는 것을 막고, 사용자에게 발생한 문제에 대해 정보를 전달하기 위함

2. 예외처리
    1) 고전적 예외 처리
"""
# a = int(input("나누는 수(제수)를 입력하세요 >>> "))
# b = int(input("나누어지는 수(피제수)를 입력하세요 >>> "))
# if a == 0:
#     print("0으로 나눌 수 없습니다.")
# else:
#     result = b / a

"""
coffee_machine에서 
if drink == None:
이라는 방식으로 해봤다.
어떤 값이든 0으로 나눌 수 없기 때문에 if a == 0을 통해 0으로 나누는 것을 아예 시도할 수 없도록 예외 처리함

여기서 생각할 수 있는 문제는:
    1) 어떤 문제가 발생할 지 예상할 수 있어야 미리 대비할 수 있다.
    2) 어떤 문제가 발생할 지 예상할 수 있더라도 대비할 수 없는 경우가 있다.
    
3. 예외처리의 종류
    +------+---------------------+-------------------------------------------+
| 순번 |     예외 클래스     |                    의미                   |
+------+---------------------+-------------------------------------------+
|  1   |    BaseException    |             최상위 예외 클래스            |
|  2   |      Exception      |      대부분 예외 클래스의 슈퍼 클래스     |
|  3   |   ArithmeticError   |         산술 연산에 문제가 있을 때        |
|  4   |    AttributeError   |          잘못된 속성을 참조할 때          |
|  5   |       EOFError      | 파일에서 더이상 읽어들일 데이터가 없을 때 |
|  6   | ModuleNotFoundError |          import할 모듈이 없을 때          |
|  7   |  FileNotFoundError  |          존재하지 않는 파일일 때          |
|  8   |      IndexError     |         잘못된 인덱스를 사용할 때         |
|  9   |      NameError      |       잘못된 이름(변수)을 사용할 때       |
|  10  |     SyntaxError     |              문법이 틀렸을 때             |
|  11  |      TypeError      |  계산하려는 데이터의 유형이 잘못되었을 때 |
|  12  |      ValueError     |   계산하려는 데이터의 값이 잘못되었을 때  |
+------+---------------------+-------------------------------------------+

4. 예외처리 방식
    1) 모든 예외를 처리하는 방식 -> try / except / finally
    형식 :
try:
    코드 작성영역
except
    예외 발생시 처리영역
finally:
    언제나 실행되는 영역
"""
# from prettytable import PrettyTable
#
# exception_list = [(1,"BaseException","최상위 예외 클래스"), (2, "Exception", "대부분 예외 클래스의 슈퍼 클래스"), (3, "ArithmeticError", "산술 연산에 문제가 있을 때"), (4, "AttributeError", "잘못된 속성을 참조할 때"), (5, "EOFError", "파일에서 더이상 읽어들일 데이터가 없을 때"), (6,"ModuleNotFoundError","import할 모듈이 없을 때"),(7,"FileNotFoundError","존재하지 않는 파일일 때"),(8,"IndexError","잘못된 인덱스를 사용할 때"),(9,"NameError","잘못된 이름(변수)을 사용할 때"),(10,"SyntaxError","문법이 틀렸을 때"),(11,"TypeError","계산하려는 데이터의 유형이 잘못되었을 때"),(12,"ValueError","계산하려는 데이터의 값이 잘못되었을 때")]
#
# table = PrettyTable()
# table.field_names = ["순번", "예외 클래스", "의미"]
# table.add_rows(exception_list)
# print(table)

# try:
#     a = int(input("나누는 수(제수)를 입력하세요 >>> "))
#     b = int(input("나누어지는 수(피제수)를 입력하세요 >>> "))
#     print(f'b/a = {b/a}')
# except:
#     print('예외가 발생했습니다.')

'''
기본예제

다음은 사용자가 입력한 키를 정수로 반올림해서 다시 저장하는 프로그램이다.
try / except 사용해서 '예외가 발생했습니다.'를 출력
'''

# try:
#     height = input('키를 입력하세요 >>> ')
#     height = round(height)
#     print(f'입력하신 키는 {height}cm로 처리됩니다.')
# except:
#     print('예외가 발생했습니다.')

'''
    1) 특정 예외만 처리하는 방식
        try / except 문을 사용하면 기본적으로 예외의 종류에 상관없이 모든 예외가 처리됨. 하지만 이상에서 본것처럼, 0으로 나누는 경우와, str 자료형을 실수로 바꾸고자 하는 경우에 서로 다른 멧시지를 출력해줄 수 있다면 개발자에게 예외를 처리할 수 있을만한 추가적인 정보를 제공할 수 있음.
        
        1)-1. 0으로 나누려고하는 경우 -> 0으로 나눌 수 없습니다.
        1)-2. 정수가 아닌 값을 입력하는 경우 -> 정수만 입력할 수 있습니다.
        등으로 특정 예외에 따른 서로 다른 안내문을 제시한다고 하면,
        except문 뒤에 처리하고자하는 예외를 모두 명시하면 된다.
'''

# try :
#     a = int(input('나누는 수를 입력하세요 >>> '))
#     b = int(input("나누어지는 수를 입력하세요 >>> "))
#     print(f'b/a = {b/a}')
# except ZeroDivisionError:
#     print('0으로 나눌 수 없습니다.')
# except TypeError:
#     print('나눌 때 자료형이 일치하지 않습니다.')
# except ValueError:
#     print('정수만 입력할 수 있습니다.')


# try :
#     a = int(input('나누는 수(정수)를 입력하세요 >>> '))
#     b = int(input("나누어지는 수(정수)를 입력하세요 >>> "))
#     print(f'b/a = {b/a}')
# except ZeroDivisionError:
#     print('0으로 나눌 수 없습니다.')

'''
    거의 모든 예외는 Exception 클래스의 서브 클래스에 해당함. 따라서 모든 예외는 Exception의 인스턴스가 된다. 다음과 같이 except의 마지막에 Exception을 명시하면 예상치 못한 예외들도 웬만하면 처리된다.
    
형식 :
try:
    코드 작성영역
except 예외 클래스1:
    예외메시지1
except 예외 클래스2:
    예외메시지2
except Exception:
    예외 메시지n
finally:
    항시 실행되는 코드 영역
    
Java와 동일하게 Exception이 가장 상위에 있으면 모든 예외가 전부 Exception으로 잡히기 때문에 순서 역시 중요하다.

3. 예외 메시지 처리하기 
    이상까지는 특정 예외 발생시 메시지를 커스텀했지만 기본적으로 이미 예와 메시지가 있는 경우도 있다. default exception message를 출력하는 방식 학습
형식 :
try:
    코드 작성영역
except 예외클래스 as 예외메시지
    예외 발생시 처리 영역

'''
# z = [10,20,30,40,50]
#
# try:
#     print(z[10])
# except IndexError as e:
#     print(e)

'''
4. else / finally
    try / except 문에 else / finally를 달 수 있는데
    else : 예외가 발생하지 않으면 처리되는 구문
    finally : 예외 발생 여부와 관계없이 맨 마지막에 항상 처리되는 구문
'''

# try:
#     a = int(input('나누는 수를 정수로 입력하세요 >>> '))
#     b = int(input('나누어지는 수를 정수로 입력하세요 >>> '))
#     result = b/a # 예외가 발생할 수 있는 구간이 try문 내에 있어야만 한다.
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else:
#     print(f'b/a {b / a}')
# finally:
#     print('프로그램이 종료되었습니다.')

'''
5. 강제로 예외 발생시키기
    나이를 정수로 입력받는다.
    -1000이 정수라서 예외가 발생하지않는다.
    하지만 -1000살은 불가능해서 조건문이 아니라 직접 예외를 발생시켜서 처리하는 방법 학습 -> raise 문
    
형식 :
raise 예외클래스()
또는
raise 예외클래스(예외 메시지)

raise의 경우 강제로 예외를 발생시킨다는 점에서 주로 사용되는 예외 클래스는 Exception이다.
'''

# age = int(input('나이를 입력하세요 >>> ')) -1000입력해도 예외발생 x
# print(f'당신의 나이는 {age}살 입니다.')

# try:
#     age = int(input('나이를 입력하세요 >>> '))
#     if age < 0 or age > 200:
#         raise Exception('강제로 발생시킨 예외입니다.')
# except Exception as e:
#     print('발생한 예외 메시지는 다음과 같습니다.')
#     print(e)

'''
특정 예외가 아니라 raise 부분으로 넘어가기만 하면 바로 예외가 발생해버린다.ㅡㅡ
그렇다면 이 부분에서는 조건문을 이용해서 특정 조건일 때만 예외로 넘기는 추가 코드가 필요하다고 할 수 있다.

6. 사용자 정의 예외 클래스
'''

# class NegativeAgeError(Exception): # Exceptin 클래스를 상속받ㅡ다는 의미
#     pass
# class TooManyAgeError(Exception):
#     pass
#
# try:
#     age = int(input('나이를입력하세요 >>> '))
#     if age < 0:
#         raise NegativeAgeError('나이는 음수 일 수 업습니다.')
#     if age > 200:
#         raise TooManyAgeEror('200살을 초과할 수 없습니다.')
# except NegativeAgeError as e:
#     print('발생한 예외 메시지는 다음과 같습니다.')
#     print(e)
# except TooManyAgeError as e:
#     print(e)
# else:
#     print(f'당신의 나이는 {age}살 입니다.')
# finally:
#     print('프로그램이 종료되었습니다.')

'''
사용자의 점수를 0점 이상 100이하 입력받음
80점 이상 합격, 아니면 불합격
0이상 100이하의 유효한 값이 아니면 예외
'점수는 0이상 100이하입니다.' 예외 메시지 출력 -> 사용자 정의 예외 클래스
ScoreOutOfRangeError 클래스 정의

백점 입력시 '점수는 숫자로 입력해야합니다.'출력
실수로 입력시 '정수로 입력해야합니다.' 출력
예상할 수 없는 예외 발생시 Exception 적용하여 디폴트 에러 메시지
프로그램 마지막에 프로그램 종료 메시지
'''

# 0점 미만에 대한 사용자 정의 클래스를 추가할 수 있다.
# class ScoreOutOfRangeError(Exception):
#     pass
#
# try:
#     score = input('점수를 입력하세요 >>> ')
#     score = int(score)
#     if score < 0 or score > 100:
#         raise ScoreOutOfRangeError('점수는 0이상 100이하입니다.')
# except ScoreOutOfRangeError as e:
#     print(e)
# except TypeError as e:
#     print('점수는 숫자로 입력해야 합니다.')
# except ValueError as e:
#     print('정수로 입력해야 합니다.')
# except Exception as e:
#     print(e)
# else:
#     if score >= 80:
#         print('합격')
#     else:
#         print('불합격')
# finally:
#     print('프로그램 종료')

# try:
#     num = input('숫자를 입력하세요 >>> ')
#     num = int(num)
#     result = 100 / num
#
# except ZeroDivisionError:
#     print('0으로 나눌 수 없습니다.')
# except ValueError:
#     print('숫자만 입력할 수 있습니다.')
# except Exception as e:
#     print(e)
# else:
#     print('정상적으로 처리되었습니다.')
#     print(result)
# finally:
#     print('프로그램 종료')

'''
리스트의 인덱스를 입력받는다.
인덱스의 리스트의 값을 출력
인덱스가 범위 벗어나면 메시지 출력
예상되는 예외 적용
예외 발생안하면 정상적으로 입력되었습니다. 메시지와 함께 해당 인덱스의 값을 출력
프로그램 종료 메시지
마이너스 인덱스는 적용 x -> 사용자 정의 클래스 NegativeNumIndexError
'''
# class NegativeNumIndexError(Exception):
#     pass
#
# my_list = [10, 20, 30, 40, 50]
# try:
#     idx = input('인덱스를 입력하세요 >>> ')
#     idx = int(idx) # 3.3을 입력할 경우 반환값은 "3.3"이다 이를 3.3형태의 str을 int로 변환하려면 3.3을 먼저 float으로 변환해야한다.
#     if idx < 0:
#         raise NegativeNumIndexError('0과 양수만 입력해 주세요')
#     num = my_list[idx]
# except NegativeNumIndexError as e:
#     print(e)
# except ValueError:
#     print('정수만 입력해주세요')
# except IndexError:
#     print('인덱스 범위를 벗어났습니다.')
# except Exception as e:
#     print(e)
# else:
#     print(f'정상적으로 입력되었습니다.\n{idx}번 인덱스의 값 : {num} ')
# finally:
#     print('프로그램 종료')
#


'''
속성명을 받는다.
속성명을 사용하여 객체의 속성값을 출력
잘못된 속성명을 입력하면 '존재하지않는 속성입니다.'출력
예외 발생안하면 '정상적으로 출력되었습니다.'와 속성값 출력
프로그램 종료 메시지 출력
'''

class Person:
    school = '코리아아이티아카데미'

    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person(name='김일', age=21)
# print(vars(person1)) # vars(객체명) : 객체의 속성명 - 값을 dict으로 만든다. JSON이 생각나는 부분
# print(getattr(person1, 'age'))
# # getattr의 두번째 argument는 인스턴스 변수명을 받는다. -> 그 데이터를 str로 받는다.
# print(getattr(person1, 'name')) # 결과값 : 김일

# print(person1.school)
# getattr(person1, 'school')
# getattr(person1, school) 두번째 인수가 str이 아니다. 클래스 변수인 school이 main단계에서 선언되지 않은 것으로 간주된다. -> 그래서 NameError가 발생했지 속성명과는 관계가 없다.

try:
    attr = input('속성명을 입력해 주세요 >>> ')
    per_attr = getattr(person1, attr)
except AttributeError:
    print('존재하지 않는 속성입니다.')
except Exception as e:
    print(e)
else:
    print(f'정상적으로 처리되었습니다. {per_attr}')
finally:
    print('프로그램 종료.')

'''
getattr(객체명, 속성명_str) - 특정 객체의 두번째 argument와 일치하는 속성명의 값을 return
vars(객체명) - 특정 객체의 속성명-속성값 쌍을 dict 형태의 key-value 쌍으로 변환
'''

person1_dict = vars(person1)
print(person1_dict)
attr_key = input('출력할 속성명을 입력하세요 >>> ')
print(person1_dict[attr_key])

