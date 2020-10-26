countries = {
    'colombia': 60,
    'mexico':122,
    'chile': 19,
    'peru': 31
}

while True:
    country = input('Escribe el nombre de un pais: ').lower()
    try:
        print('La poblacion de {} es de {}'.format(country, countries[country]))
    except KeyError:
        print('No tenemos el dato de la poblaciòn del pais seleccionado')
        