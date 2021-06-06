#6.4

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for language in set(favorite_languages.values()):
    print(language.title())

programming_words = {
    'Boolean': 'a true or false',
    'Integer': 'usually a whole number',
    'Variable': 'a name you can set to a label for a thing in programming',
    'List': 'like variable, but with more things inside',
    'Dictionary': 'similar to key value pairs, like list but better',
}

for term, definition in programming_words.items():
    print(term + ' is ' + definition)

#6.5

rivers =  {
    'nile': 'egypt',
    'thames': 'england',
    'Mississipi': 'united states',
}

for river, country in rivers.items():
    print('The', river.title(), 'runs through', country.title())

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())

#6.6

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

poll_people = ['jen', 'sarah', 'edward', 'phil', 'bill', 'alan']

for people in poll_people:
    if people in favorite_languages.keys():
        print('Thank you for taking the the poll!')
    else:
        print('Please take the poll!')

# Nesting

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {
    'color': 'green',
    'points': 5,
    'speed': 'slow',
    }
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# show the first 5 aliens:

for alien in aliens[:5]:
    print(alien)
print('...')

# show how many aliens have been created.
print('Total number of aliens: ' + str(len(aliens)))

# Store information about a pizza being ordered

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

#summarize the order.
print('You ordered a ' + pizza['crust'] + "-crust pizza", 'with the following toppings:')

for topping in pizza['toppings']:
    print('\t', topping)