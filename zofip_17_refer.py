import re
import sys


def extract_numbers(text):
    pattern = r'\[([\d\s,]+)\]'
    matches = re.findall(pattern, text)
    result = []
    for match in matches:
        numbers = match.replace(' ', '').split(',')
        result.extend(map(int, numbers))
    return result

def error(num, numbers):

    missing_numbers = list(set([n for n in range(1, num + 1) if n not in numbers]))
    greater_numbers = list(set([n for n in numbers if n > num]))
    l = missing_numbers + greater_numbers
    if l == []:
        print(0)
    else:
        l.sort()
        for l in l:
            print(l)

text = sys.stdin.read().replace('\n', ' ')

##with open('06.txt', 'r') as file:
##    text = file.read().replace('\n', ' ')

num  = int(text.split()[0])
numbers = extract_numbers(text)
error(num, numbers)