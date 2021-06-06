x = 1
while x <= 5:
    print(x)
    x += 1

#7.4 Pizza Toppings

prompt = 'Enter your favorite toppings: '
message = ''

active = True

while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print('I love putting ' + message + ' on my pizza as well! ')