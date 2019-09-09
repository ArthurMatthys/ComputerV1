import sys


def my_sqrt(nb):
    a = 0
    b = nb
    while b - a < 0.00001:
        mid = (a + b) / 2
        if mid * mid < nb:
            b = mid
        else:
            a = mid
    return b


def degree(a,b,c):
    if a == 0 and b == 0:
        return 0
    elif a == 0:
        return 1
    else:
        return 2


def discriminant(a,b,c):
    return b*b - 4*a*c


def get_coeff(side):
    a, b, c = 0, 0, 0
    for coeff in side:
        if coeff == "":
            continue
        digit, power = coeff.split("*")
        power = float(power.split("^")[1])
        if power == 0:
            c += float(digit)
        elif power == 1:
            b += float(digit)
        elif power == 2:
            a += float(digit)
        else:
            sys.exit("Wrong power")
    return(a, b, c)


def print_reduc(a, b, c):
    print("The reduced form is : {} * X^2 + {} * X^1 + {} = 0".format(a, b, c))


def easy_solv(a,b,c):
    if c == 0:
        print("R")
    else:
        print("There is no solution")
    sys.exit()


def linear_solv(a,b,c):
    print("The solution is : ", -c/b)
    sys.exit()

def run(equation):
    a = 0
    b = 0
    c = 0
    equation = equation.replace(" ", "").replace("-", "+-").split("=")
    parts = [equation[i].split("+") for i in range(len(equation))]
    if len(parts) != 2:
        print("Input not valid")
        return
    for index, side in enumerate(parts):
        aN, bN, cN = get_coeff(side)
        if index == 0:
            a += aN
            b += bN
            c += cN
        else:
            a -= aN
            b -= bN
            c -= cN
    print_reduc(a,b,c)
    deg = degree(a,b,c)
    print("Polynomial degree : {}".format(degree(a,b,c)))
    if deg == 0:
        easy_solv(a,b,c)
    elif deg == 1:
        linear_solv(a,b,c)
    else:
        second_degree_solv(a,b,c)


if __name__== "__main__":
    print("Write down an equation : ", end="")
    equation = str(input())
    run(equation)
