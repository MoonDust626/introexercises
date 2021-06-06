def city_country(city, country):
    location = city.title() + ', ' + country.title()
    return(location)
place = city_country('alhambra', 'united states')
print(place)
place = city_country('quebec', 'canada')
print(place)
place = city_country('hanoi', 'vietnam')
print(place)