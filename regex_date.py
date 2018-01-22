import re
filepath = 'dates.txt'


text = []
with open(filepath) as fp:
    text = fp.read()
str1 = ''.join(text)


regex = r"\d{1,2}\/\d{1,2}\/\d{2,4}|\d{1,2}\-\d{1,2}\-\d{2,4}|\d{2}\s[a-z]{3,8}\s\d{4}|\w*.?[\s\d{2}]?,?\s\d{4}"
matches = re.findall(regex, str1)
print(matches)

regex2 = r"[C|c][a-z]*:\s\d{4}"
remove_matches =  re.findall(regex2, ''.join(matches))

for cnt, match in enumerate(remove_matches):
    matches.remove(match)

print(matches)