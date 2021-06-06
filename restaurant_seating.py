dinner_group = input('How many people are in your dinner group?')
dinner_group = int(dinner_group)
if dinner_group >= 8:
    print('\nPlease wait to be seated')
else:
    print('\nYour table is ready')
