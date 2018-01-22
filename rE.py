import re
from datetime import datetime

text = open("dates.txt")

match=re.search(r'(\d+/\d+/\d+)','The date is 11/12/98')

patn = re.compile(r'\d{2} \d{2} \d{4}')
for line in text:
    for match in patn.findall(line):


