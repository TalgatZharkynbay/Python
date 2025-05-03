# Email
# An N number of lines is entered. You want to find out how many email addresses are written in total in these lines. Assume that only email addresses contain @ (there is no need to check validity of emails).
#
# INPUT FORMAT
# Integer N
# N of strings, each on a new line.
#
# OUTPUT FORMAT
# An integer, the number of emails in the inputted strings.

n = int(input())
count = 0

for i in range(n):
    lines = input()
    count += lines.count('@')
    
print(count)

# Exam results
# The results of the exam are given. Divide the names of students into two lists: those who got an unsatisfactory grade and those who got a passing grade. The grading system of the Higher School of Economics is used (10-point scale, unsatisfactory marks are less than 4).
#
# INPUT FORMAT
# String with the name of students, separated by spaces.
# On a new line, string with the grades for those students, separated by spaces.
# It is guaranteed that the number of grades and students are the same.
#
# OUTPUT FORMAT
# There are two strings in the output, each on a new line.
# The first line contains the names of the students who are retaking the exam, the second line contains the students who passed the exam.
# Students' names are separated by spaces.
# If there are no students for one of the lines (e.g. all students have passed the exam), then the empty string is printed for that row.

names = input().split()
grades = list(map(int, input().split()))

retake = []
passed = []

for i, v in enumerate(names):
    if grades [i] < 4:
        retake.append(v)
    else:
        passed.append(v)
        
print(*retake)
print(*passed)

# Website registration
# To sign up on the website you have to create a password, which would satisfy those rules:
#
# There is at least one letter and one number
# There are no other symbols (only letters and numbers)
# There is at least one capital letter and one lowercase letter
# Write a program that will identify whether the password satisfies those requirements.
#
# INPUT FORMAT
# A string, containing a password
#
# OUTPUT FORMAT
# A string "Password is valid" if it satisfies all requirements, or a string "Password is not valid" if it doesn't. Those strings are saved into the variables for you.

valid = 'Password is valid'
not_valid = 'Password is not valid'

password = input()

if (password.isalnum() == True) & (password.isalpha() == False) & (password.isdigit() == False) & (password.isupper() == False) & (password.islower() == False):
    print(valid)
else:
    print(not_valid)

# Expenditures on lunches
# Vasya is back and he still writes down his lunch expenses for every day of the week. Help Vasya find the cheapest lunch he bought during the weekdays. First five numbers in Vasya's list are expenses from Monday to Friday.
#
# INPUT FORMAT
# A string, containing a list of seven sums (real numbers), divided by a comma and a space
#
# OUTPUT FORMAT
# A float, an answer to the task

sums = list(map(float, input().split(', ')))
print(min(sums[:5]))

# Encrypted message
# Masha and Vasya use encrypted messages to communicate. The rules for encryption are the following: the first two and the last two symbols in a word do not mean anything. Thus, the meaningful word starts with the third letter and end with the third letter from the end.
#
# Spaces are placed in right places. Write a program, that will decrypt these messages.
#
# INPUT FORMAT
# Encrypted message in one string (it is guaranteed that every word contains at least 5 letters)
#
# OUTPUT FORMAT
# Decrypted message as one string

encrypted = input().split()

for i in range(len(encrypted)):
    encrypted[i] = encrypted[i][2:-2]

print(*encrypted)

# Magic wands
# The manager of Ollivander's wand shop checks that the magic wand system is working properly. Selectively, he records information about the wands sold in the form of 
# a list containing the owner's name, the year of purchase, and the material of which the wand is made. The entries are entered until the manager enters 
# the word "End". Sometimes the shopkeeper, Ollivander, wants to check who bought a wand from him in a particular year. If no one 
# bought a wand in the specified year, the phrase is displayed: "No one bought magic wands this year." Otherwise it outputs the string 
# of the required format (see below).
#
# INPUT FORMAT
# Strings like "Owner's first and last name, year, material", each on a new line. Within each string data are separated by a comma and a space.
# Lines are inputted until the string 'End' is entered.
# Then on a new line, an integer, the year in which Ollivander is interested.
#
# OUTPUT FORMAT
# A line like "In XXXX year, the magic wand was bought by:" and then in the specified format (see example) the first and last names of those who bought 
# the magic wand and specifying the material of which it is made. Entries are separated by a comma and a space, the line ends with a dot.
# Hint: don't try to print everything within one f-string, it is possible but rather complicated. Better create first a string with all customers in 
# a specified format joined by a comma and a space. Then use that variable within f-string or as an argument in print() function. 
# If nobody bought the wands in the given year, then the line "No one was buying magic wands this year." is outputted

customer = []
material = []
year = []
result = []

while True:
    owner = input()
    if owner == 'End':
        break
    owner=owner.split(', ') 
    customer.append(owner[0])
    year.append(owner[1])
    material.append(owner[2])

