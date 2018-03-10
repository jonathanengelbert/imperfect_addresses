
# Imperfect Addresses

This script standardizes addresses provided in an excel workbook.

It was first developed to attend the needs of the Urban Planning Department of the City and County of San Francisco, which must follow a specific standard for how official addresses are stored and manipulated.

Although this script is very case-specific, it is flexible enough in its structure to accommodate differente standards for the transformation of other kinds of data.

## Last Modified

The final version of this script was released 01/26/2018.
Subsequent updates may follow as needed.

## Functionality

 1. Tranformations:

 * Address types are abbreviated, following the standards found here:

     https://data.sfgov.org/Geographic-Locations-and-Boundaries/Street-Names/6d9h-4u5v/data

 * Everything to the right of an address type is wiped out (as in
     "123 1st street, Apt 345" --> "123 1st st"
 * Apostrophes are removed and leave no whitespace in between characters
 * Ranges (as in "517-520 1st Street") are eliminated. Only the first
 number in the range must is kept
 * No fractions in addresses (as in 10/2 Market Street)
 * Streets and avenues from 1-9 must have a "0" added to the left (as in
 7th street --> 07th street
 * Cardinal directions are kept to the right of the address type in 13
 cases.


 2. Processes:

 * Book to be transformed is loaded as object "wb"
 * Output book is created as object "wb2"
 * Active sheet is stored to object "ws"
 * First column is copied and pasted into the second column of "ws"
 * Abbreviates addressees and wipes out characters to the right of
     address type
 * Makes sure that cardinal directions are kept (as in 123 1st NE)
 * Remove apostrophes, periods, octothorpe and commas
 * Removes ranges
 * Removes letters mixed with numbers
 * Removes fractions in addresses
 * Adds a number to single digit addresses (as in 7th ave * 07th Ave)
 * Transforms BAYSHORE BLVD * BAY SHORE BLVD
 * Handles Embarcadero Center Transformations as:
      - 1 embarcadero center * 301 CLAY ST
      - 2 embarcadero center –-> 201 CLAY ST
      - 3 embarcadero center –-> 101 CLAY ST
      - 4 embarcadero center –-> 150 DRUMM ST
 * Handles addresses commonly entered without address type
 * Writes new header for column with value addresses
 * Saves workbook changes

## Getting Started

This is a standalone script. Simply download the latest version of the script (imperfect_addresses.py) from the production folder.

The input file must be in the same folder as the script, and the output will be generated in the same folder were the script is running.

## Dependencies

1. openpyxl

External library used to manipulate spreadsheet

2. numerate_xl.py

Stores dictionary that reads excel columns as numbers and function that looks for target column

## Constraints and Potential Issues

* Target column must be named "Address" or "Location"
* Target column name above must be unique
* Excel file must be named "test.xlsx"
* .xls files are not accepted
* Spreadsheet must be in the same folder where script is running
* Output spreadsheet is overwritten every time script is ran

### Installing

No instalation required.

## Authors

* **Jonathan Engelbert** - *Sole Developer* - [jonathanengelbert](https://github.com/jonathanengelbert/)

This project has no participating contributors at the moment.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* To all the amazing resources available online
* Mike Wynne
* Python Documentation (https://docs.python.org/3/)
