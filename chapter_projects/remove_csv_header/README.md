# Removing the Header from CSV Files

Say you have the boring job of removing the first line from several hundred CSV files. Maybe you’ll be feeding them into an automated process that requires just the data and not the headers at the top of the columns. You could open each file in Excel, delete the first row, and resave the file—but that would take hours. Let’s write a program to do it instead.

The program will need to open every file with the .csv extension in the current working directory, read in the contents of the CSV file, and rewrite the contents without the first row to a file of the same name. This will replace the old contents of the CSV file with the new, headless contents.

At a high level, the program must do the following:
-
- Find all the CSV files in the current working directory
- Read in the full contents of each file
- Write out the contents, skipping the first line, to a new CSV file

Ideas for similar programs
-
- Compare data between different rows in a CSV file or between multiple CSV files
- Copy specific data from a CSV file to an Excel file, or vice versa
- Check for invalid data or formatting mistakes in CSV files and alert the user to these errors
- Read data from a CSV file as input for your Python programs

## Sample Output
<p align=center>
  <img src=./images/sample_output.png alt=sample console output>
</p>

### Before
<p align=center>
  <img src=./images/before.png alt=csv before script height=500>
</p>

### After
<p align=center>
  <img src=./images/after.png alt=csv after script height=500>
</p> 