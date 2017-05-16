"""Script to return Global Adaptation Index (GAI) data by country."""
import csv
import requests

def loadcsv(url):
    csv_download = requests.get(url)

    with open('gai.csv', 'w') as f:
        f.writelines(csv_download.content.decode('utf-8'))

def returnDataOptions(iso_code):
    """Takes an ISO code as an argument and returns options for data"""
    pass

def listData(country):
    """Lists data available for given country"""
    pass

def averageData(country):
    """Returns an average of all GAI scores for all available years for a given country"""
    pass
