def city_country(city, country):
    location = city.title() + ', ' + country.title()
    return(location)
place = city_country('alhambra', 'united states')
print(place)