#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys
import operator

def print_words(filename):
    #learnings: Sorting a dict using sorted returns a list type (with the key value pair inside as tuples)
    #the print function works below because while I iterate over the sorted list with word (string) as the iterable,
    #the word_count_dict[word] is actualy calling the dict with the word key
    word_count_dict = word_count(filename)
    print(type(sorted(word_count_dict)))
    print(type(word_count_dict))
    for word in sorted(word_count_dict.items()): #.items() method returns the key value pair of the dict as a list tuples
        print(type(word), word, word_count_dict[word])
        #print (type(word), word[0], word[1]) #to prove the above
    return 0

def get_count(word_count_tuple):
    return word_count_tuple[1]

def print_top(filename):
    ### both codes below are equivalent - one users item getter method (needs import operator) and the other uses a lambda function
    #itemgetter(0) will fetch the key and itemgetter(1) fetches the value associated with the key...
    #both together is a tuple and the sorted dict is a list of tuples
    word_count_dict = word_count(filename)
    sorted_dict = sorted(word_count_dict.items(), key=operator.itemgetter(1), reverse = True)
    print (type(sorted_dict))
    print(type(word_count_dict))
    for item in sorted_dict[:20]:
        print(type(item), item[0], item[1])
    # the below is equivalent using the lambda function
    #which then is used to fetch the value from the tuple of key and value and then sort the list in reverse order
    word_count_dict = word_count(filename)
    sorted_dict1 = sorted(word_count_dict.items(), key=lambda fetch_value:fetch_value[1], reverse = True)
    print (type(sorted_dict1))
    print(type(word_count_dict))
    for item in sorted_dict1[:20]:
        print(type(item), item[0], item[1])

    if sorted_dict == sorted_dict1:
        print ("the methods are equivalent")
    return 0


def word_count(filename): #utility function to build a count dict

    word_count = {} # dictionary
    input_file = open(filename, 'r')
    for line in input_file: #read the input file line by line
        words = line.split()  #no splitter called makes it use space by default
        for word in words:
            word = word.lower()
            if not word in word_count:
                word_count[word] = 1
            else:
                word_count[word] = word_count[word] + 1

    input_file.close()  # Not strictly required, but good form.
    return word_count





# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print ('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print ('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
