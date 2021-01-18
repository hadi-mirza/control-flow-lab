# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month = input('Enter the month of the year (Jan - Dec): ')
day = input('Enter the day of the month: ')
day = int(day)


if month in ('dec', 'Dec'):
    if day < 21:
        print(f'{month} {day} is in Fall')
    else:
        print(f'{month} {day} is in Winter')
elif month in ('mar', 'Mar'):
    if day < 20:
        print(f'{month} {day} is in Winter')
    else:
        print(f'{month} {day} is in Spring')
elif month in ('jun', 'Jun'):
    if day < 21:
        print(f'{month} {day} is in Spring')
    else:
        print(f'{month} {day} is in Summer')
elif month in ('sep', 'Sep'):
    if day < 21:
        print(f'{month} {day} is in Summer')
    else:
        print(f'{month} {day} is in Fall')
elif month in ('jan', 'feb', 'Jan', 'Feb'):
    print(f'{month} {day} is in Winter')
elif month in ('apr', 'may', 'Apr', 'May'):
    print(f'{month} {day} is in Spring')
elif month in ('jul', 'aug', 'Jul', 'Aug'):
    print(f'{month} {day} is in Summer')
elif month in ('oct', 'nov', 'Oct', 'Nov'):
    print(f'{month} {day} is in Fall')
else:
    print('Please enter the month (as three characters)')