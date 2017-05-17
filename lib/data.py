import requests
import csv

class Data:
    def __init__(self, url):
        self.url = url
        self.dataset = self.create_dataset()

    def create_dataset(self):
        """Creates dataset from csv url"""
        csv_download = requests.get(self.url)
        self.dataset = csv.DictReader(csv_download.content.decode('utf-8'))
