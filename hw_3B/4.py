N = int(input())
nowset = set(range(1, N+1))
question = ''
answer = ''
while 1:
    question = input()
    if question == 'HELP':
        break
    answer = input()
    question = set(map(int, question.split(' ')))
    if answer == 'YES':
        nowset.intersection_update(question)
    else:
        nowset.difference_update(question)
print(" ".join(map(str, sorted([int(i) for i in nowset]))))

