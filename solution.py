def palindrome(string):
	new_str = ""
	for i in string:
		if i.isalnum():
			new_str += (i)
	return new_str.lower()[::-1] == new_str.lower()