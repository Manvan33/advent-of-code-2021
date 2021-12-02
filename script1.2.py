#!/usr/bin/python3
with open("input1") as input:
	lines = input.readlines()
lines = [int(line.strip()) for line in lines]
last_sum = 0
incr = 0
for i in range(len(lines)-2):
	new_sum = lines[i]+lines[i+1]+lines[i+2]
	if i > 1:
		if new_sum > last_sum:
			incr += 1
	last_sum = new_sum
print(incr)
