"""Script to return Global Adaptation Index (GAI) data by country."""
import csv
import requests

def loadcsv(url):
    csv_download = requests.get(url)

    with open('lib/gai.csv', 'w') as f:
        f.writelines(csv_download.content.decode('utf-8'))

def extractData(iso_code):
    """Extracts data from csv file"""
    with open('lib/gai.csv', 'r') as f:
        reader = csv.DictReader(f)
        year = []
        value = []
        for row in reader:
            if row['id'] == iso_code:
                year.append(row['year'])
                value.append(row['value'])

        dataset = zip(year, value)
        return dataset

def listData(iso_code):
    """Returns a formatted string of years and values for the given ISO"""
    dataset = list(extractData(iso_code))
    formatted_data = []
    for data in dataset:
        formatted_data.append(data[0] + ' | ' + data[-1])
    result =  ('\n'.join(formatted_data))
    return result

def averageData(iso_code):
    """Returns an average of all GAI scores for all available years for a given country"""
    pass

def returnDataOptions(iso_code):
    """Takes an ISO code as an argument and returns options for data"""
    pass
