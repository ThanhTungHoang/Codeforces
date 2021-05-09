n = int(input())
x = 0
for i in range(n):
    bit_operation = input()
    if bit_operation == "X++" or bit_operation == "++X":
        x = x + 1
    elif bit_operation == "X--" or bit_operation == "--X":
        x = x - 1
print(x)