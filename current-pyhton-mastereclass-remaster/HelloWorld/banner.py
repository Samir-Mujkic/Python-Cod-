def is_palindrome_sentence(sentence):
    """

    :param sentence:
    :return:
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return is_palindrome_sentence(string)