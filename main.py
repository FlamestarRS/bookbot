# bookbot

def counter(lowercase_contents):
    character_counts = {}
    for character in lowercase_contents:    # counts how many times each character appears
        if character not in character_counts:   # adds key to dict character_counts
            character_counts[character] = 1
        elif character in character_counts:     # increments value for each appearance
            character_counts[character] += 1
        else:                                   # error detection
            print(character, "not in dict")
    return character_counts


def sort(character_counts):
        sorted_character_counts = dict(sorted(character_counts.items()))    # new dict sorted alphabetically
        for key in sorted_character_counts:
            if key.isalpha():                       # removes non-letter characters
                print(f"The", "'"+key+"'", "character was found", sorted_character_counts[key], "times")
          

def main():
    
    word_count = 0

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        total_words = file_contents.split() # splits book into list of words
        lowercase_contents = file_contents.lower()      # lowercase book for counting characters
        
        for words in total_words:           # counts total number of words
            word_count += 1

    lowercase_data = counter(lowercase_contents)       

    print(f"--- Begin report of books/frankenstein.txt ---")
    print(word_count, "words found in the document")
    report = sort(lowercase_data)
    print("--- End report ---")
    
main()