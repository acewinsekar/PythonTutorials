#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.

def remove_adjacent(nums):
  # +++your code here+++
  #no_adjacent = []  #empty list
  i = 1
  if len(nums) <= 1:
      return nums
  while i < len(nums) :
#          print (nums, i, nums[i])
          if nums[i-1] == nums[i]:
              nums.pop(i)
              i -= 1 #reduce index by 1 when you pop so you
                     #stay at the same index for next comparison
#              print(nums, i, nums[i])
          i += 1 #default increment needed
  return nums
'''
  #writing even better than the above as per stack overflow
  def remove_adjacent(seq): # works on any sequence, not just on numbers
    i = 1
    n = len(seq)
    while i < n: # avoid calling len(seq) each time around
        if seq[i] == seq[i-1]:
            del seq[i]
      # value returned by seq.pop(i) is ignored; slower than del seq[i]
            n -= 1 #reduce length of n and keep i at the same value
        else:
            i += 1 # move onto the next
  #### return seq #### don't do this
  # function acts in situ; should follow convention and return None
'''

# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
  # +++your code here+++
 merged = list1 + list2
 merged.sort()
 return merged

'''
  len1 = len(list1)
  len2 = len(list2)
  big_num = 0
  i = 0
  # store the greatest number upto a certain index. and since both
  #lists are sorted, can just append till the big_num is reached
  merged = [] #empty list to append to

for l1, l2 in zip(list1, list2) :

  if list1[0] < list2[0] :
      big_num = list2[0]
  else :
      big_num = list1[0]

if len1 < len2 :
    n = len1
else :
    n = len2

1 2 3 4 5 6
4 7 8 10

  while i <= n:
      while list1[i] <= big_num and list2[] <= big_num:


      if list1[i] <= list2[i]:
          merged.append(list1[i])
          merged.append(list2[i])
      else :
          merged.append(list2[i])
          merged.append(list1[i])
'''

# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
  print ('remove_adjacent')
  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])

  print
  print ('linear_merge')
  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
  main()
