import random
#word_list 내부의 elemet 중 하나를 임의로 선택하기위해 random 모듈 도입
'''
사용예시
'''
# numbers = [1,2,3,4,5]
# chosen_number = random.choice(numbers) # choice라는 메서드의 argument로 list를 넣었다.
# print(chosen_number)

word_list = ['apple', 'banana', 'camel']
#todo - 1 : word_list에서 단어 하나를 임의적으로 선택하도록 random 모듈을 사용하고 해당 단어를 chosen_word 변수에 담으시오.
chosen_word = random.choice(word_list)
print(chosen_word)
#todo - 2 : 사용자에게 알파벳을 하나 추측해서 입력하라고 요청하고, 이를 guess 변수에 담으시오. 그리고 대문자로 시작하는 경우를 방지하기위해 input() 함수뒤에 .lower()를 적용하시오

#todo - 3 : guess에서 입력한 문자 하나가 chosen_word의 string 문자열 중에 하나의 문자와 일치하는 지를 반복문을 통해 확인할 수 있도록 프로그램을 작성하시오. 맞으면 정답, 틀리면 오답이라고 출력될 수 있도록 할 것.

'''
예를 들어 chosen_word가 apple이고, guess에 a를 입력했다면
정답
이라고 출력될 것
b라고 입력했다면
오답
이라고 출력될것 
'''

# 향상된 for 문
guess = input('알파벳을 하나 입력하세요 >>> ').lower()
for letter in chosen_word:
    if letter == guess:
        print('정답')
    else:
        print('오답')

# 일반 for
for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
        print('정답')
    else:
        print('오답')

