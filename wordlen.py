def word_length(lst):
    length_list = []
    for i in lst:
        length_list.append(len(i))
    print(length_list)

# test_list = ['hey', 'hello', 'from', 'the', 'other', 'side']
word_list = [i for i in input('Enter your words: ').split()]
word_length(word_list)