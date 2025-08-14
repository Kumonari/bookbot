def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_characters(text):
    character_count_dict = {}
    character_list = list(text.lower())
    
    for character in character_list:
        if character in character_count_dict:
            character_count_dict[character] += 1
        
        else:
            character_count_dict[character] = 1

    return character_count_dict


# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items):
    return items["num"]


def sort_character_count_dict(dictionary):
    sorted_dict_list = []
    
    for character in dictionary:
        character_count = dictionary[character]
        sorted_dict_list.append({"char": character , "num": character_count})

    sorted_dict_list.sort(reverse=True, key=sort_on)
    
    return sorted_dict_list 
