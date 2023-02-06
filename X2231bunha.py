N = int(input())
for i in range(N):
    sum = 0
    for k in range(len(str(i))):
        sum += i[k]            #각자리 수의 합
    if N == sum + i:
        print(i)
