def wave(people: str) -> list:
    p_list = []
    if len(people) == 0:
        return p_list
    for i in range(len(people)):
        l = list(people)
        if l[i] == ' ':
            continue
        l[i] = l[i].upper()
        p_list.append(''.join(l))
        print(l)
    return p_list


if __name__ == '__main__':
    p = 'hell o'
    print(wave(p))
