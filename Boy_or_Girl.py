x = input()
def main_fun(str):
    s = set(str)
    s = "".join(s)
    if(len(s) % 2 == 0):
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")
main_fun(x)