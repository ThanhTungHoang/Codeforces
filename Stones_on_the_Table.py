n = int(input())
s = input()
R = G = B = 0
for i in range(1, n):
    if(s[i-1] == s[i]):
        if(s[i] == "R"):
            R = R+1
        elif (s[i] == "G"):
            G = G+1
        else:
            B = B+1 
print(R+G+B)