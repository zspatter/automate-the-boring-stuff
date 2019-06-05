# Reading Data from a Spreadsheet

Say you have a spreadsheet of data from the 2010 US Census and you have the boring task of going through its thousands of rows to count both the total population and the number of census tracts for each county. (A census tract is simply a geographic area defined for the purposes of the census.) Each row represents a single census tract.

Even though Excel can calculate the sum of multiple selected cells, you’d still have to select the cells for each of the 3,000-plus counties. Even if it takes just a few seconds to calculate a county’s population by hand, this would take hours to do for the whole spreadsheet.

In this project, you’ll write a script that can read from the census spreadsheet file and calculate statistics for each county in a matter of seconds.

This script does the following:
* Reads the data from the Excel spreadsheet
* Counts the number of census tracts in each county
* Counts the total population of each county
* Prints the results

## Sample Output
<p align=center>
  <img src=./sample_output.png alt=sample console output width=600>
</p>
