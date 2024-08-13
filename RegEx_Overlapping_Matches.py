'''
findall() work great if there are no overlapping matches. If there are overlapping matches, the regex engine will just ignore
them because it “consumes” the whole matching substrings and starts matching the next pattern only after the stop index of the
previous match.
The idea is to keep track of the start position in the previous match and increment it by one after each match:
'''
import re

pattern = '99'
text = '999 ways of writing 99 - 99999'
left = 0
count = 0
while True:
    match = re.search(pattern, text[left:])
    if not match:
        break
    count += 1
    left += match.start() + 1

print(f'Found {count} matches')

# lookahead assertion
# formate: (?=...)
text = "AAAA"
pattern = "(?=(AA))"

x = re.findall(pattern, text)
print(x)
print(f'Found {len(x)} times')
