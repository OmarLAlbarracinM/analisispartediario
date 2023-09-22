import utils

def run():
    data = utils.read_csv('parte_diario.csv')
    name = 'ST. YESICA LORENA POLANCO ANDRADE'
    user = list(filter(lambda item: item['Modificado por'] == name, data))
    ubicacion  = list(map(lambda item: item['UBICACION'], data))
    n = ubicacion.count('FILA')

    # countries = list(map(lambda x: x['Country'], data))
    # percentages = list(map(lambda x: x['World Population Percentage'], data))
    # utils.generate_bar_chart(ubicacion, name)

if __name__ == '__main__':
    run()
