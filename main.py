import sys
from stats import get_num_words
from stats import get_num_characters
from stats import sort_character_count_dict


def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    sorted_characters = sort_character_count_dict(num_characters)

    header_text = f"============ BOOKBOT ============\nAnalyzing book found at {book_path}..."
    word_count_text = f"----------- Word Count ----------\nFound {num_words} total words"
    character_count_header = "--------- Character Count -------"
    ending_text = "============= END ==============="

    print(header_text)
    print(word_count_text)
    print(character_count_header)
    
    for entry in sorted_characters:
        if entry["char"] and entry["num"]:
            char_string = str(entry["char"])

            if char_string.isalpha():
                print(f"{char_string}: " + str(entry["num"]))

            else:
                continue

        else:
            print("failed to get character data")

    print(ending_text)


def get_book_text(path):
    with open(path) as file:
        return file.read()


main()

