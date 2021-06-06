prompt = 'What is your age?'
prompt += '\nEnter quit to exit\n>>>'


# while True:
#     user_input = input(prompt)
#     if user_input == 'quit':
#         break
#     try:
#         user_input = int(user_input)
#         if user_input <= 3:
#             print('You are free to go')
#         elif user_input > 3 and user_input < 12:
#             print('The price is $10')
#         elif user_input >= 12:
#             print('the price is $15')
#     except:
#         print('you really fucked up')
#         continue

while True:
    user_input = input(prompt)
    if user_input == 'quit':
        break

    if user_input.isnumeric() == True:
        user_input = int(user_input)
    else:
        print('you really fucked up')
        continue
        
    if user_input <= 3:
        print('You are free to go')
    elif user_input > 3 and user_input < 12:
        print('The price is $10')
    elif user_input >= 12:
        print('the price is $15')





