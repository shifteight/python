def get_city_info(city, country, population=None):
    
    city_info = (city + ', ' + country).title()
    if population:
        city_info = city_info + ' - population ' + str(population)
    return city_info