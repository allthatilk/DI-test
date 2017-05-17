# WIP
from lib.data import CountryData
from lib.averages import Averages

country_data = CountryData('lib/gai.csv', "AE")
country_data.createDataset()
print(country_data.listData())

averages = Averages(country_data)
averages.prepData
print(averages.mean())
print(averages.range())
print(averages.standardDeviation())
