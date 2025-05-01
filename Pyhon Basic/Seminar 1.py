# Lucky numbers
# Oleg considers all numbers that are divisible by 4 and by 6 at the same time (for example, 12) his lucky numbers.
# Oleg wants to write a program that accepts a number and outputs all Oleg's lucky numbers between 1 and this number inclusive.
# If there are no such numbers, the program outputs nothing.

n=int(input())
number=1
while number <= n:
    
    if (number % 4 == 0) & (number % 6 == 0):
        print(number)
        
    number+=1

# Excellence Scholarship - 1
# Scholarship for studying with excellence is 20000 rubles.
# Vasya decided to find out whether he will have enough money to support his lifestyle if he gets the scholarship.
# He calculated and wrote all his expenditures for the last 12 months.
# Help Vasya find the number of months in which scholarship would not be enough to cover all the expenditures.
#
# INPUT FORMAT
# 12 non-negative integers, not higher than 100000.
# Each on the new line
#
# OUTPUT FORMAT
# Integer, number of months in which Vasya spends more than 20000 rubles per month

month = 0
count = 0

while month < 12:
    money = int(input())
    if money > 20000:
        count += 1
    month += 1

print(count)

# A New Album
# The band called Crimson Fantomas is about to record an album on vinyl,
# but the record won't hold material longer than 45 minutes.
# Help the band work out how many songs they can release.
#
# INPUT FORMAT
# On each line, enter the length of the song in minutes and seconds in m:ss format.
# It is guaranteed that each song is no longer than 10 minutes.
# Input ends when the total length of the songs exceeds 45 minutes.
#
# OUTPUT FORMAT
# The number of songs that will fit on a vinyl record.

summ = 0
count = 0
while summ <= 45 * 60:
    song = input()
    minutes = int(song[0])
    seconds = int(song[2] + song[3])
    summ += minutes * 60 + seconds
    count += 1
print(count - 1)

# Expenses on a lunch
# Vasya ate at a different place every month and then decided to find out
# in which month he had the cheapest lunches.
# He calculated and wrote down all the expenditures on food in a few recent months.
# Calculate what was the minimum amount of money that Vasya had spent on lunches.
#
# INPUT FORMAT
# Non-negative integers, not higher than 1 million, each on a new line
# Then a negative integer, indicating the end of input
#
# OUTPUT FORMAT
# Integer, the lowest inputted number (except the last one, which is indicating the end of input)

# Enter the amount of the first month
money = int(input())

# The amount is higher at the beginning and there is a minimum, because there is nothing to compare with yet
minimum = money

while money >= 0:
    if money < minimum:   
        minimum = money   
    money = int(input()) 

print(minimum) 

# Monthly expenditures
# Vasya has noticed, that every month he struggles more and more to save for a laptop.
# He thinks, that it is due to the fact, that he spends more and more money every month.
# Check, whether it is true, that in every month Vasya had spent more money than in a previous one.
#
# INPUT FORMAT
# Non-negative integers, not higher than 1 million, each on a new line
# Then a negative integer, indicating the end of input
#
# OUTPUT FORMAT
# True (boolean data type), if in every month Vasya had spent more than in previous one
# (not including the last number, which indicates the end of an input), and otherwise False
# If expenditures were inputted only for zero or one month, then output should be True

increase=True
previous_month=0

while True:
    current_cost=int(input())
    
    if current_cost < 0:
        break
    
    if current_cost <= previous_month:
        increase=False
        
    previous_month=current_cost
        
print(increase)

# Date
# Write a program that takes a date in a format DD/MM/YYYY and prints it like "DD month YYYY year"
#
# For months' name use the list provided in the answer box.
#
# INPUT FORMAT
# String with a date in a format DD/MM/YYYY, for example "1.04.2017".
#
# OUTPUT FORMAT
# Inputted date in a format "DD month YYYY year", for example, "1 April 2017"

months = ["January" ,"February", "March", "April" ,"May" ,"June" , "July", 
"August", "September", "October", "November", "December"] 

date=input()

