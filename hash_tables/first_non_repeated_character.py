def find_first_non_repeated_char(input_string):
    input_string = input_string.lower()
    char_dict = {}
    for item in input_string:
        count = char_dict[item] if item in char_dict.keys() else 0
        char_dict[item] = count + 1

    for item in input_string:
        if char_dict[item] == 1:
            return item


if __name__ == "__main__":
    input_string = "Python is awesome"
    char = find_first_non_repeated_char(input_string)
    print(char)
