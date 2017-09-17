import sys

word = list(raw_input())
for i in range(len(word)-1, -1, -1):
    sys.stdout.write(word[i])
print
