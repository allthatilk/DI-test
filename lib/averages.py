import math

class Averages:
    def __init__(self, country_data):
        self.country_data = country_data.dataset
        self.data = self.prepData()

    def prepData(self):
        """Formats given dataset for averaging methods"""
        scores = []
        for data in self.country_data:
            scores.append(float(data[-1]))
        return scores

    def mean(self):
        """Returns mean average of all GAI scores for all available years"""
        length = len(self.data)
        total_value = sum(self.data)
        result = total_value / length
        return result

    def range(self):
        """Returns range of GAI scores"""
        sorted_scores = sorted(self.data)
        result = sorted_scores[-1] - sorted_scores[0]
        return result


    def standardDeviation(self):
        """Returns standard deviation for GAI scores"""
        subtracted_scores = []
        for score in self.data:
            subtracted_scores.append((score - self.mean())**2)
        sum_subtracted_scores = sum(subtracted_scores)
        length = len(subtracted_scores)
        sd_mean = sum_subtracted_scores / length
        result = math.sqrt(sd_mean)
        return result
