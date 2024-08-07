#2.Write a program to check whether the given word is vowel or consonant.


def check_vowels_consonants(word):
    # Define vowels
    vowels = 'aeiouAEIOU'

    # Initialize flags
    has_vowel = False
    has_consonant = False

    # Check each character in the word
    for char in word:
        if char.isalpha():  # Check only alphabetic characters
            if char in vowels:
                has_vowel = True
            else:
                has_consonant = True

    # Determine the result
    if has_vowel and not has_consonant:
        return "The word contains only vowels."
    elif has_consonant and not has_vowel:
        return "The word contains only consonants."
    elif has_vowel and has_consonant:
        return "The word contains both vowels and consonants."
    else:
        return "The word does not contain any alphabetic characters."


# Example usage:
word = input("Enter a word: ")
result = check_vowels_consonants(word)
print(result)
