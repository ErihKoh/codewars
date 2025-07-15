def find_outlier(integers):
    even_numbers = []
    odd_numbers = []
    for i in integers:
        if i % 2 == 0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)

    if len(even_numbers) == 1:
        return even_numbers[0]

    return odd_numbers[0]


def find_outlier_1(int):
    odds = [x for x in int if x % 2 != 0]
    evens = [x for x in int if x % 2 == 0]
    return odds[0] if len(odds) < len(evens) else evens[0]


if __name__ == '__main__':
    integers = [2, 4, 0, 100, 4, 11, 2602, 36]
    print(find_outlier(integers))
