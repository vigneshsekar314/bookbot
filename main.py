def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print_char_report(file_contents)

def word_count(full_text: str) -> int:
    return len(full_text.split())

def char_dictionary(full_text: str):
    char_dict = {}
    full_text_copy = full_text.lower()
    for i in full_text_copy:
        if i in char_dict:
            char_dict[i] = char_dict[i] + 1
        else:
            char_dict[i] = 1
    return char_dict

def sort_on(dict_of_char):
    return dict_of_char["num"]

def get_char_list(c_dict):
    new_list = []
    for (key, value) in c_dict.items():
        if key.isalpha():
            new_list.append({"key": key, "num": value})
    return new_list

def print_char_report(full_text):
    char_dict = char_dictionary(full_text)
    ch_lst = get_char_list(char_dict)
    ch_lst.sort(reverse=True, key=sort_on)
    # begin report
    print("--- Begin report of books/frankenstein.txt ---")
    print (f"{word_count(full_text)} words found in the document\n")
    for cdict in ch_lst:
            if cdict["key"].isalpha():
                ckey, ccount = cdict["key"], cdict["num"]
                print(f"The '{ckey}' character was found {ccount} times")
    print("--- End report ---")

main()