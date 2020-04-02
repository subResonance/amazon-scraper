# Currently only stable on Google Chome Version 80.0.3987.149 (latest 04/01/20)
# MUST retain current directory structure, path to Selenium Chrome driver binary
# is appended to cwd and used to instantiate a webdriver 

# Execute from virtual environment in terminal by running: \Amazon\Scripts\activate.bat
# Otherwise you must configure selenium for your machine before running which is used
# to mimick a browser to pass amazon's automated check for a valid request 

# GOAL: Perform regular price monitoring to create an interface with price history graphs that 
  also allows for custom price drop alerts for a user specified set of amazon products
-----------------------------------------------------------------------------------------------------------------------------------
Changelog

## [1.0] - 2020-03-31
### Added
- amazon_scraper.py
	- Uses automated Google Chrome brower interfaced with Selenium
	- Retrieves all amazon URLs from https://drive.google.com/file/d/1Vu2e_00dniSqkHH9115DP0qeqpwMuR4C/view
	- Information is fetched from each amazon listing via CSS selectors and stored in a collection of dicitionaries in the form
		- ['seller', 'title', 'price', 'rating', 'num_ratings', 'date'] 
		- Output file product_info.json is generated with the retrieved information for each listing
- demo.mp4
	- Simple video demomonstration of execution
	
-----------------------------------------------------------------------------------------------------------------------------------

## [1.1] - 2020-04-01
### Added
- amazon_scraper.py
	- Exception handling for attributes that are not retrived
	- Secondary selector id for the listing's price attributes
	- Indentation and formating for the generated product_info.json
### Changed
- product_urls.txt
	- Updating file by version does in fact retain the original URL
		-  https://drive.google.com/file/d/1Vu2e_00dniSqkHH9115DP0qeqpwMuR4C/view
	- Increased number of listings from 3 -> 15 (without breaking anything :D)
	
-----------------------------------------------------------------------------------------------------------------------------------
