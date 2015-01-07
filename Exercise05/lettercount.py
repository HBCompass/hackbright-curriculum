import string

text = open("twain.txt")
graphs = text.read()
text.close

graphs = graphs.lower()

letters = list(string.ascii_lowercase)

letter_count = []

for i in range(len(letters)):
	letter_count.append(i)

for char in graphs:
	if char in letters:
		letter_count[letters.index(char)] += 1

print letter_count