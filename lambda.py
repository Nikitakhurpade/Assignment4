#Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.
#sample input: 10
#sample output: 35
argument=int(input('Input : Enter the Number : '))
add = lambda a : a + 25
print('Adding 25 to entered number')
print ('Output : ',argument,'+ 25 =', add(argument))

