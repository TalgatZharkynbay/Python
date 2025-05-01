# Deadline
# Problem Statement:
# Masha sits down to do her homework and starts a timer that will remind her every hour how many hours are left until the
# deadline.
# Write a program that counts down to Masha's deadline.
#
# Input Format:
# - A positive integer N – the number of hours to Masha's deadline.
#
# Output Format:
# - N number of lines "Hours to deadline: <number>", where <number> is a number of hours left
# - At the end, the line "Time to hand in your work!" is printed.

hours = int(input())

while hours > 0:
    
    print(f'Hours to deadline: {hours}')
    
    hours = hours -1 

print("Time to hand in your work!")

# Delegation from Japan
# Problem Statement:
# Asya is organizing an event for a delegation from Japan. Help her prepare place cards for the guests by adding "-san"
# to their names.
#
# Input Format:
# - A positive integer N, the number of guests from Japan.
# - Then, N surnames of guests, strings, each on a new line.
#
# Output Format:
# - N guest surnames, each on a new line, with "-san" appended to each.

n = int(input())
number_guests=0

while number_guests < n:
    
    guests=input()
    
    print(f'{guests}-san', sep='\n')
    
    number_guests += 1

# The word game
# Problem Statement:
# Nina and Sasha are playing a word game with complicated rules: a new word must begin with the last letter of the
# previous one and be one letter longer than the previous one. Write a program that prints the length of the word chain
# made during this game.
#
# Input Format:
# - The words for the game, each on a new line.
# - The last word always breaks the chain (does not satisfy the rules of the game)
#
# Output Format:
# - A positive integer, the length of the word chain obtained during the game.
# - Only words that satisfy the rules are counted.

words = input()
count = 1

while True:
        
    old_word = words

    last_letter = old_word[-1]
    
    length = len(old_word)

    words = input()

    if (words[0] != last_letter) | (len(words) != length + 1):

        break

    old_word = words

    count += 1

print(count)

# Excellence scholarship – 2
# Problem Statement:
# Scholarship for studying with excellence is 20000 rubles. Vasya has found a job and decided to save money from his
# scholarship for a new laptop. Sometimes his salary is not enough to cover all his expenses, and he spends some part of
# his scholarship money as well. And sometimes there is extra money left, which he also saves in addition to a scholarship
# money. Every month, when Vasya saves money, he writes down its amount. Help Vasya to determine a number of months, in
# which he was able to save all the scholarship's money (20000) on a laptop.
#
# Input Format:
# - Non-negative integers, not higher than 1 million, each on a new line.
# - Then a negative integer, indicating the end of the input.
#
# Output Format:
# - Number of months, in which Vasya saved at least 20000 rubles

count = 0

while True:
    
    money = int(input())

    if money < 0:
        
        break
    
    elif money - 20000 >=0 :
        
        count += 1
        
    else:
        pass

print(count)

# Expenses on snacks
# Problem Statement:
# Vasya continues his experiments with nutrition: every week he buys a different snack and writes down how much did it
# cost. Count the number of weeks in which he bought the most expensive snacks.
#
# Input Format:
# - Non-negative integer, not higher than 1 million, each on a new line
# - Then a negative integer, indicating the end of input
#
# Output Format:
# - Integer, the number of the highest inputted numbers

max_price = 0
max_count = 0

while True:
    price = int(input())  
    
    if price < 0:
        break  

    if price > max_price:
        max_price = price
        max_count = 1  
        
    elif price == max_price:
        max_count += 1

print(max_count)

# Word search
# Problem Statement:
# There are three lines of input. A text is inputted on two lines and on a third one a number N. You need to find whether
# there is a word number N in that text (two lines combined) and print it out. If there is no word number N, then write
# "There is no such word". Count words starting from 1.
#
# Input Format:
# - On the first line, a string
# - On the second line, another string
# - On the third line, number N – positive integer
#
# Output Format:
# - A string, either a word or string "There is no such word"

first = input()
second = input()
third = int(input())

all = (first + ' ' + second).split(' ')

if len(all) < third:
        
    print("There is no such word")
        
else: 
    print(all[third - 1])

# Password
# Problem Statement:
# According to the banking security policies, a password should not contain a year of birth of a client, otherwise the
# probability to guess a password is too high. Write a program that will check, whether the policy is observed.
#
# Input Format:
# - On the first line, client’s full year of birth (in format YYYY, for example, "1968")
# - On the second line, three versions of a password that client came up with
# - Passwords are separated via space sign.
#
# Output Format:
# - True (boolean) if password contains year of birth, and False if it doesn’t
# - Answer for every version of password should be printed on a separate line

birth = input()
password = input().split(' ')

for word in password:
    
    if birth in word:
        
         print(True)
        
    else:
        
         print(False)

# Game "Cities of the world"

# Sasha has been preparing for the game "Cities of the world" all night, 
# writing down different cities' names from the Internet. 
# Write a program, that takes a string with a list of cities, 
# and then one capital letter and prints out all the cities from the string 
# that start with that letter.

# INPUT FORMAT
# - String, that contains names of the cities, separated by a comma and a space
# - Capital letter

# OUTPUT FORMAT
# - Cities from the inputted string, that start with the given capital letter.
# - Every city should be printed on a new line

cities = input().split(', ')
letter = input()

for word in cities:
    
    if letter in word:
        print(word)
    else:
        pass

# House chores - 2

# Zhenya and Sasha divide the chores from the common list between them, 
# rotating the tasks between them: 
# Zhenya takes the first, third, and so on, 
# and Sasha takes the second, fourth, and so on. 

# Write a program that takes as input the common to-do list 
# and outputs to-do lists for Sasha and Zhenya respectively.

# INPUT FORMAT
# - A common to-do list, tasks are separated with a comma and space

# OUTPUT FORMAT
# - Two lists with tasks separated by commas and spaces: 
#   first a list of Sasha's tasks and then a list of Zhenya's tasks
#

task_str = input()

task_list = task_str.split(', ')

s_tasks = []
z_tasks = []

for i in range(1, len(task_list), 2):
    s_tasks.append(task_list[i])
    
for i in range(0, len(task_list), 2):
    z_tasks.append(task_list[i])
    
print(*s_tasks, sep=', ')

print(*z_tasks, sep=', ')

# Athletes

# A list of athletes in the order in which they have placed in the competition 
# is entered on one line, separated by a space. 
# Then some places numbers are entered on the second line. 
# Find the athlete that took those places in the final standings.

# INPUT FORMAT
# - Two lines. On the first line there are athletes’ names separated by a space.
# - On the second line there are positive integers separated by a space.

# OUTPUT FORMAT
# - For each number from the input, print a line in the format 
#   "<number> place: <athlete>." 
#   or a line with the format "<number> place: No athlete" 
#   if no such place was taken in the final standings.
# - <athlete> is the name of an athlete, <number> the number of place in final standings

names = input().split(' ')
places = input().split(' ')

for place in places:
    
    place = int(place)
    
    try:
        print(f"{place} place: {names[place - 1]}" )
        
    except:
        print(f"{place} place: No athlete" )
    
    
