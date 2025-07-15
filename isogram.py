def is_isogram(s: str):
    set_s = set(s.lower())
    return len(s) == len(set_s)


if __name__ == '__main__':
    s = 'moOse'
    print(is_isogram(s))
