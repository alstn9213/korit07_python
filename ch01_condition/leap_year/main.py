year = input('윤년인지 확인하고 싶은 연도를 입력하세요 >>> ')
year = int(year)

# 논리연산자 방식
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(f'{year}은 윤년입니다.')
# else:
#     print(f'{year}은 윤년이 아닙니다.')

if year % 400 == 0 or (year % 100 == 0 and year % 4 == 0):
    print(f'{year}은 윤년입니다.')
else:
    print(f'{year}은 윤년이 아닙니다.')
# 기본 방식
# if year % 400 == 0:
#     print(f'{year}는 윤년입니다.')
# elif year % 100 == 0:
#     print(f'{year}는 윤년이 아닙니다.')
# elif year % 4 == 0:
#     print(f'{year}는 윤년입니다.')
# else:
#     print(f'{year}는 윤년이 아닙니다.')
