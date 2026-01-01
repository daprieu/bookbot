import sys
from stats import get_word_count, count_characters, sort_character_counts

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        raise SystemExit(1)
    path = sys.argv[1]
    book_text = get_book_text(path)

    word_count = get_word_count(book_text)
    char_count = count_characters(book_text)
    sorted_char_count = sort_character_counts(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_char_count:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        # f is a file object
        file_contents = f.read()
    return file_contents


main()