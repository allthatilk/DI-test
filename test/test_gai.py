from lib.gai import extractData, listData, meanData, rangeData, standardDeviationData
import os.path

def test_loadcsv():
    """Test to check csv file downloads with method"""
    url = "https://raw.githubusercontent.com/devinit/digital-platform/master/country-year/climate-vulnerability.csv"
    loadcsv(url)
    assert os.path.isfile('lib/gai.csv') == True

def test_extractData():
    data = list(extractData("AE"))
    assert data == [('2000', '0.30251184'), ('2001', '0.302267024'), ('2002', '0.303079269'), ('2003', '0.297885987'), ('2004', '0.305190096'), ('2005', '0.310410195'), ('2006', '0.297995201'), ('2007', '0.296620561'), ('2008', '0.305768368'), ('2009', '0.297571739'), ('2010', '0.29877485'), ('2011', '0.29857415'), ('2012', '0.29837345'), ('2013', '0.298276917')]

def test_listData():
    """Test to check method returns all data for given ISO code"""
    assert listData("AE") == '2000 | 0.30251184\n2001 | 0.302267024\n2002 | 0.303079269\n2003 | 0.297885987\n2004 | 0.305190096\n2005 | 0.310410195\n2006 | 0.297995201\n2007 | 0.296620561\n2008 | 0.305768368\n2009 | 0.297571739\n2010 | 0.29877485\n2011 | 0.29857415\n2012 | 0.29837345\n2013 | 0.298276917'

def test_meanData():
    """Test to check method gives correct mean average of all GAI scores for given ISO code"""
    assert meanData("AE") == 0.30094997478571434

def test_rangeData():
    """Test to check method gives correct range of all GAI scores for given ISO code"""
    assert rangeData("AE") == 0.013789633999999995

def test_standardDeviationData():
    """Test to check method give correct standard deviation of GAI scores for given ISO code"""
    assert standardDeviationData("AE") == 0.0038898556912647137
