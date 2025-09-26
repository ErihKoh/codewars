def solution(args):
    result = []
    start = args[0]
    end = args[0]

    for n in args[1:] + [None]:  # додаємо None, щоб обробити останню групу
        if n is not None and n == end + 1:
            end = n
        else:
            if end - start >= 2:  # якщо є діапазон довжиною 3+
                result.append(f"{start}-{end}")
            elif start == end:   # одиничне число
                result.append(str(start))
            else:                # два числа
                result.append(str(start))
                result.append(str(end))
            start = end = n

    return ",".join(result)


if __name__ == "__main__":
    list_1 = [-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
    print(solution(list_1))
