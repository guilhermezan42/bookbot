def count_words(book_content):
    splitted_book_list = book_content.split()
    count = 0
    for item in splitted_book_list:
        count += 1
    return count

def count_characters(book_content):
    dict = {}
    lower_book_content = book_content.lower()
    for character in lower_book_content:
        if character not in dict:
            dict[character] = 1
            continue
        if dict[character] >= 1:
            dict[character] += 1
    return dict
"""
fazer um dict que possui todas as letras que apareceram e a contagem 
"""

def sort_dictionary(dict):
    new_list = []
    for key in dict: 
        pair = {"char": key, "num" : dict[key]}
        new_list.append(pair)
        # print(pair)
    # print(f" list: {new_list}")
    def helper_function(dict):
        return dict["num"]
    new_list.sort(key=helper_function,reverse=True)
    return new_list
    
 