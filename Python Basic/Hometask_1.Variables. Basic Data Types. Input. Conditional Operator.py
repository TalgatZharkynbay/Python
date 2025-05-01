# The Pencil Shop
# Problem Statement:
# Vitya goes to the shop to buy pencils, each costing N rubles. In total Vitya is ready to spend M rubles on pencils.
# Estimate how many pencils he can buy and how much money will be left in the end.
#
# Input Format:
# - A positive integer N - how much one pencil costs.
# - A positive integer M - how much money Vitya is willing to spend on the purchase.
# Output Format:
# An integer: how many pencils can be bought and, separated by a space on the same line also an integer: how much money remains after the purchase.
# Example:
# Input:
# 19 100
# Output:
# 5 5

n = int(input())
m = int(input())
print(m//n, m%n)

# Telegrams
# Problem Statement:
# In the 19th and 20th centuries, every single character in a telegram was paid for. Help Stepan to plan the cost of a telegram by counting and printing how many characters his text consists of.
# Input Format:
# - String with the text of the telegram.
# Output Format:
# A string like "There are <the telegram length> characters in: <the telegram text>", 
# where <the telegram length> is an integer corresponding to the number of characters in the text (including spaces) and <the telegram text> is the string with the text of the telegram.

telegram=input()
print(f"There are exactly {len(telegram)} characters in: {telegram}")

# The Telephone Number
# Problem Statement:
# The company Contoso decided to change the format of records in the telephone directory, instead of telephone numbers like 1800550123 they decided to use telephone numbers like +1(800) 555-01-23. 
Help our secretaries to record the numbers in the new format.
# Input Format:
# - An 11 digit string of the telephone number, like 12345678910
# Output Format:
# - String like +1(234) 567-89-10

tel=input()
print(f'+{tel[0]}({tel[1:4]}) {tel[4:7]}-{tel[7:9]}-{tel[9:]}')

# Time for English
# Problem Statement:
# Vika is learning English and practicing to convert time from AM/PM format to a usual 24-hour format. Help her by
# writing a program, which will print a time which corresponds with a time given in the textbook. In the textbook it is
# said that it is exactly A hours B minutes PM (after 12:00).
# Input Format:
# - Integer A – number of hours that is on the clock in the textbook, A >= 1, A < 12
# - Integer B – number of minutes that is on the clock in the textbook, B >= 0, B < 60
# Output Format:
# - String like HH:MM

a=int(input())
b=int(input())
print(f'{a+12}:{b}')

# Interest on deposit
# Problem Statement:
# Vasya has put money in the bank at interest rate of 4% per year with fixed deposit amount and monthly payment of
# interest. Write a program, that will get information about deposit and print an amount of monthly payment. For
# example, if Vasya has deposited 90000 rubles, in a year he would get 4% out of this amount (3600 rubles) and every
# month he would get 1/12 of all the yearly interest (300 rubles)
# Input Format:
# - Integer – the deposit amount
# Output Format:
# - Integer – amount of monthly payments

deposit=int(input())
print(int(deposit*0.04/12))

# Traffic lights
# Problem Statement:
# In some cities traffic lights have a special voice signal. Write a program that will print a text for a voice signal
# corresponding to the current light colour.
# Input Format:
# - String "red" or "green" depending on the current signal of traffic light.
# Output Format:
# - If there is a red signal, output should be a string "Please, wait for the permission to cross".
# - If there is a green signal, output should be a string "Crossing is allowed"

col=input()
if col=='green':
    print("Crossing is allowed")
else:
    print("Please, wait for the permission to cross")

# What century is it?
# Problem Statement:
# Write a program that will show to which century the given year belongs. Don't forget that, for example, 21st century
# began in year 2001, year 2000 is considered to be a part of 20th century.
# Input Format:
# - Integer from 1 to 2100 – a year
# Output Format:
# - Integer – a century to which belongs a given year

year=int(input())
if year % 100==0:
    print(int(year/100))
else:
    print(int(1+year/100))

# Aibolit’s assistant
# Problem Statement:
# Dr. Aibolit decided to build a robot to help him make standard prescriptions. The robot should work per the following
# instructions:
# 1. First, ask the patient what they are complaining about?
# 2. If the patient has a cough, ask if it is a wet or a dry cough? The robot prescribes "Otharkin-1" for a wet cough and
# "Otharkin-2" for a dry cough.
# 3. If the patient complains of fever, ask what the temperature is. If it’s higher than 38 degrees, the robot prescribes
# "Antifever-1", otherwise "Antifever-2".
# 4. Otherwise, the robot sends the patient to Dr. Aibolit.
# Help Dr. Aibolit to implement such a robot.
# Input Format:
# - The string with the patient’s initial complaint.
# - If the patient has "cough" as a complaint, ask for the nature of the cough on a new line – "wet" or "dry".
# - If the patient entered "fever" as the complaint, ask for a positive real number (float) on a new line – patient
# temperature.
# Output Format:
# - If the robot knows how to handle the complaint, a string in the format "Prescribing you <name of medicine>" is output.
# - Otherwise, the string "Please see Dr. Aibolit" will be displayed.

complaint=input()
if complaint=='cough':
    cough=input()
    if cough=='dry':
        print("Prescribing you Otharkin-2")
    else:
        print("Prescribing you Otharkin-1")
elif complaint=='temperature':
    temp=float(input())
    if temp>38:
        print("Prescribing you Antifever-1")
    else:
        print("Prescribing you Antifever-2")
else:
    print("Please see Dr. Aibolit")

# Going to the museum
# Problem Statement:
# A ticket to the museum costs 500 rubles, but for those who show a student ID, it’s 250. Help Andrei see if he can get
# into the museum today.
# Input Format:
# - A positive integer, the amount of money that Andrei has on him.
# - Then on a new line a string "Yes" if Andrei has his student ID or string "No" – otherwise.
# Output Format:
# - String "Yes" if Andrei can buy a museum ticket, string "No" otherwise.

money=int(input())
has_id=input()
if (has_id=='Yes') & (money>=250):
    print('Yes')
elif (has_id=='No') & (money>=500):
    print('Yes')
elif (has_id=='Yes') & (money<250):
    print('No')
elif (has_id=='No') & (money<500):
    print('No')

# Quotas to the Olympics
# Problem Statement:
# Athlete Slavik wants to earn Olympic quotas for his country. To do so, he competes in the World Championship and the
# European Championship. The rules are as following:
# 1. In order to ensure a trip to the Olympics, an athlete must be in the top 20 of the World Championship AND in the top
# 16 of the European Championship.
# - If an athlete is in the top-10 of at least one of the championships, they will get 2 quotas for their country.
# - If they are in the top-2 of at least one of the championships, they get 3 quotas.
# 1. If an athlete qualifies in the top 24 of the World Championships OR in the top 20 of the European Championships, they
# may go for a further qualifying competition, where they will have one more chance to win a quota.
# 2. Otherwise, the athlete does not receive a quota to the Olympic Games for their country.
# Write a code that determines whether Slavik has won a quota for the Olympic Games.
# Input Format:
# - Two positive integers, each on a new line – Slavik’s places at the World Championship and the European Championship,
# respectively.
# Output Format:
# - If Slavik has won a quota, print "Hurray! The Olympic quotas are won!", followed by the number of quotas on a new line.
# - If Slavik qualifies for an extra qualifier, output "Must participate in a qualifying competition".
# - Otherwise, output "Unfortunately, this time it was not possible to win an Olympics quota".

world=int(input())
euro=int(input())

if (world<=20 and world >=1) & (euro<=16 and euro>=1):
            
    if (world<=2 and world>=1) | (euro<=2 and euro>=1):
        
        print("Hurray! The Olympic quotas are won!\n3")
    
    elif (world<=10 and world>=3) | (euro<=10 and euro>=3):
        
        print("Hurray! The Olympic quotas are won!\n2")
        
    else:
        
        print("Hurray! The Olympic quotas are won!\n1")
        
elif (world<=24 and world>=21) | (euro<=20 and euro>=17):
    
    print("Must participate in a qualifying competition")
else:
    
    print("Unfortunately, this time it was not possible to win an Olympics quota")








