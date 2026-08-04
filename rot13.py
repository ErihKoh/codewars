def rot13(text):
    result = ""

    for ch in text:
        # Великі літери
        if 'A' <= ch <= 'Z':
            result += chr((ord(ch) - ord('A') + 13) % 26 + ord('A'))

        # Малі літери
        elif 'a' <= ch <= 'z':
            result += chr((ord(ch) - ord('a') + 13) % 26 + ord('a'))

        # Усе інше залишаємо без змін
        else:
            result += ch

    return result


print(rot13("EBG13 rknzcyr."))
print(rot13("This is my first ROT13 excercise!"))

if __name__ == '__main__':
    joke = 'EBG13 rknzcyr.'

    print(rot13(joke))
