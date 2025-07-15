def longest_consec(strarr, k):
    if len(strarr) == 0 or k > len(strarr) or k <=0:
        return ''
    st = ''.join(strarr[:k])
    while len(strarr) >= k:
        strarr = strarr[1:]
        if len(''.join(strarr[:k])) > len(st):
            st = ''.join(strarr[:k])

    return st


if __name__ == '__main__':
    strarr = []
    k = 3
    print(longest_consec(strarr, k))
