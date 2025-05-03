# Implement a programme that finds branches of a chain of shops with high profit levels.
#
# INPUT FORMAT
# Given is the dictionary shops, in which the keys are shop names (strings) and the values are lists with profit amounts for the last 3 months (integers). It is guaranteed that shop names are not repeated.
# Then the amount of profit, below which the shop becomes unprofitable, is entered.
#
# OUTPUT FORMAT
# The programme checks if a shop had at least one month with profit that is too low (less than entered value) and displays the names of such shops, each on a new line. If there are no such shops, the programme does not output anything.

shops = {'Coin': [6000, 4000, 2300], 
        'Road': [6700, 4000, 2100], 
        'A Primer of Tastes' : [10000, 8000, 6000], 
        'SladkoVill' : [5000, 9000, 4000]}

profit = int(input())
companies = []

for key, value in shops.items():

    if min(value) < profit:
            companies.append(key)
    else:
        pass

print(*companies, sep = '\n')

# Implement a programme that finds cities by the name of a country.
#
# INPUT FORMAT
# Given is the dictionary cities, in which keys are country names (strings) and values are lists of city names (strings).
# The name of a country is entered.
#
# OUTPUT FORMAT
# The programme checks if the entered country exists in the dictionary.
# If there is no such country in the dictionary, the programme prints the phrase "There is no such country".
# If there is such a country in the dictionary, the programme prints the first alphabetical city from the list of relevant cities.

cities = {'Austria' : ['Vienna', 'Granz', 'Linz'],
          'Spain' : ['Barcelona'],
          'Norway' : ['Oslo', 'Hamar', 'Alta'],
          'Mexico' : ['Mexico City', 'Leon']}

country = input()

try:
    print(sorted(cities[country])[0])
except:
    print("There is no such country")


# Implement a programme that checks internet providers in terms of fulfilling contractual terms and finds reliable providers.
#
# INPUT FORMAT
# Given is the internet dictionary, in which the keys are company names and the values are lists with speed indicators for the last week:
# 2 — speed exceeded the stated speed;
# 1 — speed was as advertised;
# 0 — speed was lower.
# It is guaranteed that company names are not repeated.
# The minimum acceptable number of days with the speed higher than the declared one is entered.
#
# OUTPUT FORMAT
# The programme checks that there are no days with lower speed in the company's statistics and that the number of days with increased speed is not less than the entered value, and outputs the names of such companies, each on a new line.
# If there are no such companies, the programme does not output anything.

internet = {'Mostelecom': [1, 2, 1, 1, 1, 2, 1], 
            'Connection2023': [1, 1, 0, 1, 1, 1, 0], 
            'MTTS': [1, 1, 1, 1, 2, 1, 1], 
            'Triline': [2, 2, 1, 1, 1, 2, 2]}

minimum = int(input())
good = []

for key, value in internet.items():
    if (value.count(2) >= minimum) & (min(value) != 0):
        good.append(key)
    else:
        pass    
print(*good, sep = '\n')
    
# Implement a programme that checks how popular a language school is.
#
# INPUT FORMAT
# Given is the dictionary schools, in which the keys are school names and the values are lists with the number of student applications for the last week. It is guaranteed that school names are not repeated.
# The minimum acceptable average number of applications per week so that the school does not lose profit is entered.
#
# OUTPUT FORMAT
# The programme checks that the average number of applications to a school is not lower than the entered value in the application statistics and outputs the names of such schools. The names are printed in the same order in which they are stored in the dictionary. Each name is printed on a new line.
# If there are no such schools, the programme does not output anything.

schools = {'LanguageforEveryone': [45, 67, 30, 24, 82, 12, 91], 
           'Pythonists2023': [32, 14, 29, 100, 21, 70, 25], 
           'EngStart': [105, 48, 22, 74, 53, 90, 12], 
           'NewLang': [83, 200, 0, 44, 12, 54, 19]}

minimum = int(input())
good = []

for key, value in schools.items():
    if sum(schools[key]) / len(schools[key]) >= minimum:
        good.append(key)
    else:
        pass
    
print(*good, sep = '\n')

