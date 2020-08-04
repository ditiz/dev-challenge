def count_vowel(str):
    count = 0
    vowels = ["a", "e", "i", "o", 'u', 'y']
    for char in str:
        char = char.lower()
        if char in vowels:
            count += 1

    return count


print(count_vowel("I am blob"))
print(count_vowel("This is not a test"))
