def array_diff(a, b):
    b_set = set(b)
    return [x for x in a if x not in b_set]


if __name__ == '__main__':
    a = [3, 11, 1, 8, 4, -9, -20, 14]
    b = [12, -20, 4, -16, 18, -16, -18, -13, -7, 15, 8, 8, -6, -17, -6, 17, 20, 9]
    print(array_diff(a, b))
