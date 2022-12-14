#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic string exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in string2.py.


# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'
def donuts(count):
  # +++your code here+++
  if count <10:
      return 'Number of donuts: ' + str(count)
  else:
      return 'Number of donuts: many'


# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
def both_ends(s):
  # +++my code below+++
  if len(s) < 2:
      return ""
  else:
      f2 = s[:2]  # prints from 0th index to2nd index, 2nd not included
      l2 = s[-2:] #prints from -2 index (starting from -1 which is the last letter
  return f2 + l2  #concatenate and return


# C. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.
def fix_start(s):
  # +++my code here+++
  first_letter = s[0]
  s_wo_first_letter = s[1:]
  s_replaced = s_wo_first_letter.replace(first_letter,'*')
  return first_letter + s_replaced


### D. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
def mix_up(a, b):
# pithiest way, but will fail for repeating pattern further in the string
    return a.replace(a[:2], b[:2]) + " " + b.replace(b[:2], a[:2])

# cleanest way to do it
    new_a = a[:2] + b[2:]
    new_b = b[:2] + a[2:]
    return new_a + " " + new_b
  # +++your code here+++ (inelegant brute force way of doing it)
#  a2_0 = a[0]
 # a2_1 = a[1]
#  b2_0 = b[0]
#  b2_1 = b[1]
 # return b2_0 + b2_1 + a[2:] + " " + a2_0 + a2_1 + b[2:]

  #### using string methods to do the same (risk of other repeating
  # patterns getting replaced as well)
  #a2 = a[:2]
  #b2 = b[:2]
#  a_mod = a.replace(a[:2], b[:2])
#  b_mod = b.replace(b[:2], a[:2])
#  return a_mod + " " + b_mod
#'''

# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
  print ('donuts')
  # Each line calls donuts, compares its result to the expected for that call.
  test(donuts(4), 'Number of donuts: 4')
  test(donuts(9), 'Number of donuts: 9')
  test(donuts(10), 'Number of donuts: many')
  test(donuts(99), 'Number of donuts: many')


  print
  print ('both_ends')
  test(both_ends('spring'), 'spng')
  test(both_ends('Hello'), 'Helo')
  test(both_ends('a'), '')
  test(both_ends('xyz'), 'xyyz')


  print
  print ('fix_start')
  test(fix_start('babble'), 'ba**le')
  test(fix_start('aardvark'), 'a*rdv*rk')
  test(fix_start('google'), 'goo*le')
  test(fix_start('donut'), 'donut')

  print
  print ('mix_up')
  test(mix_up('mix', 'pod'), 'pox mid')
  test(mix_up('dog', 'dinner'), 'dig donner')
  test(mix_up('gnash', 'sport'), 'spash gnort')
  test(mix_up('pezzy', 'firm'), 'fizzy perm')


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
