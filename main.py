import os
import sys
from stats import book_word_count, count_char, get_sorted_chars

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Get the book path from command line argument
    book_path = sys.argv[1]

    # Get the book text
    text = get_book_text(book_path)

    # Count words
    num_words = book_word_count(text)

    # Count characters
    char_counts = count_char(text)
    sorted_chars = get_sorted_chars(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")  # Added f-string
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

main()
