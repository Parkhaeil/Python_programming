#chatgpt사용해서 일부 풀었습니다.

import re
import sys

s_markers = sys.stdin.readline().split()
e_markers = sys.stdin.readline().split()

r_s = "|".join(s_markers)
r_e = "|".join(e_markers)
r = "({0}).*?({1})".format(r_s, r_e)
checker = re.compile(r)

with open("genome.txt", 'r') as file:
    dna = file.read().replace("\n","")

result = "None"

while dna:
    match = checker.search(dna)
    if not match : break
    group = match.group()
    dna = dna[match.start()+1:]
    if result == "None" : result = group
    elif len(result) > len(group) : result = group
    elif len(result) < len(group) : continue
    elif result > group : result = group

print(result)