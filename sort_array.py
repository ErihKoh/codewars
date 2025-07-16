# def sort_array(source_array):
#     odd_arr = []
#     for i in range(len(source_array)):
#         if source_array[i] % 2 != 0:
#             odd_arr.append(source_array[i])
#             source_array[i] = 'x'
#     odd_arr.sort()
#     for i in range(len(odd_arr)):
#         for j in range(len(source_array)):
#             if source_array[j] == 'x' and len(odd_arr) > 0:
#                 source_array[j] = odd_arr.pop(0)
#     return source_array


def sort_array(source_array):
    # Копія, щоб не змінювати оригінал
    result = source_array.copy()

    # Знаходимо непарні числа з їх позиціями
    odd_positions = [i for i, x in enumerate(result) if x % 2 != 0]
    odd_values = sorted(result[i] for i in odd_positions)

    # Вставляємо відсортовані непарні числа назад у ті самі позиції
    for idx, val in zip(odd_positions, odd_values):
        result[idx] = val

    return result


if __name__ == '__main__':
    source_array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(sort_array(source_array))