search = input()   
for customer, year, material in zip(customer, year, material):
    if search == year:
        result.append(f' {customer} (material - {material})')
    else:
        pass

result = ",".join(result)

if len(result) > 0:
    print(f'In {year} the following people bought a wand:{result}.')
else:
    print('No one was buying magic wands this year.')

# Club enrolment
# Each student in the class has to participate in two clubs out of a list of three. The leader of each club brings to the class teacher 
# the unordered list of names of the students who signed up. Each student has to choose two clubs, but some students decided to cheat and signed 
# up for all the clubs at once. Calculate how many of them there are.
#
# INPUT FORMAT
# On the first line, the list of students in the first club, separated by a comma and a space;
# On the second line, the list of students in the second club, separated by a comma and a space;
# On the third line, the list of students in the third club, separated by a comma and a space.
#
# OUTPUT FORMAT
# An integer, the number of students who signed up to all three clubs at once.

first = set(input().split(', '))
second = set(input().split(', '))
third = set(input().split(', '))

result = first & second & third
print(len(result))

# Cakes on Instagram
# Leonid bakes cakes and runs a professional Instagram account. He wants to collect statistics on how many unique users left comments on his posts last week. 
# In addition, Leonid has a list of spam accounts, and if a comment is left from such an account, Leonid doesn't count it. Write a program to help Leonid.
#
# INPUT FORMAT
# Accounts from which Leonid received comments are entered first. Each account is entered on a new line. The input ends when the string "END" is entered.
# Next are the spam accounts, some of them might be accounts that didn't post any comments last week. Each account is entered on a new line. The input ends when 
# the string "END" is entered.
#
# OUTPUT FORMAT
# An integer, the number of unique non-spam accounts that wrote comments to Leonid during last week.

all = set()
bad = set()
while True:
    comments = input()
    if comments == 'END':
        break
    all.add(comments)

spam = input()
while spam != 'END':
    bad.add(spam)
    spam = input()

good = all - bad
print(len(good))

# Kanji
# Vasya learns Japanese words and makes cards. He enters the words in pairs: a word in Russian and then a Japanese character. 
# You have to save the pairs into a dictionary, where the key will be the Russian word, and the Japanese character will be the value. 
# When there is no more pairs, Vasya enters "END". Then Vasya checks whether he has put all the words on the cards and enters words in Russian. 
# Your program should check the dictionary for the entered Russian word and either output the Japanese character corresponding to it or print the 
# message "There is no such word".
#
# INPUT FORMAT
# The word pairs, a Russian word and a Japanese hieroglyph separated by a space. Each on a new line
# The pairs are entered until the line "END" is entered
# Then a string with the Russian word that Vasya wants to check is entered on a new line.
#
# OUTPUT FORMAT
# The string with a Japanese character corresponding to the inputted word or the string "There is no such word".

words = input()
dict = {}

while True:
    if words == 'END':
        break
    words = words.split()
    dict[words[0]] = words[1]
    words = input()

check = input()

try:
    print(dict[check])
except:
    print('There is no such word')

# Searching for a book
# The books variable stores a dictionary with book titles as keys and authors as values. It is created for you already. If you occasionally deleted the variable, 
# click the 'Reset answer' button.
#
# Write a program that takes some non-empty string as input. Then output those titles out of a dictionary books for which either an author's name or the 
# book's title contains the inputted string.
#
# The search is case-sensitive ("Harry" and "harry" are different queries). If there is no match in the dictionary to the inputted string, the 
# program outputs nothing.
#
# INPUT FORMAT
# Non-empty string
#
# OUTPUT FORMAT
# Authors and their book titles matching the condition, each pair on a new line. The author's name and book's title are separated by a colon and a space.

books = {'The Silmarillion': 'John Tolkien',
'Harry Potter and the Goblet of Fire': 'Joanne Rowling',
'The Indomitable Planet': 'Harry Harrison',
'The Man Without a Face': 'Alfred Bester',
'Alice in Wonderland': 'Lewis Carroll', 
'A Space Odyssey': 'Arthur C. Clarke', 
'Dune': 'Frank Herbert', 
'Twenty Thousand Leagues Under the Sea': 'Jules Verne', 
'A Connecticut Yankee in King Arthurs Court': 'Mark Twain', 
'American Gods': 'Neil Gaiman', 
'The Chronicles of Amber': 'Roger Gélasny', 
'The Chronicles of Narnia': 'Clive S. Lewis', 
'War of the Worlds': 'Herbert Wells'}

new_dict = {}
for key, value in books.items(): 
    new_dict[tuple(key.split())] = value

word = input()
for key, value in new_dict.items():
    if (word in key) | (word in value):
        key = str(key).strip('()').replace("'", "").replace(',', '')
        print(f'{value}: {key}')     
    else: 
        pass 
        
        
        


















