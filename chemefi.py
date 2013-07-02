'''chemefi.py

dumps list of metafilter usernames containing as a whole word the name of
a chemical element
'''

from json import load
from re import compile

with open('elements.json') as elementsfile: elementsdict = load(elementsfile)

elements = [key.lower() for key in elementsdict]

with open('usernames.txt') as usernamesfile:
    usernames = [line.split('\t')[2].strip().lower()
                 for line
                 in usernamesfile.readlines()[2:]]

res = [compile('\\b%s\\b' % element) for element in elements]

matches = [username for username in usernames
           if any([re.match(username) for re in res])]

with open('out.txt', 'w') as outfile:
    outfile.write('\n'.join(matches))