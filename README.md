# Development Initiatives Test

## How to:
	* clone this repo
	* create and load virtual environment in local directory
	* pip install requirements.txt
	* load python REPL
	* from lib.gai import loadcsv, extractData, listData, meanData, rangeData
	* before all other methods run loadcsv(https://raw.githubusercontent.com/devinit/digital-platform/master/country-year/climate-vulnerability.csv)
	* use the listData, meanData, and rangeData methods to manipulate csv data in REPL

## Task

```
Using Python, write functionality that takes any ISO country code as input, and can return for the given country:
	* A list of Global Adaptation Index scores for all available years
	* The average of all Global Adaptation Index scores for all available years

There's no need to return the country text name (e.g. Andorra if the input country code was AD)
```

[Global Adaptation Index CSV](https://github.com/devinit/digital-platform/blob/master/country-year/climate-vulnerability.csv "GAI CSV")

## Technologies

* Python (with csv module)
* Pytest

## Comments on Task

Time taken: ~6 hours

Decisions:
	* Created a method to loadcsv file so data can be updated in future if needed
	* Extracted data extraction from csv to a method that other methods depend on to make code more DRY and keep to SRP
	* Removed returnDataOptions method as task specifies that data will feed into external interface so a command line UI isn't needed
	* Added range because why not?


Challenges:
	* Getting used to the csv module
	* Incomplete Python knowledge
	* Extracting the data in a useful way
