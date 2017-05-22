from lib.data import CountryData
import requests
import requests_mock

data = "id,year,value\nTE,2000,0.3\nTE,2001,0.4\nTE,2002,0.1\nTE,2003,0.2"

# need to look into requests.get to figure out how to mock csv data
def test_CountryData():
    """Test to see that CountryData class can be instantiated"""
    url = 'this is a URL'
    country = CountryData(url)
    assert country.url == 'this is a URL'

def test_createDataset():
    with requests_mock.mock() as m:
        m.get('http://test.com', text=data)
        country = CountryData('http://test.com')
        country.createDataset("TE")
        assert country.dataset == [('2000', '0.3'), ('2001', '0.4'), ('2002', '0.1'), ('2003', '0.2')]

# createDataset returns dataset for given country_data
#
#     assert data ==

# listData returns a list of years and GAI scores for specified ISO code
