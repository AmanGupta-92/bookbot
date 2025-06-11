def no_of_words(book_text):
    count = 0
    words = book_text.split()
    return len(words)

def count_characters(book_text):
    char_dict = {}
    for i in list(book_text):
        i_lower = i.lower()
        if i_lower in char_dict:
            char_dict[i_lower] += 1
        else:
            char_dict[i_lower] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def sort_count_char(char_dict):
    char_count_list = []
    
    for i in char_dict:       
        num_dict = dict(char=i, num=char_dict[i])
        char_count_list.append(num_dict)
    
    char_count_list.sort(reverse=True, key=sort_on)
    return char_count_list