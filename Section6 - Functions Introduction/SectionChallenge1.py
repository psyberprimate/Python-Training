def multiply(x: float, y: float) -> float:
    """_summary_

    Multiply 2 numbers with each other
    Args:
        x (_type_): _description_   first number to multiply x
        y (_type_): _description_   second number to multiply y

    Returns:
        _type_: _description_   The product of x and y
    """    
    result = x * y
    return result

def palindrome_sentence(string: str) -> bool:
    """_summary_
    Check if a sentence is a palindrome
    Args:
        string (_type_): _description_  Sentence to check

    Returns:
        _type_: _description_   Return True or False depending if sentence is a palindrome
    """    

    #string_palindrome = "".join(string.split())
    char_list = []
    for character in string:
        if character.isalnum():
            char_list += character
    string = "".join(char_list)
    return is_palindrome(string)

    #or option 2
    # string_chars = ""
    # for char in string:
    #     if char.isalpnu():
    #         string +=char
    # return is_palindrome(string)


def is_palindrome(string: str) -> bool:
    """_summary_
    Check if a string is a palindrome
    Args:
        string (_type_): _description_  The string to check

    Returns:
        _type_: _description_   True if 'string' is a palindrome, False otherwise
    """    
    return string.casefold()[::-1] == string.casefold()


""" word = input("Please enter a word to check: ")
if is_palindrome(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word)) """

while True:
    print("="*40)
    sentence = input("Please enter a sentece to check whatever its a palindrome or not. Write '0' to quit: ")
    if sentence == "0":
        break
    else:
        #print(palindrome_sentence(sentence))
        if palindrome_sentence(sentence):
            print("'{}' sentence is a palindrome".format(sentence))  
        else:
            print("'{}' sentence is not a palindrome".format(sentence))
