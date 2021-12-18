            # Unique Email Addresses

def unique(a):
    t = [i.split('@') for i in a]
    print(t)
    st = set()
    for k in t:
        tmp = k[0]
        if '.' in tmp:
            tmp = ''.join(tmp.split('.'))
        if '+' in tmp:
            tmp = tmp[:tmp.index('+')]
        st.add(tmp + '@' + k[1])
    return len(st)


# emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# print(unique(emails))


            # Find and Replace pattern

def find_and_replace(words, pattern):
    c = []
    chr_to_CHR = [chr(ord(i) - 32) for i in pattern]
    print('Base: ', chr_to_CHR)
    for i in words:
        tmp = i
        for j in range(len(chr_to_CHR)):
            tmp = tmp.replace(tmp[j], chr_to_CHR[j]) if chr_to_CHR[j] not in tmp else tmp
        print(tmp)
        if tmp == ''.join(chr_to_CHR):
            c.append(i)
    return c


# w = ["abc","cba","xyx","yxx","yyx"]
# p = "abc"
# print(find_and_replace(w, p))


            # Finding the Users Active Minutes

def active_minutes(l, k):
    answer = [0] * k
    d = dict()
    for x in l:
        i = x[0]
        j = x[1]
        try:
            d[i] += [j]
        except:
            d[i] = [j]
    print(d)
    for i, j in d.items():
        k = len(set(j)) - 1
        answer[k] += 1
    return answer

  
# logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]
# k = 5
# print(active_minutes(logs, k))


            # Jewels and Stones

def j_and_s(jewels, stones):
    c = 0
    for i in stones:
        if i in jewels:
            c += 1
    return c


# jewels = "aA"
# stones = "aAAbbbb"
# print(j_and_s(jewels, stones))


            # Beautiful binary string

def bin_str(b):
    lst = list(b)
    c = 0
    for i in range(len(b)-2):
        if lst[i] == '0' and lst[i+1] == '1' and lst[i+2] == '0':
            c += 1
            lst[i+2] = '1'
    print(c)


# st = input()
# print(bin_str(st))


            # String Power

def pow_of_str(str_, num_):
    if num_ < 0 and str_[:len(str_) // abs(num_)] * abs(num_) == str_:
        return str_[:len(str_) // abs(num_)]
    elif num_ > 0:
        return str_ * num_
    elif num_ == 0:
        return ""
    else:
        return 'undefined'


# s = str(input('Input string'))
# k = int(input('Input number'))
# print(pow_of_str(s, k))
