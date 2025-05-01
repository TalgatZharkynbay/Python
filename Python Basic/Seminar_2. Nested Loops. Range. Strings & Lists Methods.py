# Implement a programme that filters transport companies based on the estimated number of days for the delivery we are interested in: 
# 
# The first line is used to enter the names of the companies, separated by a space. 
# The second line is used to enter numbers — the estimated number of days required to deliver the shipment — separated by a space. It is guaranteed that information for at least one company will be entered. 
# Then a number is entered — the maximum acceptable number of days for delivery. 
# The programme outputs the names of the companies whose estimated delivery time is less than or equal to the entered number of days, each on a new line. 
# If there are no such companies, the programme does not output anything.

names = input().split()
numbers = input().split()
max = int(input())

goodnames=[]

for i, v in enumerate(names):
    if int(numbers[i]) <= max:
        goodnames.append(v)
    else:
        pass

print(*goodnames, sep='\n')

# Implement a programme that filters countries based on their GDP per capita: 
# 
# The first line is used to enter the names of the countries, separated by a space.
# The second line is used to enter real numbers — GDP per capita, separated by a space. It is guaranteed that at least one country is entered.
# Then a float number is read — the GDP per capita value that we are interested in.
# The programme outputs the names of countries whose GDP is equal to or higher than the entered one, each on a new line.
# If there are no such countries, the programme does not output anything.

names = input().split()
gdp = input().split()
n = input()

result = []

for i, v in enumerate(names):
    if float(gdp[i]) >= float(n):
        result.append(v)
    else:
        pass
    
print(*result, sep='\n')

# Implement a programme that filters students based on the results of international English language exams.
#
# INPUT FORMAT
# The first line is used to enter students' surnames, separated by a space.
# The second line is used to enter float numbers — scores for the exams, separated by a space.
# It is guaranteed that the information for at least one student will be entered.
#
# OUTPUT FORMAT
# The programme outputs the names of students whose scores are not less than the arithmetic mean of all scores, each on a new line.

surnames = input().split()
scores = list(map(float, input().split()))
result = []

for i, v in enumerate(surnames):
    mean = sum(scores)/len(scores)
    if scores[i] >= mean:
        result.append(v)
    else:
        pass
print(*result, sep = '\n')

# Implement a programme that will check if the word lengths are determined correctly.
#
# INPUT FORMAT
# The first line is used to enter words, separated by a comma and a space.
# The second line is used to enter integers — word lengths determined by a special algorithm, separated by a space.
# It is guaranteed that at least one word will be entered.
#
# OUTPUT FORMAT
# The programme outputs the words whose lengths are determined correctly.
# The words are output in the same order as they were input.
# Each word is printed on a new line. If there are no such words, the programme outputs nothing.

words = input().split(', ')
lengths = list(map(int, input().split()))
result = []

for i, v in enumerate(words):
    if len(v) == lengths[i]:
        result.append(v)
    else:
        pass
print(*result, sep='\n')

# Coursework
# A line with a committee's decision on the coursework is given. Output 'YES' if the decision starts with the substring "accept", or 'NO' otherwise. Note that the decision can be written in any case (e.g. capital letters, small letters, or capital letters).
#
# INPUT FORMAT
# A string
#
# OUTPUT FORMAT
# String "YES" or "NO"

stroka = input().lower()

if stroka.split()[0].startswith('accept'):
    print('YES')
else:
    print('NO')

# The Contest
# N people participated in the contest. Their results are written in the format 'M points', with any number of spaces at the beginning and at the end of the line. Calculate the average score of the participants.
#
# INPUT FORMAT
# The program takes as input the number of participants in the contest, N.
# Next comes N lines, each line contains the contestant's result in the format described above.
#
# OUTPUT FORMAT
# A real number, the average score of all participants. Print number as it is, no need for rounding.
n = int(input())
lst = []

for stroka in range(n):
    info = input().strip()
    score = int(info.split()[0])
    
    lst.append(score)
    
