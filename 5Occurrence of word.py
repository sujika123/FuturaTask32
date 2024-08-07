#5.Write a program in Python to count the occurrence of a specific  word in a string


# Python program to count the number of occurrence
# of a word in the given string
def countOccurrences(str, word):

	wordslist = list(str.split())
	return wordslist.count(word)


# Driver code
# str = "GeeksforGeeks A computer science portal for geeks "
# word = "portal"

str = input("Enter the string : ")
word = input("Enter the word : ")
print(countOccurrences(str, word))

# This code is contributed by vikkycirus
