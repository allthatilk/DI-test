import requests
import csv

class CountryData:
    def __init__(self, url):
        self.url = url
        self.dataset = []

    def createDataset(self, iso_code):
        csv_download = requests.get(self.url)
        data = csv_download.content.decode('utf-8')
        result = data.split('\n')
        data = []
        self.dataset = csv.DictReader(result)
        for row in self.dataset:
            if row['id'] == iso_code:
                data.append((row['year'], row['value']))

        self.dataset = data

    def listData(self):
        """Returns a formatted string of years and values for the given ISO"""
        dataset = list(self.dataset)
        formatted_data = []
        for data in dataset:
            formatted_data.append(data[0] + ' | ' + data[-1])
        result =  ('\n'.join(formatted_data))
        return result
