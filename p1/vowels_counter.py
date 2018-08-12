#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

def main():
	"""kk"""
	str_ = raw_input()
	# the input string is in s
	# remove pass and start your code her
	count_ = 0
    for letter_ in str_:
        if letter_ in ('a', 'e', 'i', 'o', 'u'):
		    count_ += 1
    print(count_)
if __name__== "__main__":
	main()
