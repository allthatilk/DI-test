from lib.data import CountryData
from lib.averages import Averages

print("Global Adaptation Index data for selected country")

country_data = CountryData("https://raw.githubusercontent.com/devinit/digital-platform/master/country-year/climate-vulnerability.csv")

def chooseCountry(iso_code):
    country_data.createDataset(iso_code.upper())

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

iso_code = input("Please provide a country's ISO code:\n")
chooseCountry(iso_code)
while iso_code != 'quit':
    iso_code = input("\nType 'quit' to exit, or type another ISO code:\n")
    chooseCountry(iso_code) if iso_code != 'quit' else quit()

# Implemented functionality for user to select country as script runs in command line after comment made at interview
