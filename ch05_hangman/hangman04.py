import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

'''
이상의 코드라인은 내부의 element가 복수의 라인으로 이루어진 str인 list라고 할 수 있다.


'''

# print(stages[0])
# print(stages[1])
# print(stages[2])
# print(stages[3])
# print(stages[4])
# print(stages[5])
# print(stages[6])

# todo - 1 : 남은 기회 숫자를 추적하기 위한 lives 변수를 선언하고 6으로 초기화

# todo - 2 : hangman03을 참조하여 while 반복문 바깥을 완성

# todo - 3 : while문의 조건을 수정하여 6번의 기회가 소진되면 반복문이 종료될 수 있도록 작성

# todo - 4 : lives 변수와 stages 리스트의 관계를 파악하여 guess를 입력할 때마다 올바른 stages의 element를 출력
end_of_game = False
lives = 6
display = []
word_list = ['apple', 'banana', 'camel']
chosen_word = random.choice(word_list)

for _ in range(len(chosen_word)):
    display.append('_')

print(stages[lives])

while not end_of_game:
    guess = input('알파벳을 입력하세요 >>> ').lower()
    if lives == 0:
        print('모든 기회를 잃었습니다.')
        print(stages[lives])
        end_of_game = True
    elif guess not in chosen_word:
        print(stages[lives])
        lives -= 1
        print(f'당신의 기회는 {lives}번 남았습니다.')
    else:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
    print(display)



