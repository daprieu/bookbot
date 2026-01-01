def get_word_count(text):
    words = text.split()
    return len(words)

# takes the text from the book as a string, and returns the number of times each character, (including symbols and spaces), appears in the string.
# Convert any character to lowercase using the .lower() method, we don't want duplicates.
# Use a dictionary of String -> Integer. 
def count_characters(text):
    char_count = {}
    for char in text.lower():
        if not char.isalpha():
            continue
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


# Sort the dictionary by character
# takes the dictionary of characters and their counts and returns a sorted list of dictionaries.
# Each dictionary should have two key-value pairs: one for the character itself and one for that character's count (e.g. {"char": "b", "num": 4868}).
# Use the .sort() method:
# Use a helper function to return the "num" key of each dictionary for comparison.
# Sort the list from greatest to least by the count.
def sort_character_counts(char_count):
    char_count_list = []
    for char, count in char_count.items():
        char_count_list.append({"char": char, "num": count})
    
    def get_count(item):
        return item["num"]
    
    char_count_list.sort(key=get_count, reverse=True)
    return char_count_list