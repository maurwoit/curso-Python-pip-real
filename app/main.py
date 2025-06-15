import utils
import read_csv
import charts



def run():
  data = read_csv.read_csv('data.csv')

  '''
  data = list(filter(lambda item: item['Continent'] == 'South America', data))
  
  labels, values = utils.get_countries_vs_percent(data)
  charts.generate_pie_chart(labels, values)

  '''
  
  #ESTE CODIGO GENERA UNA GRAFICA DE POBLACION POR PAIS

  data = read_csv.read_csv('data.csv')
  country = input(f'Selecciona un pais =>')
  result = utils.get_population_by_country(data, country)
  #print (result)
  countryName = country

  
  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(countryName, labels, values)
  
  
    

if __name__ == '__main__':
  run() 
#esto ejecuta cuando se llama desde la terminal