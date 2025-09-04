import random
from operator import truediv

word_list = ['apple', 'banana', 'camel']
chosen_word = random.choice(word_list)
print(chosen_word)

# todo - 1: 비어있는 list인 display를 만드시오

display = []
# print(display)
# display.append('김')
# print(display)
# display.append(1)
# print(display)

# todo - 2 : chosen_word의 각 문자 개수 마다 '_'를 추가. chosen_word == 'apple'이라면 display = ['_','_','_','_','_']이 되어야한다. 즉, chosen_word의 문자 개수만큼 '_'가 있어야한다

# todo - 3 : chosen_word의 각 문자들을 반복시키시오. 만약 그 위치의 문자가 guess와 일치하면 해당 위치의 display에서 문자를 공개하시오. 예를 들어 사용자가 'p'를 입력했고 chosen_word가 apple이라면 display = ['_', 'p', 'p', '_', '_'] 로 바뀌어야 한다.

for _ in range(len(chosen_word)):
    display.append('_')
    # 반복 실행문에서 변수 i가 쓰이지 않을 경우 '_'를 쓰는 편이다.

for n in range(5).__reversed__():
    guess = input('알파벳을 입력하세요 >>> ')
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    print(f'{n}번 남았습니다.')
    print(display)

