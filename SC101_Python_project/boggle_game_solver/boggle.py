"""
File: boggle.py
Name: Leo
----------------------------------------
Generate words by boggle game
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	Generate words by boggle game
	"""
	start = time.time()
	boggle = []
	for index, char_list in enumerate(range(4)):
		chars = input(f'{index+1} row of letters: ')
		char_list = chars.lower().split(' ')
		if check_valid_char_list(char_list):
			boggle.append(char_list)
		else:
			print('Illegal input')
			break
	find_word(boggle)
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def check_valid_char_list(char_list):
	"""
	:param char_list: input char list
	:return: check char list legal or not
	"""
	for char in char_list:
		if len(char) != 1:
			return False
		elif len(char_list) != 4:
			return False
	return True


def find_word(boggle):
	"""
	:param boggle: boggle list to iter words
	:return: None, only print out result
	"""
	found_list = []
	prefix_dict = {}
	for x in range(4):
		for y in range(4):
			pre_word = [(x, y), (x, y)]
			find_word_helper(boggle, x, y, boggle[x][y], pre_word, found_list, prefix_dict)
	print(f'There are {len(found_list)} words in total')


def find_word_helper(boggle, x, y, current_s, pre_word, found_list, prefix_dict):
	"""
	:param boggle: boggle list to find words
	:param x: x coordinate to of boggle char
	:param y: y coordinate to of boggle char
	:param current_s: current recursive string
	:param pre_word: list to record iterate path coordinate
	:param found_list: the list contains all word anagrams
	:param prefix_dict: the dictionary records the prefix be used to search has_prefix
	"""
	if len(current_s) >= 4:
		if current_s not in found_list and current_s in read_dictionary():
			print(f'Found: "{current_s}"')
			found_list.append(current_s)
	iter_list = []
	for i in range(-1, 2):
		for j in range(-1, 2):
			if i == 0 and j == 0:
				pass
			elif (i, j) in iter_list:
				pass
			else:
				neighbor_x = x + i
				neighbor_y = y + j
				iter_list.append((i, j))
				if 4 > neighbor_x >= 0 and 4 > neighbor_y >= 0 and (neighbor_x, neighbor_y) != pre_word[-2]:
					current_s += boggle[neighbor_x][neighbor_y]
					pre_word.append((neighbor_x, neighbor_y))
					if prefix_dict.get(current_s) is False:
						pass
					elif has_prefix(current_s):
						find_word_helper(boggle, neighbor_x, neighbor_y, current_s, pre_word, found_list, prefix_dict)
						prefix_dict[current_s] = True
					else:
						prefix_dict[current_s] = False
					current_s = current_s[:-1]
					pre_word.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dictionary_list = []
	with open(FILE, 'r') as f:
		for line in f:
			word = line.rstrip()
			dictionary_list.append(word)
	return dictionary_list


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in read_dictionary():
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
