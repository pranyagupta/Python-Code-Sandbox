string = input("Enter a word: ")[::-1]
print(string)

string = input("Enter a word: ")
rev_str = string[::-1]
print(rev_str)

rev = ""
for letter in string:
    rev = letter + rev

print(rev)
