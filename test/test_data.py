from lib.data import CountryData
import requests_mock

data = "id,year,value\nTE,2000,0.3\nTE,2001,0.4\nTE,2002,0.1\nTE,2003,0.2"

# need to look into requests.get to figure out how to mock csv data
def test_CountryData():
    """Test to see that CountryData class can be instantiated"""
    url = 'this is a URL'
    country = CountryData(url)
    assert country.url == 'this is a URL'

# def test_createDataset():
#     adapter = requests_mock.Adapter()
#     adapter.register_uri('GET', 'mock://test.com/path', text=data)
#     country = CountryData('mock://test.com/path')

# createDataset returns dataset for given country_data
#
#     assert data ==

# listData returns a list of years and GAI scores for specified ISO code
