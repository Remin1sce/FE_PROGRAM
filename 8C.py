def remove_duplicates(input_string):

    result = ""
    
    seen_characters = set()
    for char in input_string:
    
        if char not in seen_characters:
            result += char
            seen_characters.add(char)
    
    return result

user_input = input()

if user_input:
    cleaned_string = remove_duplicates(user_input)
    print(cleaned_string)

