alien_0 = {'color': 'green'}
print('The alien is ' + alien_0['color'] + '.')

alien_0['color'] = 'yellow'
print('The alien is now ' + alien_0['color'] + '.')

print('///')

alien_1 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print('Original x_position: ' + str(alien_1['x_position']))

alien_1['speed'] = 'fast'

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.

if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.


alien_1['x_position'] = alien_1['x_position'] + x_increment

print('New x_position: ' + str(alien_1['x_position']))

print('///')

alien_2 = {'color': 'green', 'points': 5}
print(alien_2)

del alien_2['points']
print(alien_2)


print('///')

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("Sarah's favorite language is " +
    favorite_languages['sarah'].title() + 
    '.')

print('///')

phil_info = {
    'first_name': 'Philip',
    'last_name': 'Chiang',
    'age': 27,
    'city': 'Alhambra',
    }

print(phil_info['first_name'], phil_info['last_name'], phil_info['age'], phil_info['city'], sep = '\n') #sep is a named argument

print('///')

favorite_number = {
    'Alan': '8', '11'
    'Philip': '5', '10'
    'Mom': '10',
    'Peter': '1337',
    'Jesus': '168',
    }

print('Alan\'s favorite number is ' + favorite_number['Alan'])
print('Philip\'s favorite number is ' + favorite_number['Philip'])
print('Mom\'s favorite number is ' + favorite_number['Mom'])
print('Peter\'s favorite number is ' + favorite_number['Peter'])
print('Jesus\'s favorite number is ' + favorite_number['Jesus'])

programming_words = {
    'Boolean': 'a true or false',
    'Integer': 'usually a whole number',
    'Variable': 'a name you can set to a label for a thing in programming',
    'List': 'like variable, but with more things inside',
    'Dictionary': 'similar to key value pairs, like list but better',
}

print('Boolean is ' + programming_words['Boolean'])
print('Integer is ' + programming_words['Integer'])
print('Variable is ' + programming_words['Variable'])
print('List is ' + programming_words['List'])
print('Dictionary is ' + programming_words['Dictionary'])