day=int(date.split('.')[0])
month=int(date.split('.')[1])
year=int(date.split('.')[2]) #dd, mm, yyyy = date.split('.')

name_month=months[month-1]

print(f'{day} {name_month} {year}')

# Dictation
# The teacher makes up a dictation that should check how well the students have learned
# the new spelling rule. Write a program that will check how many words for a given rule
# are there in the dictation.
#
# INPUT FORMAT
# On the first line there are the letter combinations that should occur in the dictation words,
# separated by a space.
# The second line contains the dictation text: all sentences are in lowercase letters,
# no upper case letters.
# It is guaranteed that each word does not contain two or more different letter combinations
# to be checked.
#
# OUTPUT FORMAT
# One number, how many words in the dictation text contain the correct letter combinations.

count = 0
finding_words=input().split()
stroka=input()

for word in finding_words:
    count += stroka.count(word)

print(count)

# House chores - 1
# Zhenya and Sasha divide the chores from the common list between them, trying to distribute tasks equally:
#
# If there is an even number of tasks:
#   - Zhenya does the first half
#   - Sasha does the second half
#
# If there is an odd number of tasks:
#   - They share the middle task (appears in both lists)
#   - The remaining tasks are split as above
#
# Write a program that takes as input the common to-do list and outputs
# to-do lists for Sasha and Zhenya respectively.
#
# INPUT FORMAT
# A common to-do list, tasks are separated with a comma and space
#
# OUTPUT FORMAT
# Two lists with tasks separated by commas and spaces:
#   - First line: Sasha's tasks
#   - Second line: Zhenya's tasks

task_str = input()

task_list = task_str.split(', ')

# s_tasks = []
# z_tasks = []

half_task = int(len(task_list)/2)

if len(task_list) % 2 ==0:
    
    z_tasks = task_list[:half_task]
    s_tasks = task_list[half_task:]
    
else:
    
    z_tasks = task_list[:half_task+1]
    s_tasks = task_list[half_task:]
    
  
print(*z_tasks, sep=', ')

print(*s_tasks, sep=', ')

# Library
# Zhenya has a list of textbooks to borrow from the library and their corresponding ISBNs
# (the book and its corresponding number are situated on the same position in the two lists).
# To find a book in the library you need to call its ISBN.
# Some books Zhenya already has, and you don't need to borrow them from the library.
#
# Write a program that takes as input:
#   1. A list of book titles
#   2. A list of ISBN numbers
#   3. The titles of books Zhenya already has
# And outputs the ISBNs of the books she doesn't have yet.
#
# INPUT FORMAT
# First line: Exact names of books from the list of textbooks (case-sensitive),
#             separated by comma and space
# Second line: ISBNs of books from the list of textbooks (case-sensitive),
#              separated by comma and space
# Third line: Exact titles of books that Zhenya has (case-sensitive),
#             separated by comma and space
#
# OUTPUT FORMAT
# ISBNs of the books that Zhenya does not have,
# each number on a new line

books_all_title = input().split(', ')

books_all_isbn = input().split(', ')

books_own = input().split(', ')

for idx in range(len(books_all_title)):
    if books_all_title[idx] not in books_own:
        print(books_all_isbn[idx])

# Emails
# Taisia updates her list of the classmates' email addresses before adding them to a mailing list. The classmates text her their old email address and the one they want to replace it with, separated by a space. Taisia finds the address in her list and replaces it with a new one.
#
# INPUT FORMAT
#
# On the first line, email addresses of the classmates that Taisia has, separated by commas.
# On the second line, the number of the classmates whose address are to be replaced, a non-negative integer.
# For each classmate the pair "<old address> <new address>", written with a space. The pair for each classmate is one a new line.
# OUTPUT FORMAT
#
# The answer should contain the string made of a final list of addresses, the addresses in the string are separated with a semicolon

emails = input().split(',')
n = int(input())

for student in range(n):
    to_change = input().split()
    for i in range(len(emails)):
        if emails[i] == to_change[0]:
            emails[i] = to_change[1]
            break
            
print(';'.join(emails))
