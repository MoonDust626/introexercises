responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would you go?")

#store the response in the dictionary:
    responses[name] = response

# Find out if anyone else is going to take the poll.
    repeat = input('Would you like to let another person respond? (yes/ no) ')
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print('\n--- Poll Results ---')
for name, response in responses.items():
    print(name + ' would like to visit ' + response + '.')