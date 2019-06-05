from census2010 import all_data

total_tracts = 0
total_population = 0

print(f"Printing summary for Indiana in the following form:"
      f"\n{'[county], IN:':>16} {'[tracts]'} {'[population]'}\n")

for county in all_data['IN'].keys():
    print(f"{county + ', IN:':>16}\t{all_data['IN'][county]['tracts']:3,d} "
          f"\t{all_data['IN'][county]['population']:7,d}")
    total_tracts += all_data['IN'][county]['tracts']
    total_population += all_data['IN'][county]['population']

print(f"\nSummary of census data for Indiana:"
      f"\n\t{'Census tracts:':<14} {total_tracts:9,d}"
      f"\n\t{'Population:':<14} {total_population:9,d}")
