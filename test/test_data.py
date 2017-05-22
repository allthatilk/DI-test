from lib.data import CountryData
import requests
import requests_mock


def mock():
    data = "id,year,value\nTE,2000,0.3\nTE,2001,0.4\nTE,2002,0.1\nTE,2003,0.2"
    with requests_mock.mock() as m:
        m.get('http://test.com', text=data)
        country = CountryData('http://test.com')
        country.createDataset('TE')
        return country

def test_CountryData():
    """Test to see that CountryData class can be instantiated"""
    url = 'this is a URL'
    country = CountryData(url)
    assert country.url == 'this is a URL'

def test_createDataset():
    """Test to see that the dataset builds as expected"""
    country = mock()
    assert country.dataset == [('2000', '0.3'), ('2001', '0.4'), ('2002', '0.1'), ('2003', '0.2')]

def test_listData():
    """Test to see that listData returns a list of years and GAI scores for specified ISO code"""
    country = mock()
    assert country.listData() == '2000 | 0.3\n2001 | 0.4\n2002 | 0.1\n2003 | 0.2'
