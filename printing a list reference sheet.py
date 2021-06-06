magicians = ['John', 'Carrie']

# for/in loop: easiest way to print a list
for magician in magicians:
    print(magician)

# for loop with range: print a list, but you can also modify it
magiciansLength = len(magicians)
for i in range(magiciansLength):
    print(magicians[i])

# printing a list with a while loop. can also modify the loop
index = 0
while index < len(magicians):
    print(magicians[index])
    index = index + 1