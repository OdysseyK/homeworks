# Homework 1

# Digit Sum 3


def digit_sum_3(i):
    return i%10 + i//10%10 + i//100

# Area of a right triangle


def area(a, b):
    return a*b/2

# Arithmetic Progression


def progression(a1, a2, n):
    return a1 + (n-1)(a2-a1)

# Century from year


def century_from_year(year):
    return (year-1)//100 + 1

# Two men


def two_men(first, second):
    return f'{second - 1}\n{first - 1}'

# Knight's Possible Moves

def check_moves(x, y):
    moves = ((2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2))
    for i in moves:
        print(x + i[0], y + i[1])

check_moves(6, 4)
