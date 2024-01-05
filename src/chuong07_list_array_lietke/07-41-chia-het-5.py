lst = []
n = int(input())
for i in range(n):
    lst.append(int(input()))
answers = []
check = 0
for i in lst:
    if(i % 5 == 0):
        answers.append(i)
        check += 1
if check == 0:
    answers =[0]
print(answers)
