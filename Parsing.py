import math


a = str(input())

def is_in(lst, a):
    for i in lst:
        if i == a:
            return 1
    return(0)


def is_number(s):
    p = 0
    if s == "":
        print("empty string")
        return(0)
    for i in s:
        if (i == '.'):
            p += 1
        elif (i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9'):
            continue
        else:
            return (-1)
    return (p)

def atof(str):
    i = 0
    j = 0
    p = 0
    for t in str:
        if (t == '.'):
            p == 1
        elif (p):
            j = j / 10 + int(t) / 10
        else:
            i = i * 10 + int (t)
    print("i et j et i + j :")
    print(i, j, i+j)
    return (i + j)

def handle_input(lst):
    lst = lst.replace(" ", "")
    lst = lst.split("=")
    if (len(lst) <= 1):
        print(" \'=\' is needed, would you like to add \" = 0\" ? (y) or (n)")
        while (1):
            a = str(input())
            if (a == "y"):
                lst.append("0")
                break
            elif (a == "n"):
                print("wrong input")
                exit()
            else:
                print("please, enter y or n")
    for i in range(len(lst)):
        lst[i] = lst[i].split("+")
        for j in lst[i]:
            if (is_in(j, 'X')):
                j = j.replace("X", "")
                j = j.split("^")
    mult = 0
    is_x = 0
    print(lst)

handle_input(a)