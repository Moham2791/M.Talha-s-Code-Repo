import re
print("Enter the filename you want to extract email from")

fileToRead = input()

file = open(fileToRead, 'r')
fileline = file.readlines()


emails = re.findall(r"[a-z0-9\.\-+]+@[a-z0-9\.\-+]+\.[a-z]+", str(fileline))
print(emails)
