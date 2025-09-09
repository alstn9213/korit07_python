n = input('몇 개의 숫자를 입력하시겠습니까? >>> ')
n = int(n)
numbers = []
plus = 0
minus = 0
zero = 0
for i in range(n):
    num = input(f'{i+1}번째 숫자를 입력하시오 >>> ')
    num = int(num)
    numbers.append(num)
    if num > 0:
        plus += 1
    elif num < 0:
        minus += 1
    elif num == 0:
        zero += 1

print(f'양수 : {plus}개')
print(f'음수 : {minus}개')
print(f'0 : {zero}개')

