def vowel_recognizer(char):
    if len(char)==1:
        if char in ['a','e','i','o','u']:
            return True
        else:
            return False
    else:
        return False

input_string = input('Enter your String: ')

vowel_recognizer(input_string)
