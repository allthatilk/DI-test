from lib.averages import Averages
from test.test_data import mock
# import requests
# import requests_mock

def test_Averages():
    averages = Averages(mock())
    assert averages.country_data == [('2000', '0.3'), ('2001', '0.4'), ('2002', '0.1'), ('2003', '0.2')]

# prepData returns scores in desired formatted

# mean returns the mean

# range returns the range

# standardDeviationData returns the standard deviation from the mean
