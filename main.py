import sys
from stats import no_of_words, count_characters, sort_count_char

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    print(f"Processing book at: {book_path}")
    book_text =  get_book_text(book_path)
    # print(book_text)
    count = no_of_words(book_text)
    # print(f"{count} words found in the document")
    char_count = count_characters(book_text)
    # print(char_count)
    sorted_list = sort_count_char(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for j in sorted_list:
        if j['char'].isalpha():
            print(f"{j['char']}: {j['num']}") 
        else:
            pass
    print("============= END ===============")
      
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

main()