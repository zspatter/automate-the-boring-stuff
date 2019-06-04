from census2010 import all_data

total_tracts = 0
total_population = 0

print(f'Printing summary for Indiana in the following form: [county], IN: [tracts] [population]\n')

for county in census2010.all_data['IN'].keys():
    print(f"{county}, IN: {census2010.all_data['IN'][county]['tracts']}"
          f"{census2010.all_data['IN'][county]['population']}")
    total_tracts += census2010.all_data['IN'][county]['tracts']
    total_population += census2010.all_data['IN'][county]['population']

print(f'\nSummary of census data for Indiana:'
      f'\tCensus tracts: {total_tracts}\tPopulation: {total_population}')
