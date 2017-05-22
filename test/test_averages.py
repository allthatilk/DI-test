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

def test_range():
    """Test to see that range returns the range"""
    assert averages.range() == 0.30000000000000004

def test_standardDeviation():
    """Test to see that standardDeviation returns the standard deviation from the mean"""
    assert averages.standardDeviation() == 0.11180339887498948
