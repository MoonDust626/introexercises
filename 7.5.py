prompt = 'What is your age?'

age = input(prompt)

while True:
    if age < 3:
        print('You are free to go')

    elif age > 3 and < 12:
        print('The price is $10')

    elif age > 12:
        print('the price is $15')