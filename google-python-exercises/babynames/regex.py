import re
import sys
# https://developers.google.com/edu/python/regular-expressions

str = 'piiig'

match = re.search(r'iii', str)

print(str + ' contains ' + match.group())

if match:
    print ('iii found in: ' + str )

else:
    print('iii not found')

## Search for pattern 'iii' in string 'piiig'.
## All of the pattern must match, but it may appear anywhere.
## On success, match.group() is matched text.
match = re.search(r'iii', 'piiig') # found, match.group() == "iii"
match = re.search(r'igs', 'piiig') # not found, match == None

## . = any char but \n
match = re.search(r'..g', 'piiig') # found, match.group() == "iig"

## \d = digit char, \w = word char
match = re.search(r'\d\d\d', 'p123g') # found, match.group() == "123"
match = re.search(r'\w\w\w', '@@abcd!!') # found, match.group() == "abc"



babynames_file = open(sys.argv[1], 'r') #reads the baby1990.html into one big string

#print(type(babynames_file))

babynames = babynames_file.read()
match_year = re.search(r'Popularity in \d\d\d\d', babynames)

print(match_year.group())
year_str = match_year.group()
year = year_str[-4:]
print(type(year))
print(year)
baby_names_rank = re.findall(r'(\d+)</td><td>\w+</td><td>(\w+)</td>', babynames)
#creates a list of tuples of rank, last name and first name for all repetitions of the pattern by
#inserting the paranthesis around the groups i want

#rank_name_tuple = re.search(r'\d*[]', baby_names_rank)
rank_first_name = []
rank_first_name.append(year)
rank_name_dict = {} #dict

for baby in baby_names_rank:
    rank_first_name.append(baby[0] + " " + baby[1])
    rank_name_dict[baby[1]] = baby[0]



#print(baby_names_rank)
#print(type(baby_names_rank))
#print(rank_first_name)
print(rank_name_dict)
#year_name_rank = year + (baby_names_rank)
#print(type(year_name_rank))
