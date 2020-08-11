import re

letterValues = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2,
                'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
                'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1,
                'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}


def get_letter_score(letter):
    regex = r"[^A-Za-z\.\s]"
    if (re.search(regex, letter)):
        return 0

    return int(letterValues.get(letter))


def scrabble_word_value(word):
    score = 0
    word = word.lower()

    for index, letter in enumerate(word, start=0):
        letter_score = get_letter_score(letter)

        # handle double word
        if index + 1 == len(word):
            if letter == "d":
                score = score * 2
                return score
            if letter == 't':
                score = score * 3
                return score

        # handle double and triple letter
        if index+1 < len(word):
            if word[index+1] == '*':
                if index+2 < len(word) and word[index+2] == '*':
                    letter_score = letter_score * 3
                else:
                    letter_score = letter_score * 2
            elif word[index+1] == "^":
                letter_score = 0

        score += letter_score

    if len(word) == 7:
        score = score + 50
    return score


print(scrabble_word_value('sauc*i**sson'))
print(scrabble_word_value('saucisson'))
print(scrabble_word_value('saucissond'))
print(scrabble_word_value('saucissont'))
print(scrabble_word_value('sauc^isson'))
print(scrabble_word_value('toutous'))
