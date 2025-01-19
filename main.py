

def main():
    word_count = 0
    character_counts = {}

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        total_words = file_contents.split()
        lowercase_contents = file_contents.lower()
        print(f"--- Begin report of books/frankenstein.txt ---")
        for words in total_words:
            word_count += 1
        print(word_count, "words found in the document")

        for character in lowercase_contents:
            if character not in character_counts:
                character_counts[character] = 1
            elif character in character_counts:
                character_counts[character] += 1
            else:
                print(character, "not in dict")

        sorted_character_counts = dict(sorted(character_counts.items()))
        for key in sorted_character_counts:
            if key.isalpha():
                print(f"The", "'"+key+"'", "character was found", sorted_character_counts[key], "times")
            
        return
    
main()