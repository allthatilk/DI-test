# WIP
import requests
import csv

class CountryData:
    def __init__(self, csvfile, iso_code):
        self.csvfile = csvfile
        self.iso_code = iso_code.upper()
        self.dataset = self.createDataset()

    def createDataset(self):
        """Creates dataset from csv file"""
        with open(self.csvfile, 'r') as f:
            self.dataset = csv.DictReader(f)
            year = []
            value = []
            for row in self.dataset:
                if row['id'] == self.iso_code:
                    year.append(row['year'])
                    value.append(row['value'])

            self.dataset = zip(year, value)

    def listData(self):
        """Returns a formatted string of years and values for the given ISO"""
        dataset = list(self.dataset)
        formatted_data = []
        for data in dataset:
            formatted_data.append(data[0] + ' | ' + data[-1])
        result =  ('\n'.join(formatted_data))
        return result
