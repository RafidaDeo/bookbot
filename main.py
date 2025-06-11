import sys

from stats import character_count, count_words, chars_dict_to_sorted_list

args = sys.argv

def main():
    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        with open(args[1]) as f:
            file_contents = f.read()
        word_count = count_words(file_contents)
        chars_dictionary = character_count(file_contents)
        chars_sorted_list = chars_dict_to_sorted_list(chars_dictionary)
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {args[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for item in chars_sorted_list:
            if not item["char"].isalpha():
                continue
            print(f"{item['char']}: {item['num']}")
        
        print("============= END ===============")

main()