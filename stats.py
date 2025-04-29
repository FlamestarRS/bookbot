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
