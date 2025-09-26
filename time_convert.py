def time_convert(num):
    if num <= 0:
        return "00:00"
    time = num % 60
    time_2 = int((num - time) / 60)
    if time_2 < 10:
        time_2 = "0" + str(time_2)

    if time < 10:
        time = "0" + str(time)

    return str(time_2) + ":" + str(time)

# def time_convert(num):
#     if num <= 0:
#         return '00:00'
#     return f'{num//60:02}:{num%60:02}'


if __name__ == '__main__':

    x = 970
    print(time_convert(x))