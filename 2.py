symbol = "*"
separator = " "


def string_diamond(size):
    if (size < 0):
        return False

    for i in range(size):
        before = int(size - i) * separator
        current = symbol * (2 * i - 1)
        line = before + current
        print(line)

    for i in range(size):
        i = size - i
        before = int(size - i) * separator
        current = symbol * (2 * i - 1)
        line = before + current
        print(line)


string_diamond(9)
