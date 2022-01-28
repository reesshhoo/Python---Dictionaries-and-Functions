def filter_long_words(lst, n):
    filtered_lst = []
    for i in lst:
        if len(i)>n:
            filtered_lst.append(i)
    
    print(filtered_lst)

# test_list = ['hey', 'hello', 'from', 'the', 'other', 'side', '']
words_list = [i for i in input('Enter your words: ').split()]
num = int(input('Enter the number: '))
filter_long_words(words_list, num)