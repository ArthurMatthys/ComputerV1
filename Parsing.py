import math


a = str(input())

def is_in(lst, a):
    for i in lst:
        if i == a:
            return 1
    return(0)


def is_float(s):
    try:
        a = float(s)
    except ValueError:
        return False
    else:
        return True

def is_int(s):
    try:
        a = float(s)
        b = int (a)
    except ValueError:
        return False
    else:
        return a == b

def handle_arg(lst):
    print(lst)
    if (len(lst) == 1):
        if is_float(lst[0]):
            return 1
        else:
            return 0
    elif (len(lst) == 2 and (is_float(lst[0]) or is_float(lst[1])) and (is_in(lst[0], 'X') or is_in(lst[1], 'X'))):
        return 1
    elif (len(lst) < 1 or len(lst) > 2):
        return 0
    return 0

def arg_to_tab(lst, i):
    if len(lst )
    return 0


def handle_input(lst):
    lst = lst.replace(" ", "")
    lst = lst.replace("x", "X")
    lst = lst.split("=")
    t = []
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
        for j in range(len(lst[i])):
            lst[i][j] = lst[i][j].split("*")
            if handle_arg(lst[i][j]) == 0:
                print("wront input")
                exit()
            #else:
            #    t += arg_to_tab(lst[i][j])

    print(t)

handle_input(a)