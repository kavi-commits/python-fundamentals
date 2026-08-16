print('Enter TB or GB for the advertied unit')
unit = input('>')

# calculate the amount that the advertisedd capasity lies:
if unit == 'TB' or unit == 'tb':
    discrepancy = 10000000000 / 1099511627776
elif unit == 'GB'or unit == 'gb':
    discrepancy = 10000000000 / 1073741824

print('Enter the advertised capasity:')
advertised_capasity = input('>')
advertised_capasity = float(advertised_capasity)

# calculate the reeal capasity, round ti to nearest hundredths,
# and convert it to a string so ti can be concatenated:
real_capasity = str(round(advertised_capasity * discrepancy, 2))

print('the actual capasity is '+real_capasity+''+ unit)



print('Enter the test marks')
marks = input('>')
marks = int(marks)

if marks>=71:
    if marks>=85:
        print('Your grade is A+')
    elif marks>=75:
        print('Your grade is A')
    else:
        print('Your grade is A-')
    
elif marks>=61:
    if marks>=68:
        print('Your grade is B+')
    elif marks>=65:
        print('Your grade is B')
    else:
        print('Your grade is B-')

elif marks>=50:
    if marks>=58:
        print('Your grade is C+')
    elif marks>=55:
        print('Your grade is C')
    else:
        print('Your grade is C-')
         
elif marks>=35:
    if marks>=45:
        print('Your grade is E+')
    else:
        print('Your grade is E')
else:
    print('Your are failed the exam')


print('Enter the number')
num= input('>')
num= int(num)

if num>0:
    if num%2==0:
        print('The number is Even and Positive')
    else:
        print('The number is Odd and Positive')
elif num<0:
    if num%2==0:
        print('The number is Even and Negative')
    else:
        print('The number is Odd and Negative')
else:
    print('The numberr is Zero')

