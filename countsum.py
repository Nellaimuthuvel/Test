N = int(input())
emptylist1 = []
for i in range(0, N):
    element = int(input())
    emptylist1.append(element)
sum1 = 0
temp = 0
key = int(input())
for i in range(0,key):
    temp = emptylist1[i]
    sum1 = sum1 + temp

print(sum1)
