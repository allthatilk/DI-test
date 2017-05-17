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

def prepDataForAverages(iso_code):
    dataset = list(extractData(iso_code))
    scores = []
    for data in dataset:
        scores.append(float(data[-1]))
    return scores

def meanData(iso_code):
    """Returns mean average of all GAI scores for all available years for a given country"""
    scores = prepDataForAverages(iso_code)
    length = len(scores)
    total_value = sum(scores)
    result = total_value / length
    return result

def rangeData(iso_code):
    scores = prepDataForAverages(iso_code)
    sorted_scores = sorted(scores)
    result = sorted_scores[-1] - sorted_scores[0]
    return result


def standardDeviationData(iso_code):
    pass
