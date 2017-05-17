# WIP
from lib.data import CountryData
from lib.averages import Averages

print("Global Adaptation Index data for Afghanistan\n")

country_data = CountryData('lib/gai.csv', "AF")
country_data.createDataset()
print("List of available GAI scores for available years:")
print(country_data.listData())

averages = Averages(country_data)
averages.prepData
print("\nMean Score:")
print(averages.mean())
print("\nScore Range:")
print(averages.range())
print("\nStandard Deviation from the Mean:")
print(averages.standardDeviation())
