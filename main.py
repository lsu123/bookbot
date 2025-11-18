from stats import get_book_wordcount
from stats import get_book_charactercount
from stats import sorted_list
import sys

def get_book_text(filepath):
    return open(filepath, 'r').read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    #filepath = 'books/frankenstein.txt'
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    character_dict = get_book_charactercount(book_text)
    characters_sorted = sorted_list(character_dict)
    #characters_sorted = sorted(characters_sorted.items, reverse=True, key=sort_on)
    #print(f'Found {get_book_wordcount(book_text)} total words')
    print(f'============ BOOKBOT ============')
    print(f'Analyzing book found at {filepath}...')
    print(f'----------- Word Count ----------')
    print(f'Found {get_book_wordcount(book_text)} total words')
    print(f'--------- Character Count -------')
    for item in characters_sorted:
        if item["char"].isalpha():
            print(f'{item["char"]}: {item["num"]}')
    print(f'============= END ===============')



# Using the special variable 
# __name__
if __name__=="__main__":
    main()