# Implement a programme that will help Efrosinya choose an IT company for her internship.
#
# INPUT FORMAT
# The first line is used to enter the names of the companies that are in the top 10 employers, separated by a comma and a space.
# The second line is used to enter the names of the companies where you will have to work using the Python language, separated by a comma and a space.
# The third line is used to enter the names of companies where the internship is paid for, separated by a comma and a space.
# It is guaranteed that the company names in each line are unique.
# Any line may be empty.
#
# OUTPUT FORMAT
# Output the names of companies with paid internships, which are not in the top 10 employers and where you will need to work using Python.
# The names of the companies must be printed in the alphabetical order and separated by a comma and a space.

top = set(input().split(', '))
python = set(input().split(', '))
paid = set(input().split(', '))

result = paid - top & python

print(*sorted(result), sep = ', ')

# Implement a programme that will help Anastasia choose Python programming courses.
#
# INPUT FORMAT
# The first line is used to enter the names of the courses that are only available online, separated by a comma and a space.
# The second line is used to enter the names of the courses that last more than 10 weeks, separated by a comma and a space.
# The third line is used to enter the names of the courses that are suitable for beginners.
# It is guaranteed that the names of the courses on each line are unique.
# Any line may be empty.
#
# OUTPUT FORMAT
# Output the names of the courses that last longer than 10 weeks or are online (online courses longer than 10 weeks are not suitable!)
# and that are at the same time suitable for beginners.
# The names of the courses must be printed in the alphabetical order and separated by a comma and a space.

online = set(input().split(', '))
long = set(input().split(', '))
beginners = set(input().split(', '))

courses = (online ^ long) & beginners

print(*sorted(courses), sep=', ')

# A dictionary with the names of students and their grades is given. This code has already been written.
# Next, the score is entered (an integer).
# Print the names of all students whose grade is higher than the one inputted. Each name is printed on a new line.
# The names should be printed in the same order as they appear in the dictionary.

marks = {
    'Маря': 8, 'Люба': 9, 'Маша': 2,
    'Вова': 4, 'Боря': 4, 'Костя': 5
}

# ваш код ниже
grade = int(input())

for student in marks:
    if marks[student] > grade:
        print(student)
    else:
        pass

# In the while loop, lines of the form "name: score" are read until the line "КОНЕЦ" is entered.
# Each name should be written to the dictionary as a key, and the score (integer) as a value.
# It is guaranteed that the names are not repeated.
# Print the resulting dictionary.

name_score = input()
grades = {}
while name_score != 'КОНЕЦ':
    name, score = name_score.split(': ')
    grades[name] = int(score)
    name_score = input()
    
print(grades)

# Diet
# Petya has decided to follow a new diet. He eats for dinner only those products which names have a certain length and begin with a certain letter. Help Petya determine what he can eat for dinner as a part of the new diet. The input is a comma-separated list of products. The program should output only those products that Petya can eat. If there are no such products, it should output the string "Have to go to the shop."
#
# INPUT FORMAT
# A line of products' names, separated by a comma and space
# The letter with that the names of the products allowed by a diet must begin.
# An integer, the required length of the product name
# Each entry from a new line.
#
# OUTPUT FORMAT
# A string like "Petya can have the following for dinner tonight:" and then a comma-separated sequence of products' names (see example). Do not forget the dot in the end!
# If there are no products satisfying conditions then the program outputs the string "Have to go to the shop."

products = input().split(', ')
letter = input()
n = int(input())

products_list = []

for i, v in enumerate(products):
    if v.startswith(letter) and len(v) == n:
        products_list.append(v)
        
if len(products_list) == 0:
    print("Have to go to the shop.")
else:
    print(f'Petya can have the following for dinner tonight: {", ".join(products_list)}.')

# Battle of the bloggers
# Bloggers Anya and Vanya decided to find out who can make the most money from advertising in two months. Every time someone gets an order for an advertisement, they write down in a special notebook the name of the person who got it and the price of the deal. Help them summarize the results of the competition.
#
# INPUT FORMAT
# Strings with the name of the blogger who got the order (Anya or Vanya) and after a space, an integer, the number that represents the price of the deal. Each such string on a new line.
# The input is terminated when the string "END" is entered.
#
# OUTPUT FORMAT
# Name of the blogger who earned more.
# If they both have earned the same amount, output the string "It's a tie."

anya = 0
vanya = 0

info = input()

while info != 'END':
    name, summ = info.split()
    
    if name == 'Anya':
        anya += int(summ)
    else:
        vanya += int(summ)
    
    info = input()

if anya > vanya:
    print('Anya')
elif vanya > anya:
    print('Vanya')
else:
    print("It's a tie.")




