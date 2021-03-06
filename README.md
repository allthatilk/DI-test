# Development Initiatives Test

## How to:

* clone this repo
* create and load virtual environment in local directory
* install requirements:
```
pip install -r requirements.txt
```
```
python run.py
```
Enjoy!

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

### Refactoring in progress
* Separated responsibilities in original code to CountryData and Averages classes
* All methods tested
* After feedback made it so users can continue to select country info via ISO code until they choose to quit program
* Finally got rid of the need for a CSV file. Though the climate-vulnerability.csv URL is hardcoded into the run file currently, purely to avoid errors from URLs with invalid formats being passed to the method
* Looking to add some kind of URL data validation to allow URLs to be passed in as long as they have the correct format in the future
* Need to add error handling for when users enter an ISO code that doesn't have any associated values
