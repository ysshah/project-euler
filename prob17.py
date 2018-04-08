# If all the numbers from 1 to 1000 (one thousand) inclusive were 
# written out in words, how many letters would be used?

import math

ones_and_teens = [
	('zero',0),
	('one',3),
	('two',3),
	('three',5),
	('four',4),
	('five',4),
	('six',3),
	('seven',5),
	('eight',5),
	('nine',4),
	('ten',3),
	('eleven',6),
	('twelve',6),
	('thirteen',8),
	('fourteen',8),
	('fifteen',7),
	('sixteen',7),
	('seventeen',9),
	('eighteen',8),
	('nineteen',8)]

tens = [
	('zero',0),
	('ten',3),
	('twenty',6),
	('thirty',6),
	('forty',5),
	('fifty',5),
	('sixty',5),
	('seventy',7),
	('eighty',6),
	('ninety',6)]

words = {
	'thousand' : 8,
	'hundred' : 7,
	'and' : 3,}

def print_output(i,this_sum,letter_sum,ones_digit,tens_digit,hundreds_digit):
	hundreds_str = ones_and_teens[hundreds_digit][0]+' hundred'
	tens_str = tens[tens_digit][0]
	ones_str = ones_and_teens[ones_digit][0]
	if i > 99:
		if i % 100 == 0:
			num_str = hundreds_str
		else:
			if tens_digit > 1:
				if ones_digit == 0:
					num_str = hundreds_str+' and '+tens_str
				else:
					num_str = hundreds_str+' and '+tens_str+'-'+ones_str
			else:
				num_str = (hundreds_str+' and '+
					ones_and_teens[tens_digit*10+ones_digit][0])
	elif i > 19:
		if i % 10 == 0:
			num_str = tens[tens_digit][0]
		else:
			num_str = tens[tens_digit][0]+'-'+ones_and_teens[ones_digit][0]
	else:
		num_str = ones_and_teens[i][0]
	print '%4s %40s %7s %10s' % (i, num_str, this_sum, letter_sum)

def sum_it_up(i,letter_sum,ones_digit,tens_digit,hundreds_digit):
	hundreds_val = ones_and_teens[hundreds_digit][1]+words['hundred']
	tens_val = tens[tens_digit][1]
	ones_val = ones_and_teens[ones_digit][1]
	if i > 99:
		if i % 100 == 0:
			this_sum = hundreds_val
		else:
			if tens_digit > 1:
				if ones_digit == 0:
					this_sum = hundreds_val+words['and']+tens_val
				else:
					this_sum = hundreds_val+words['and']+tens_val+ones_val
			else:
				this_sum = (hundreds_val+words['and']+
					ones_and_teens[tens_digit*10+ones_digit][1])
	elif i > 19:
		if i % 10 == 0:
			this_sum = tens_val
		else:
			this_sum = tens_val+ones_val
	else:
		this_sum = ones_and_teens[i][1]
	return this_sum

def sum_letters(i):
	letter_sum = 0
	while i > 0:
		hundreds_digit = int(math.floor(i/100))
		tens_digit = int(math.floor((i - (hundreds_digit*100))/10))
		ones_digit = i - (hundreds_digit*100) - (tens_digit*10)

		this_sum = sum_it_up(i, letter_sum, ones_digit, tens_digit, 
			hundreds_digit)
		letter_sum += this_sum

		print_output(i, this_sum, letter_sum, ones_digit, tens_digit, 
			hundreds_digit)
		i -= 1
	return letter_sum

