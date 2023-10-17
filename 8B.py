def remove_non_letters(input_string):
    result = ""
    for char in input_string:

        if char.isalpha():
            
            result += char
    
    return result

user_input = input()

if user_input:
    cleaned_string = remove_non_letters(user_input)
    print(cleaned_string)
else:
    print("Input string is empty. Please enter a non-empty string.")
