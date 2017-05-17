"""Script to return Global Adaptation Index (GAI) data by country."""
import csv
import requests

def loadcsv(url):
    csv_download = requests.get(url)

    with open('lib/gai.csv', 'w') as f:
        f.writelines(csv_download.content.decode('utf-8'))

def listData(iso_code):
    """Extracts data from csv file and returns a formatted string of years and values for the given ISO"""
    with open('lib/gai.csv', 'r') as f:
        reader = csv.DictReader(f)
        data = []
        for row in reader:
            if row['id'] == iso_code:
                 data.append(row['year'] + ' | ' + row['value'])
    result =  ('\n'.join(data))
    return result
    # Maybe something like while ID == string return row sort of thing? Or values for year and gai score in row...

def averageData(iso_code):
    """Returns an average of all GAI scores for all available years for a given country"""
    # Will need to use listData to get gai scores and then some kind of inject method to average unless python has
    # a mean function built in. Will need to iterate through list output to turn gai scores into seperate array...
    pass

def returnDataOptions(iso_code):
    """Takes an ISO code as an argument and returns options for data"""
    pass
