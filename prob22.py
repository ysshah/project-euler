# names.txt is a text file containing over 5,000 first names. Sort it
# by alphabetical order, then for each name, multiply its alphabetical
# position in the list by the sum of the alphabetical position of all
# its characters.
# What is the total of all the name scores in the file?

import csv

nf = open('names.txt','rb')
reader = csv.reader(nf)
names = []
all_scores = []

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for n in reader:
	for i in range(len(n)):
		names.append(n[i])

names.sort()

for idx, a_name in enumerate(names):
	alpha_score = 0
	final_score = 0
	for c in a_name:
		alpha_score += alpha.index(c) + 1
	final_score = alpha_score * (idx + 1)
	all_scores.append(final_score)

print sum(all_scores)