# Registration for the hackathon
# Many teams have registered for the student hackathon and the organisers want to list them on the website. Help them sort the list of team names alphabetically. Please note that the letter case of the team names should not be taken into account.
#
# INPUT FORMAT
# A string of team names separated by semicolons.
#
# OUTPUT FORMAT
# A string of team names separated by semicolons, sorted alphabetically.
#
# Hint: use sorted() with a key parameter.

names = input().split(';')
print(*sorted(names, key = str.lower), sep=';')

# Vinyl records
# Vasya collects music on vinyl records and wants to put his library in order, arranging the records by artist name in alphabetical order 
# (don't worry about the case, just normally sort the strings that you've read).
#
# INPUT FORMAT
# Lines consisting of the name of the record and the artist, separated by a semicolon and a space.
# After all the lines with the record names, there is an "end" line, which indicates the end of the input.
# It is guaranteed that each performer appears only once.
#
# OUTPUT FORMAT
# Titles of vinyl record names, one title per line
# The titles are outputted in the order determined by the alphabetical order of the artists, who published the album 
# (so David Bowie comes before Simon & Garfunkel and Queen)

dict = {}

while True:
    names = input()
    if names == 'end':
        break
    names = names.split('; ')
    dict[names[0]] = names[1]

for key, value in sorted(dict.items(), key = lambda item: item[1]):
    print(key)

# Final exams
# After the final exams, the school needs to print the school-leaving certificates. These may only be issued to pupils who have achieved a passing grade. Prepare a list of students for whom certificates can be printed.
#
# INPUT FORMAT
# A line with a list of students and their final exam scores, separated by semicolons and spaces. The student's name is separated from their exam score by a comma and a space.
# A positive integer, the passing grade, is entered on a new line.
#
# OUTPUT FORMAT
# A list of students' names to whom certificates can be issued, separated by commas with a space, in order of appearance.

scores = input().split('; ')
passing = int(input())
dict ={}

for scores in scores:
    student, score = scores.split(', ')
    if int(score) >= passing:
        dict[student] = int(score)

print(*dict.keys(), sep = ', ')

# E-store
# Mira is browsing new furniture in an online shop. But unfortunately she is limited in her finances. Please help her by sorting all the products on the page from the most expensive to the cheapest.
#
# INPUT FORMAT
# Lines consisting of the name of the item followed by its price in rubles. The price is separated by a semicolon and a space. The price of each item is a positive integer.
# When the string 'end' is inputted, there will be no more input.
# It is guaranteed that all names are unique and all prices are unique.
#
# OUTPUT FORMAT
# Lines with items names, each name on a new line. Names are outputted in the descending order by their prices.

dict = {}

while True:
    furni = input()
    if furni == 'end':
        break
    furni = furni.split('; ')
    dict[furni[0]] = int(furni[1])

for key, value in sorted(dict.items(), key = lambda item: item[1], reverse = True):
    print(key)

# The best delivery guy
# A delivery manager wants to find the best delivery guys (or girls) among his subordinates — the delivery man with the highest average score received from the customers.
# For each delivery, customers have rated the delivery men and the manager has a record of each delivery man's performance on a scale from 1 to 5, where 1 is the worst score and 5 is the best.
# Help the manager by reading the delivery performance records and finding the best delivery person in the company.
#
# INPUT FORMAT
# Lines consisting of a delivery person's name and delivery score. The score is separated from the name by a comma and a space, and can be an integer between 1 and 5.
# When the string 'end' is inputted, then there will be no more input.
#
# OUTPUT FORMAT
# A line containing the name of the best delivery person, their average grade and a list of all the grades given to them.
# The name is separated from the average grade by a comma and a space, the average grade is separated from the list of grades by a colon and a space.
# The grades in the list of grades are displayed separated by a comma and a space.
# There is a dot at the end of the line.

dict = {}

while True:
    score = input()
    if score == 'end':
        break
    else:
        pass
    
    score = score.split(', ')
    
    if score[0] in dict.keys():
        dict[score[0]].append(int(score[1]))
    else:
        dict[score[0]] = [int(score[1])]

winner = sorted(dict, key = lambda key: sum(dict[key])/len(dict[key]), reverse = True)[0]
     
print(f'{winner}, {sum(dict[winner])/len(dict[winner])}: {", ".join(str(i) for i in dict[winner])}.')




    
    
    
