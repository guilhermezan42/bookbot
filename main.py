import sys
from stats import count_words,count_characters, sort_dictionary

def get_book_text(rel_path):
    with open(rel_path) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book_content = get_book_text(path)
    num_words = count_words(book_content)
    list_of_charts_counts = sort_dictionary(count_characters(book_content))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in list_of_charts_counts:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]} ")
    print("============= END ===============")

main()