# bookbot
import sys
from stats import counter


def sort(character_counts):
        sorted_character_counts = dict(sorted(character_counts.items()))    # new dict sorted alphabetically
        for key in sorted_character_counts:
            if key.isalpha():                       # removes non-letter characters
                print(f"The", key+":", sorted_character_counts[key], "times")
          

def main():
    
    word_count = 0
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    with open(sys.argv[1]) as f:

        file_contents = f.read()
        total_words = file_contents.split() # splits book into list of words
        lowercase_contents = file_contents.lower()      # lowercase book for counting characters
        
        for words in total_words:           # counts total number of words
            word_count += 1

    lowercase_data = counter(lowercase_contents)       

    print(f"--- Begin report of {sys.argv[1]} ---")
    print(word_count, "words found in the document")
    report = sort(lowercase_data)
    print("--- End report ---")
    
main()