#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++my code here+++
  f = open(filename, 'r')
  babynames = f.read()

  match_year = re.search(r'Popularity in \d\d\d\d', babynames)
  year = match_year.group()[-4:]
  baby_names_rank = re.findall(r'(\d+)</td><td>\w+</td><td>(\w+)</td>', babynames)
  #creates a list of tuples of rank, (last name - remove paranthesis to get the last name removed)
  #and first name for all repetitions of the pattern by inserting the paranthesis around the groups i want

  rank_first_name = []
  rank_first_name.append(year)
  rank_name_dict = {} #dict

  for baby in baby_names_rank:
      rank_name_dict[baby[1]] = baby[0] #name is key, rank is value for this dict

  sorted_dict_rank_name = dict(sorted(rank_name_dict.items())) #sort the dict

  for key in sorted_dict_rank_name:
      rank_first_name.append(key + " " + sorted_dict_rank_name[key])

  return rank_first_name


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print ('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]


  summary_baby_names = open(r'./SummaryBabyNames.txt', 'w')

  for babynames_file in args:
      names = extract_names(babynames_file)

      text = '\n'.join(names) #make a text out of the list

      if summary:
          outf = open(babynames_file + '.summary', 'w')
          outf.write(text)
          outf.close()
      else:
          print(text)

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file

if __name__ == '__main__':
  main()
