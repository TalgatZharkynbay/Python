# Online shop
# A table of products in an online shop is given. Write a program that learns how to select items from the table that are not more expensive than a certain price.
#
# INPUT FORMAT
# File goods.csv, where on each line there is information about the product. The separator in the table is a semicolon, that organizes information into columns.
# You should open file with encoding='utf-8' parameter.
# The last column always contains a positive integer — the price of the goods.
# A positive integer — the upper price limit for the goods — is inputted.
#
# OUTPUT FORMAT
# File filtered-goods.csv, where lines with goods from file goods.csv are written out, for which the price does not exceed the entered one. Rows must be written out in the same order as they appear in goods.csv file.
# Save file with encoding='utf-8' parameter.
# The files used in the sample are goods.csv and filtered-goods.csv

limit = int(input())
with open('goods.csv', 'r', encoding = 'utf-8') as input_file:
    with open('filtered-goods.csv', 'w', encoding = 'utf-8') as output_file:
        for line in input_file:
            line = line.strip()
            price = int(line[line.rfind(';')+1:])
            if price <= limit:
                print(line, file = output_file)

# Generator of invitations
# The university from time to time organizes conferences for students. For each conference, the organizers form and send invitations to all registered participants with the name of the registered participant, the name of the conference, the opening time and the registration number of the participant.
#
# Write a program that will automatically generate and save these invitations to the file.
#
# INPUT FORMAT
# A string with a conference name
# Then, the opening time of the conference is entered on a new line.
# Then, on a new line, a sequence of names of registered conference participants is entered, separated by commas and spaces
#
# OUTPUT FORMAT
# invitations.txt text file
# Inside the file for each registered participant, an invitation should be written in the format:
# Good afternoon, <name>!
# You have registered for the conference "<conference name>", which will take place at <conference opening time time>.
# Your registration number is <number>.
#
# Registration numbers are generated as the number of the participant in the inputted list, starting from 1. The invitations must be written in the file in the same order.
# In the example file invitations.txt is used

conference_name = input()
opening_time = input()
names = input().split(', ')
number = 1
with open('invitations.txt', 'w', encoding = 'utf-8') as output_file:
    for name in names:
        print(f'Good afternoon, {name}!', file = output_file)
        print(f'You have registered for the conference "{conference_name}", which will take place at {opening_time}.', file = output_file)
        print(f'Your registration number is {number}.', file = output_file)
        number += 1

# An editor of reviews
# Pasha wrote a review on a film, but forgot to put quotation marks (" ") around the film's title. Write a program that will do it automatically.
#
# INPUT FORMAT
# A text file review.txt with a review.
# A string containing a title of a reviewed film.
#
# OUTPUT FORMAT
# A review_correct.txt text file with a review's text, in which the film's title is surrounded by double quotation marks (" "). Every time, the title is mentioned in a text, it should be corrected. You should consider word's case (words, that begin with a small and a big letter are counted as different ones)
# File names in example are: review.txt и review_correct.txt

film = input()
with open('review.txt', 'r', encoding = 'utf-8') as input_file:
    with open('review_correct.txt', 'w', encoding = 'utf-8') as output_file:
        for line in input_file:
            line = line.strip()
            line = line.replace(f'{film}', f'"{film}"')
            print(line, file = output_file)
