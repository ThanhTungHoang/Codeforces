n = int(input())
dem = 0
for i in range(0, n):
    x = input()
    if x.count('1') >= 2:
        dem += 1
print(dem)