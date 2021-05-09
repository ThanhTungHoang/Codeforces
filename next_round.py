n, k = map(int, input().split())
counter = 0
ele = input().split()

for i in range(n):
    if int(ele[i]) >= int(ele[k-1]) and int(ele[i]) != 0:
        counter = counter + 1

print(counter)