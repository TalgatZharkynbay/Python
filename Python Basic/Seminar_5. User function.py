# The employees of an inn are entitled to 30 days of holiday per year. The owner of the inn keeps a record of the employees' names and the number of days they have used.
#
# Write a function that displays the names of the employees who still have holiday days left.
#
# REQUIRED FUNCTION
# The remaining_days function takes two lists as input:
# the first list contains employee names (strings);
# the second list contains the corresponding number of holiday days used by each of them (integers).
# The function should return the list of employees who have unused holiday days left (i.e. used days less than 30).
# The employee names must be in the same order as in the original list.
# If there are no such employees, the function returns an empty list.
# NB! In this problem you only define the function, you don't need to call it and read the values, it will happen automatically during the check.

def remaining_days (employees : list, used_holidays : list):
    return [person for person, days in zip(employees, used_holidays) if days < 30]

# Vitya records data about his friends in each country. Write a function that determines how many countries people with the name Vitya is interested in, live in.
#
# REQUIRED FUNCTION
# The function get_contact, whose parameters are:
# dictionary, where the keys are the names of the countries (strings) and the values are lists with the names of Vitya's friends from those countries (string lists).
# the name of a person (string), for which it is necessary to check what country they are from.
# The function should return the number of countries where Vitya's friends with the specified name live.
# If there are no such countries, the function returns 0.
# NB! In this task you only define the function, you don't need to call it and read the values, it will happen automatically during the check.

def get_contact(dictionary, name):
    visit = 0
    for key, value in dictionary.items():
        if name in value:
            visit += 1
        else:
            pass
        
    return visit

# An emperor's reign is considered successful if his battles only end in victories.
#
# Write a function that determines whether the reign was successful.
#
# REQUIRED FUNCTION
# The function great_ruler, whose parameter is a list of tuples, each of which consists of two elements — an integer (the year of the battle) and a string ("victory" or "defeat").
# The function must return the boolean variable True if the emperor's reign was successful and False otherwise.
# NB! In this task you only define the function, you don't need to call it and read the values, it will happen automatically during the check.

def great_ruler (list_of_tuples):
    bad = 0
    for battle in list_of_tuples:
        if battle[1] != 'victory':
            bad += 1
    if bad > 0:
        return False
    else:
        return True

# The researcher collects information about respondents, their income and expenses for the month. For each one, it records the respondent's name and, separated by commas and spaces, income and expenses.
#
# INPUT FORMAT
# Records: respondent's name and, separated by commas and spaces, income and expenses (separated by an underscore "_"). Each entry is entered from a new line. The respondent's name can contain any characters other than commas and underscores.
# Information about one respondent is read only once.
# It is guaranteed that the names of respondents are not repeated.
# When the entries end, the word "END" is entered on a separate line.
#
# OUTPUT FORMAT
# Name of the respondent who had the largest negative income for the month (the value by which expenses exceeded income).
# It is guaranteed that there is only one such respondent.

the_dict = {}
while True:
    records = input()
    if records == 'END':
        break
    else:
        pass
    records = records.split(', ')
    income = int(records[1].split('_')[0])
    expense = int(records[1].split('_')[1])
    
    the_dict[records[0]] = income - expense

worst = [key for key, value in the_dict.items() if value == min(the_dict.values())]
print(*worst)



