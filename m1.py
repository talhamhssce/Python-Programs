#packages or modules:
#There are 2 types of packages
# build in packages
# user defined packages


# you have a file name as demo.txt which has some content in it. 
# how many word are there in that file and 
# how many unique words are there in that and how many word are starting with 'a'

# import os 

# f = open("demo.txt", "r")

# str = f.read()
# f.close

f = open("demo.txt", "r")
words = f.read().split()
print(words)

#task 1 print word word
print("number of words in a file are:", len(words))

#task 2 print unique word
unique_words = set(words)
print("unique words in a file are", unique_words)
print("number of unique word in a file", len(unique_words))

#task 3 word starting with 'a' or 'A
words_with_a = []
for word in unique_words:
    if words[0].lower() == 'a':
        words_with_a.append(word)
print('Words starting with\'a\' or \'A\' are:', words_with_a)
print("Numbers of word starting with \'a\' or \'A\' are :", words_with_a)        

