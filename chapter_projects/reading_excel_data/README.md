# Reading Data from a Spreadsheet

Say you have a spreadsheet of data from the 2010 US Census and you have the boring task of going through its thousands of rows to count both the total population and the number of census tracts for each county. (A census tract is simply a geographic area defined for the purposes of the census.) Each row represents a single census tract.

Even though Excel can calculate the sum of multiple selected cells, you’d still have to select the cells for each of the 3,000-plus counties. Even if it takes just a few seconds to calculate a county’s population by hand, this would take hours to do for the whole spreadsheet.

In this project, you’ll write a script that can read from the census spreadsheet file and calculate statistics for each county in a matter of seconds.

This script does the following:
* Reads the data from the Excel spreadsheet
* Counts the number of census tracts in each county
* Counts the total population of each county
* Writes the resulting data structure to a new .py file

The readCensusExcel.py program was throwaway code: Once you have its results saved to census2010.py, you won’t need to run the program again. Whenever you need the county data, you can just run import census2010.

Calculating this data by hand would have taken hours; this program did it in a few seconds. Using OpenPyXL, you will have no trouble extracting information that is saved to an Excel spreadsheet and performing calculations on it. 

The above data structure allows us to import the data into another script to work with and manipulate the the data.

## Sample Output
<p align=center>
  <img src=./sample_output.png alt=sample console output width=600>
</p>

## Ideas for Similar Programs
Many businesses and offices use Excel to store various types of data, and it’s not uncommon for spreadsheets to become large and unwieldy. Any program that parses an Excel spreadsheet has a similar structure: It loads the spreadsheet file, preps some variables or data structures, and then loops through each of the rows in the spreadsheet. Such a program could do the following:
- Compare data across multiple rows in a spreadsheet
- Open multiple Excel files and compare data between spreadsheets
- Check whether a spreadsheet has blank rows or invalid data in any cells and alert the user if it does
- Read data from a spreadsheet and use it as the input for your Python programs
