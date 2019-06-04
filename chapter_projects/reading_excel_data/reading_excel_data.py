#! /usr/bin/env python3
# reading_excel_data.py - tabulates population and number of census
# tracts for each county

import pprint

import openpyxl

print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']

# county_data[stave abbrev][county]['tracts']
# county_data[stave abbrev][county]['population']
county_data = {}

# iterates over each row and calculates tracts/population
for row in range(2, sheet.max_row + 1):
    # each row in the sheet has data for one census tract
    state = sheet[f'b{row}'].value
    county = sheet[f'c{row}'].value
    population = sheet[f'd{row}'].value

    # ensures the key for this state exists
    county_data.setdefault(state, {})
    # ensures key for this county exists
    county_data[state].setdefault(county, {'tracts': 0, 'population': 0})

    # increment tract count and population accordingly
    county_data[state][county]['tracts'] += 1
    county_data[state][county]['population'] += int(population)

print('Writing results...')
with open('census2010.py', 'w') as result:
    result.write(f'all_data = {pprint.pformat(county_data)}')
print('Done.')
