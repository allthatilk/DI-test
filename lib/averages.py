import math

class Averages:

    def __init__(self, dataset, iso_code):
        self.dataset = dataset
        self.iso_code = iso_code

    def prepData(self):
        """Formats given dataset for averaging methods"""
        dataset = list(extractData(self.iso_code))
        scores = []
        for data in dataset:
            scores.append(float(data[-1]))
        return scores

    def mean(self):
        """Returns mean average of all GAI scores for all available years"""
        scores = prepDataForAverages()
        length = len(scores)
        total_value = sum(scores)
        result = total_value / length
        return result

    def range(self):
        """Returns range of GAI scores"""
        scores = prepDataForAverages()
        sorted_scores = sorted(scores)
        result = sorted_scores[-1] - sorted_scores[0]
        return result


    def standardDeviation(self):
        """Returns standard deviation for GAI scores"""
        scores = prepDataForAverages()
        mean = meanData(iso_code)
        subtracted_scores = []
        for score in scores:
            subtracted_scores.append((score - mean)**2)
        sum_subtracted_scores = sum(subtracted_scores)
        length = len(subtracted_scores)
        sd_mean = sum_subtracted_scores / length
        result = math.sqrt(sd_mean)
        return result
