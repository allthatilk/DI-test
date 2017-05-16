from lib.gai import loadcsv, returnDataOptions, listData, averageData
import os.path
# first test = csv file loads?

def test_loadcsv():
    """Test to check csv file downloads with method"""
    url = "https://raw.githubusercontent.com/devinit/digital-platform/master/country-year/climate-vulnerability.csv"
    loadcsv(url)
    assert os.path.isfile('gai.csv') == True

# or ISO code returns correct data set?
