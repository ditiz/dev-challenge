def get_format_number(array_number):
    string_num = ''

    new = 0
    for num in array_number:
        if new == 2:
            string_num = string_num + ' '
            new = 0
        string_num = string_num + str(num)
        new += 1

    return string_num


num = (0, 6, 1, 2, 3, 4, 5, 6, 7, 8)
print(get_format_number(num))
