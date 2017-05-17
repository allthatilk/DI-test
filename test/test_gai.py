from lib.gai import loadcsv, returnDataOptions, listData, averageData
import os.path

def test_loadcsv():
    """Test to check csv file downloads with method"""
    url = "https://raw.githubusercontent.com/devinit/digital-platform/master/country-year/climate-vulnerability.csv"
    loadcsv(url)
    assert os.path.isfile('lib/gai.csv') == True

def test_listData():
    """Test to check method returns all data for given ISO code"""
    assert listData("AE") == '2000 | 0.30251184\n2001 | 0.302267024\n2002 | 0.303079269\n2003 | 0.297885987\n2004 | 0.305190096\n2005 | 0.310410195\n2006 | 0.297995201\n2007 | 0.296620561\n2008 | 0.305768368\n2009 | 0.297571739\n2010 | 0.29877485\n2011 | 0.29857415\n2012 | 0.29837345\n2013 | 0.298276917'
