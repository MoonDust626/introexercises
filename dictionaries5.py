#6.8
donut = {'animal':'dog',
'owner':'Jenny',
}

ladybird = {'animal':'dog',
'owner':'Hank Hill',
}

pets = [donut, ladybird]

for pet in pets:
    print('One ' + pet['animal'] + ' is owned by ' + pet['owner'])

print('///')

#6.9
favorite_places = {
    'alan':['santa barbara', 'alhambra', 'hong kong'],
    'peter':['irvine', 'san diego'],
    'edmund':['hong kong', 'paris'],
}

for person, places in favorite_places.items():
    places_str = ''
    for i in range(len(places)):
        if i == len(places) - 1: #last item in list
            places_str = places_str + 'and ' + places[i].title()
        else:
            places_str = places_str + places[i].title() + ', '
    print(person.title() + '\'s ' + 'favorite places are ' + places_str + '.')

print(len(favorite_places['alan']))

#6.10
favorite_number = {
    'Alan': ['8', '11', '13131'],
    'Philip': ['5', '10'],
    'Mom': ['10', '1'],
    'Peter': ['1337', '324'],
    'Jesus': ['168', '312563'],
    }

for person, numbers in favorite_number.items():
    print(person + '\'s' + ' favorite numbers are ' )
    for number in numbers:
        print('\t' + number)

#6.11
cities = {
    'los angeles':{
        'country':'us',
        'population':'14 million',
        'fun fact':'has a large aerospace industry',
    },
    'beijing':{
        'country':'china',
        'population':'20 million',
        'fun fact': 'capitol of a oppressive regime',
    },
    'Johannesburg':{
        'country':'south africa',
        'population':'5.8 million',
        'fun fact': 'home of district 9',
    }
}

for city,city_info in cities.items():
    print(city.title())
    for city_info_key,city_info_value in city_info.items():
        print('\t' + city_info_key.title() + ': ' + city_info_value)