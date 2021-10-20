        # The Goldbach Conjecture
        
def is_prime(a):
    if a <= 1:
        return False
    for i in range(2, int(a**0.5)+1):
        if a%i == 0:
            return False
    return True


def goldbach(n):
    for i in range(1, n//2+1, 2):
        if is_prime(i) and is_prime(n-i):
            return (i, n-i)
    return 2, n-2 # as 2 is the only even prime number



        # Palidrome numbers

def palidrome(a, b):
    for i in range(a, b+1):
        tmp1 = i
        tmp2 = 0
        while i:
            tmp2 = tmp2*10 + i%10
            i//=10
        if tmp1 == tmp2:
            print(tmp1, end=' ')
            
            

        # Suffix Sums

def suffix_sums(a):
    return [sum(a[i:]) for i in range(len(a))]

# print(suffix_sums([float(i) for i in input('b: ').split(' ')]))



        # Cyclic Shift

def cyclic_shift(a, n):
    if len(a) == n:
        return a
    n -= len(a)*(n//len(a))
    for i in range(n):
        a.insert(0, a.pop())

# a = [int(i) for i in input('a: ').split(' ')]
# n = int(input())
# cyclic_shift(a, n)
# for i in a:
#     print(i, end=' ')



        # Tree
        
def tree(a):
    for i in range(1, a+1, 2):
        print(' '*((a-i)//2) +'*'*i + ' '*((a-i)//2))

# a = int(input())
# tree(a)
