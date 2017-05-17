import requests
import csv

class Data:
    def __init__(self, url):
        self.url = url


    def loadcsv(self):
        """Rewrites csv file with data from given URL"""
        csv_download = requests.get(self.url)
        with open('lib/gai.csv', 'w') as f:
            f.writelines(csv_download.content.decode('utf-8'))

    def extractData(self):
        """Extracts data from csv file"""
        with open('lib/gai.csv', 'r') as f:
            reader = csv.DictReader(f)
            ids = []
            years = []
            values = []
            for row in reader:
                ids.append(row['id'])
                years.append(row['year'])
                values.append(row['value'])

            dataset = zip(ids, years, values)
            return dataset
