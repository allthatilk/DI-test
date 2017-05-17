# WIP

from lib.data import CountryData
from lib.averages import Averages

country_data = CountryData('lib/gai.csv', "AF")
country_data.createDataset()
country_data.listData

averages = Averages(country_data)
averages.prepData
averages.mean
averages.range
averages.standardDeviation
