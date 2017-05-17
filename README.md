# Development Initiatives Test

## How to:
* clone this repo
* create and load virtual environment in local directory
* run python
* run:
```
from lib.gai import loadcsv, extractData, listData, meanData, rangeData, standardDeviationData
```
* before all other methods run to make sure data is up to date:
```
loadcsv("https://raw.githubusercontent.com/devinit/digital-platform/master/country-year/climate-vulnerability.csv")
```
* use the listData, meanData, rangeData, and standardDeviationData methods to manipulate csv data in REPL eg. listData("AE") which will return the available data for the United Arab Emirates

	All methods need an ISO code as an argument

## Task

Using Python, write functionality that takes any ISO country code as input, and can return for the given country:
	* A list of Global Adaptation Index scores for all available years
	* The average of all Global Adaptation Index scores for all available years

There's no need to return the country text name (e.g. Andorra if the input country code was AD)

[Global Adaptation Index CSV](https://github.com/devinit/digital-platform/blob/master/country-year/climate-vulnerability.csv "GAI CSV")

## Technologies

* Python (with csv module)
* Pytest

## Comments on Task

Time taken: ~9 hours

### Decisions:
* Created a method to loadcsv file so data can be updated in future if needed
* Extracted data extraction from csv to a method that other methods depend on to make code more DRY and keep to SRP
* Removed returnDataOptions method as task specifies that data will feed into external interface so a command line UI isn't needed
* Added range and standard deviation because why not? But really because they gave a good indication of how the data has changed over time in relation to the mean value.
* Didn't add mode or median because they didn't seem useful for this data set as scores didn't repeat and the middle score would have given more of a time snapshot than any useful data on score trends
* Didn't want to finish with no working code so experimented with refactoring in separate files but ran out of time for writing new tests


### Challenges:
* Getting used to the csv module
* Incomplete Python knowledge
* Extracting the data in a useful way
* Remembering how to do averages... it's been a while.
* Problems with zip on refactoring(can only use list on zip once per dataset generation)
* Not enough time to write tests for refactored code
