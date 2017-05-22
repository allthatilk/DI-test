from lib.averages import Averages
from test.test_data import mock

def test_Averages():
    """Tests to see that Averages class can be instantiated"""
    averages = Averages(mock())
    assert averages.country_data == [('2000', '0.3'), ('2001', '0.4'), ('2002', '0.1'), ('2003', '0.2')]

def test_prepData():
    """Tests to see that prepData returns scores in desired format"""
    averages = Averages(mock())
    averages.prepData()
    assert averages.data == [0.3, 0.4, 0.1, 0.2]



# mean returns the mean

# range returns the range

# standardDeviationData returns the standard deviation from the mean
