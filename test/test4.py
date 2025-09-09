candidates = []
n = input('후보자 수를 입력하시오 >>> ')
n = int(n)
votes = {}

for i in range(n):
    name = input(f'{i+1}번째 후보자의 이름을 입력하시오 >>> ')
    candidates.append(name)
    votes[name] = 0

candidates_dict = {}
for num in range(len(candidates)):
    candidates_dict[num+1] = candidates[num]

m = input('전체 투표 횟수를 입력하시오 >>> ')
m = int(m)
for i in range(m):
    vote = input(f'{i+1}번째 투표 {candidates_dict} >>> ')
    vote = int(vote)
    votes[candidates_dict[vote]] += 1

print('---투표결과---')
for key in votes:
    print(f'{key} : {votes[key]}표')