print(sum(lst) / len(lst))

# Corporate emails
# A company "Pamparam" registers corporate emails for its employees and wants to use their logins for their regular email services.
#
# The company has only one limitation: corporate email cannot start with a number, a dot, a dash or an underscore. So if the regular email address starts with those symbols, they should be removed. Help a company HR manager form a list of new email addresses for their domain pamparam.ru
#
# INPUT FORMAT
# String with the regular email addresses of company's employees, divided by a comma and a space
#
# OUTPUT FORMAT
# String with the new email addresses: domains (the part after @) should be changed on 'pamparam.ru', and symbols violating the limitation should be removed. Domain address is saved for you into the variable.
# New email addresses are printed via semicolon (';') and space.

domain = 'pamparam.ru'
result = []
emails = input().split('; ')

for mail in emails:
    mail = mail.lstrip('_-0123456789.')
    mail = mail.split('@')[0]
    result.append(f'{mail}@{domain}')
    
print('; '.join(result))

# Tests
# Petya solves tests from the text book. He writes down his answers as a four-digit test ID and a capital letter for the answer option 
# (for example 4578A). In the end of a textbook there are answers, given as a sequence of the capital letters. 
# Help Petya to find out if his answers are correct.
#
# INPUT FORMAT
# A string, containing a list of Petya's answers divided by a comma and a space
# A string, a sequence of letters — correct answers to the test
#
# OUTPUT FORMAT
# There are two lines in the output.
#
# On the first line, string "Your answer:" and the sequence of capital letters that Petya has choosen.
# On the second line print string "Good job! Everything is correct" if Petya's answers are the correct ones. Otherwise, print string "You have made some mistakes, 
# the correct answer is:" followed by the sequence of letters — the correct answer.

petya = input().split(', ')
right_answers = input()

ans = ''
for word in petya:
    ans += word[-1]
print(f"Your answer: {ans}")
if ans == right_answers:
    print("Good job! Everything is correct")
else:
    print(f"You have made some mistakes, the correct answer is: {right_answers}")

# The sports season
# There are 5 competitions during the sports season.
# If an athlete participates in a competition, he gets 1 point.
# If he is in the top three, he gets 3 points.
# If he wins, he gets 5 points.
# If an athlete did not participate, he gets 0 points.
# Write a code that calculates an athlete's rating based on the standings and an athlete's name.
#
# INPUT FORMAT
# Tournament table that consists of five strings, each on a new line.
# Each string contains the names of athletes, separated by comma and space.
# The order of the names corresponds to the order of their places in the given competition. E.g. the first name in the string is Ivanov, 
  # it means that Ivanov was first in that competition.
# Then on a new line a string with the name of an athlete for whom we need to calculate a ranking.
#
# OUTPUT FORMAT
# An integer, the rating for the inputted athlete

lst = []

for i in range(5):
    surnames = input().split(', ')
    lst.append(surnames)

finding_surname = input()
counter = 0

for spisok in lst:
    if finding_surname in spisok:
        place = spisok.index(finding_surname) + 1
        
        if place == 1:
            counter += 5
        elif (place == 2) or (place == 3):
            counter += 3
        else:
            counter += 1

print(counter)

# Execute the following program.
#
# INPUT FORMAT
# The first input are words, separated by a space.
# The second input are integers "1" or "0", separated by a space. These numbers represent the result of an algorithm that determines whether a word has lowercase letters (1) or not (0).
#
# OUTPUT FORMAT
# The program should verify the accuracy of the algorithm.
# If the algorithm failed for certain words, the program should store them in a separate list.
# In the end, the program should print the resulting list. The words should appear in the same order as they were entered.
# If there are no such words, the program prints an empty list.

word = input().split()
integer = input().split()
store = []

for i, v in enumerate(word):
    if (integer[i] == '1') and (v.isupper()):
        
        store.append(v)
    
    elif (integer[i] == '0') and (v.isupper() == False):
        
        store.append(v)
        
print(store)
