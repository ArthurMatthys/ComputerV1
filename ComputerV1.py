def my_abs(x):
    if x < 0:
        return -x
    else:
        return x


def pow_int(a, b):
    if b == 0:
        return 1
    i = 1
    res = a
    while i < b:
        res *= a
        i += 1
    return res


def my_sqrt(i, prec):
    a = 0
    b = i
    while (b - a) >= prec:
        mid = (a + b) / 2
        if pow_int(mid, 2) > i:
            b = mid
        else:
            a = mid
    return a


def is_in(lst, a):
    for i in lst:
        if i == a:
            return 1
    return 0


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
        b = int(a)
    except ValueError:
        return False
    else:
        return a == b


def handle_arg(lst):
    if (len(lst) == 1):
        if is_float(lst[0]):
            return 1
        else:
            return 0
    elif len(lst) == 2 and (is_float(lst[0]) or is_float(lst[1])) and (lst[0][0] == 'X' or lst[1][0] == 'X'):
        return 2
    elif len(lst) < 1 or len(lst) > 2:
        return 0
    return 0


def arg_to_tab(lst, i):
    if i == 0:
        a = 1
    else:
        a = -1
    if len(lst) == 1:
        return [a * float(lst[0]), 0]
    else:
        for j in lst:
            if is_in(j, 'X'):
                if len(j) == 1:
                    pow = 1
                else:
                    pow = int(j[2])
            else:
                nbr = float(j)
    return [a * nbr, pow]


def tab_to_poly(t):
    tab = [0, 0, 0]
    if i[0] > 2 or i[0] < 0:
        print("Wrong input")
        exit()
    for i in t:
        tab[i[1]] += i[0]
    if tab[1] == 0 and tab[2] == 0:
        print("This is not an equation")
        exit()
    print ("Reduced form of the equation : {} {:+} * X{:+} * X^2 = 0".format(tab[0], tab[1], tab[2]))
    return tab


def resolve(tab):
    D = pow_int(tab[1], 2) - 4 * tab[2] * tab[0]
    im = 0
    print("The discriminant is : ", D)
    if D < 0:
        print("Solutions aren't real, would you like to see imaginary solutions ? (y) or (n)")
        while 1:
            t = str(input())
            if t == "y":
                im = 1
                D *= -1
                break
            elif t == "n":
                print("No real solution found")
                exit()
            else:
                print("Please, enter y or n")
    if tab[2] == 0:
        print("this is a degree 1 equation")
        print("The solution of this equation is {}".format(-tab[0]/tab[1]))
    else:
        print("this is a degree 2 equation")
        delta = my_sqrt(D, 0.0000000001) / (2 * tab[2])
        res = -tab[1] / (2 * tab[2])
        if im == 1:
            print("The imaginary solutions of this equation are {0} + i * {1:-} and {0} - i * {1:-}".format(res, delta))
        elif delta == 0:
            print("The double solution of this equation is {}".format(res))
        else:
            print("The real solutions of this equation are {} and {}".format(res + delta, res - delta))



def run(lst):
    lst = lst.replace(" ", "")
    lst = lst.replace("-", "+-")
    if not len(lst) == 0 and lst[0] == '+':
        lst = lst.replace("+", "", 1)
    lst = lst.replace("x", "X")
    lst = lst.split("=")
    t = []
    if len(lst) <= 1:
        print(" \'=\' is needed, would you like to add \" = 0\" ? (y) or (n)")
        while 1:
            a = str(input())
            if a == "y":
                lst.append("0")
                break
            elif a == "n":
                print("Wrong input")
                exit()
            else:
                print("Please, enter y or n")
    for i in range(len(lst)):
        lst[i] = lst[i].split("+")
        for j in range(len(lst[i])):
            lst[i][j] = lst[i][j].split("*")
            if handle_arg(lst[i][j]) == 0:
                print("Wrong input")
                exit()
            else:
                t += [arg_to_tab(lst[i][j], i)]
    tab = tab_to_poly(t)
    return resolve(tab)


if __name__ == '__main__':
    print("Write down an equation to solve")
    equation = str(input())
    run(equation)

