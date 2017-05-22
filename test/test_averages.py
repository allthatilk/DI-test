from lib.averages import Averages
from test.test_data import mock

averages = Averages(mock())

def test_Averages():
    """Tests to see that Averages class can be instantiated"""
    assert averages.country_data == [('2000', '0.3'), ('2001', '0.4'), ('2002', '0.1'), ('2003', '0.2')]

def test_prepData():
    """Tests to see that prepData returns scores in desired format"""
    averages.prepData()
    assert averages.data == [0.3, 0.4, 0.1, 0.2]

def test_mean():
    """Tests to see that mean returns the mean"""
    assert averages.mean() == 0.25







# range returns the range

# standardDeviationData returns the standard deviation from the mean
