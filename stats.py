def count_char(string):
    counts = {}
    for char in string:  
        char = char.lower()  # Convert to lowercase
        counts[char] = counts.get(char, 0) + 1  # Count the character
    return counts  # Return the resulting dictionary

def book_word_count(string):
    words = string.split()
    return len(words) - 1 # Example: Simple word count based on splitting string

def sort_on(dict):
    return dict["count"]

def get_sorted_chars(counts):
    chars_list = []

    for char, count in counts.items():
        char_dict = {"char": char, "count": count}
        chars_list.append(char_dict)
   
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
    


