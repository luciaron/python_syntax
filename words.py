def print_upper_words(words, letters):
    """Changes strings in a list to all-caps if the strings start with any of the letters in the list"""

    
    for word in words:
        for letter in letters:
           if word.startswith(letter):
               print(word.upper())
