# Jolly movers
# The furniture shop movers are loading the truck to make a delivery. The heaviest goods have to be loaded first to prevent the car from tipping over. Help the movers by sorting the list of product by their weight in descending order: the heaviest products should be at the beginning of the row and the lightest ones at the end.
#
# INPUT FORMAT
# String of real numbers separated by spaces
#
# OUTPUT FORMAT
# String of real numbers separated by spaces, sorted in descending order.

weight = list(map(float, input().split(' ')))

print(*sorted(weight, reverse = True), sep = ' ')

# Number of visitors to the café
# Dima has opened a 24-hour café and wants to find out during which hours his café has more customers so that he can better plan the shifts of the waiters and the kitchen stuff.
# Help Dima by reading the information about the number of bills paid for each hour of the cafe's operation over several days and displaying the information about one of the hours requested.
#
# INPUT FORMAT
# A positive integer N, the number of days with statistics.
# N lines of 24 comma-separated integers, statistics for customers numbers for each hour of the day.
# Then the integer H — the hour that Dima wants to see information about (0 to 23) — is inputted.
#
# OUTPUT FORMAT
# Integers, the numbers of customers for a given hour for each day.
# The number for each day is outputted on a new line.

days = int(input())
hours = [[] for i in range(0, days)] 

for i in range(0, days):
    hours[i] = list(map(int, input().split(', ')))

h = int(input())

for hour in hours:
    print(hour[h])

# Music library
# Vasya collects music and wants to get better acquainted with the records he collects. Help Vasya by writing a program that tells him how many records Vasya has of the given artist, and displays them in alphabetical order.
#
# INPUT FORMAT
# Lines with the artist's name and the record's title, separated by a colon and a space, for each of the records that Vasya has.
# A line with the name of the artist that Vasya wants to get info about. There are no colons in this line and this line marks the end of the data entry.
#
# OUTPUT FORMAT
# A string of the form "Queen (3): A Night at the Opera, Innuendo, The Miracle.", consisting of the band name, number of records that Vasya has (in parentheses) and, after a colon and a space, a list of albums titles, separated by a semicolon and a space.
# Note, there is a dot at the end of the line.
#
# Hint: read the data in the dictionary of lists where the artist is the key and the list of album titles is the value. To output albums' titles in desired format you can with a help of `.join()` method.

music = {}

while True:
    song = input()
    if song.find(':') == -1:
        break
    else:
        pass
    
    song = song.split(': ')
    
    if song[0] in music.keys():
        music[song[0]].append(song[1])
    else:
        music[song[0]] = [song[1]]

print(f'{song} ({len(music[song])}): {", ".join(sorted(music[song]))}.')

# Grammy's Award
# Anya is writing an article about the Grammy Awards and wants to count how many times artists have won an award and find out who has won the biggest and the fewest number of awards. Help Anya write a program that counts these statistics.
#
# INPUT FORMAT
# A positive integer N, the number of lines with the names of artists who have won Grammys.
# N lines with the names of the performers (each name on a new line).
#
# OUTPUT FORMAT
# A string with the name of the artist who received the most Grammys and, separated by a colon and a space, the number of Grammys received (an integer).
# On a new line, a string with the name of the artist who received the Grammy the fewest amount of times and, separated by a colon and a space, the number of Grammys received (an integer).

number = int(input())
music = {}

for i in range(number):

    artist = input()
    if artist not in music.keys():
        count = 1
        music[artist] = count
    else:
        count = music[artist]
        count += 1
        music[artist] = count

min = [key for key in music if music[key] == min(music.values())][0]
max = [key for key in music if music[key] == max(music.values())][0]

print(f'{max}: {music[max]}')
print(f'{min}: {music[min]}')
    
# Instagram subscriptions
# Help Anton, a blogger to select Instagram accounts from his database with a specific audience size to send a collaboration offer.
#
# REQUIRED FUNCTION
# The function named filter_accounts that accepts a dictionary of accounts as a parameter, the keys of which are account logins and the values are the number of subscribers.
# It also takes integers min_followers and max_followers as parameters.
# The function has to return a list of account logins, where the number of subscribers is between min_followers and filter_accounts inclusive, the addresses have to be sorted in lexicographical order.
# In this task you only define the function: you don't need to read the input and call it, the platform will do it automatically when checking.

def filter_accounts (dict, min_followers , max_followers ):
    return sorted([key for key, value in dict.items() if value >= min_followers and value <= max_followers])

# A telegram from Matroskin - 2
# Matroskin wants to send Uncle Fedor a telegram, but to do this he has to remove all punctuation marks and write everything in capital letters. Write a program that will format Matroskin's telegram. Use the punctuation variable from the string module to get/identify punctuation marks.
#
# Note that you don't need to implement functions for this task.
#
# INPUT FORMAT
# The telegram text with punctuation marks
#
# OUTPUT FORMAT
# The telegram text entered, with no punctuation marks and all letters should be in uppercase.

import string

text = input()
clean_text = '' # initiating an empty string to store a clean text
for symbol in text:
  if symbol not in string.punctuation: # if the symbol is not a punctuation then add it to the clean_text
    clean_text += symbol

print(clean_text.upper()) # print the text without punctuation

