# Digit Product

def digit_product(a):
    prod = 1
    while a != 0:
        dig = a % 10
        if dig != 0:
            prod *= dig
        a //= 10
    return prod


# Largest Power Of 3

def pow_of_3(a):
    power = 1
    while power <= a:
        power *= 3
    return power // 3


# Triangle

def triangle(a, b, c):
    x = max(a, b, c)
    z = min(a, b, c)
    y = a+b+c-x-z

    if x >= y + z:
        print('No Triangle')
    elif x ** 2 == y ** 2 + z ** 2:
        print('Right Triangle')
    elif x ** 2 > y ** 2 + z ** 2:
        print('Obtuse Triangle')
    else:
        print('Acute Triangle')


# The Root Of The Number

def root(a):
    print(a)
    while a > 10:
        _sum = 0
        while a != 0:
            tmp = a %10
            a //= 10
            _sum += tmp
        print(_sum)
        a = _sum


# Number Of Divisors

def num_of_div(a):
    count = 1
    for i in range(1, a//2+1):
        if a % i == 0:
            count += 1
    return count


# Quadratic Equation

def equation(a, b, c):
    if a == b == c == 0:
        print('Non-Quadratic equation', '\nInfinite Solutions')
        return
    elif a == b == 0:
        print('Non-Quadratic equation', '\nNo Solutions')
        return
    elif a == 0:
        print('Non-Quadratic equation', f'\nOne Solution: {-c / b }')
        return

    d = b * b - 4 * a * c

    if d < 0:
        print('Quadratic equation', f'\nDiscriminant: {d}', '\nNo Solutions')
    elif d == 0:
        print('Quadratic equation', '\nDiscriminant: 0', f'\nOne Solution: {-b / (2 * a)}')
    else:
        print('Quadratic equation', f'\nDiscriminant: {d}', f'\nTwo Solutions: {(-b + d ** 0.5) / 2 * a},'
                                                            f' {(-b - d ** 0.5) / 2 * a}')
