import pandas as pd
import geopandas as gpd

european_countries = [
    'Albania', 'Azerbaijan', 'Andorra', 'Armenia', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina',
    'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France',
    'Georgia', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia', 
    'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Montenegro', 'Netherlands', 
    'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'Serbia', 
    'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'Ukraine', 'United Kingdom'
]

def cleaner(data, countries=european_countries):

    data = pd.read_csv("./data/alcohol-consumption.csv")

    for index, country in data['country'].items():
        if country not in european_countries:
            # Usuń wiersz, jeśli kraj nie jest w Europie
            data.drop(index, inplace=True)

    # for index, total_alcohol in data['total_litres_of_pure_alcohol'].items():
    #     if total_alcohol <= 0.001:
    #         data.drop(index, inplace=True)

    data = data.sort_values(by='country')
    data = data.reset_index(drop=True)
    data = data.drop(columns=['2020_projection' ,'2025_projection'])

    # print(data)
    # print(len(european_countries))
    # print(len(data))

    return data

def geo_cleaner(geodata, countries=european_countries):

    geodata = gpd.read_file('./europe.geojson')

    for index, country in geodata['NAME'].items():
        if country == 'The former Yugoslav Republic of Macedonia':
            geodata.at[index, 'NAME'] = 'North Macedonia'
        if country == 'Republic of Moldova':
            geodata.at[index, 'NAME'] = 'Moldova'

    for index, country in geodata['NAME'].items():
        if country not in countries:
            geodata.drop(index, inplace=True)

    geodata.rename(columns={'NAME': 'country'}, inplace=True)

    geodata = geodata.sort_values(by='country')
    geodata = geodata.reset_index(drop=True)

    print(geodata['country'])

    return geodata