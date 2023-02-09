#Display all duplicate items from a list
#Given: sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]

import collections

sample = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
duplicates = []

for item, count in collections.Counter(sample).items():
	if count > 1:
		duplicates.append(item)
print (duplicates)
