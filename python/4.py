import re

data = '''1233.00
125 Hardware;! 24.8?;
123 Flowers 93.5
127 Meat 120.90
120 Picture 34.00
124 Gasoline 11.00
123 Photos;! 71.4?;
122 Picture 93.5
132 Tires;! 19.00,?;
129 Stamps 13.6
129 Fruits{} 17.6
129 Market;! 128.00?;
121 Gasoline;! 13.6?;'''


def sanitize(str):
    regex = r"[^0-9A-Za-z\.\s]"
    return re.sub(regex, "", str)


def checkbook_balancing(checkbook):
    strs = checkbook.split("\n")

    money = float(strs.pop(0))
    expense = 0.0

    for sample in strs:
        part = sample.split(' ')

        cost = float(sanitize(part[2]))

        money -= cost
        expense += cost

        print(sanitize(part[0]) + ' ' +
              sanitize(part[1]) + ' ' + str(cost) + ' | Balance ' + str(round(money, 2)))

    print("Total expense " + str(round(expense, 2)))


checkbook_balancing(data)
