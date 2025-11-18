# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items):
    return items["num"]

def sorted_list(dictionary):
    character_count_list = [{"char": k, "num": v} for k, v in dictionary.items()]
    character_count_list.sort(key=sort_on, reverse=True)
    return character_count_list

def get_book_charactercount(book_text):
    characters = [char for char in book_text.lower()]
    character_dict = {}
    for char in characters:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict

def get_book_wordcount(book_text):
    words = book_text.split()
    word_count = len(words)
    return word_count

