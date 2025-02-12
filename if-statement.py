# Exercise 1: Movie Ticket Price Calculator
age = int(input('Enter your age: '))

if age <= 10 :
  print('The ticket price is $5')
elif age <= 15:
  print('The ticket price is $8')
elif age <= 20:
  print('The ticket price is $11')
elif age <= 25:
  print('The ticket price is $14')
else:
  print('The ticket price is $19')


# Exercise 2: Even or Odd Number Checker

num = int(input('Enter a number: '))

if num%2 == 0 :
  print('The number is even')
else:
  print('The number is odd')

# Exercise 2: Simple Login System

username = input('Enter username: ')
password = input('Enter password: ')

if username == 'admin' and password == '1234' :
  print('Access granted')
else:
  print('Access denied')