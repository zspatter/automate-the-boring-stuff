# Date Converter

Here’s what the program does:

* It searches all the filenames in the current working directory for American-style dates (MM-DD-YYYY)
* When one is found, it renames the file to make it ISO 8601 format (YYYY-MM-DD)

This means the code will need to do the following:
* Create a regex that can identify the text pattern of American-style dates
* Call `os.listdir()` to find all the files in the working directory
* Loop over each filename, using the regex to check whether it has a date
* If it has a date, rename the file with `shutil.move()`

## Sample Output
<p align=center>
  <img src=./sample_output.png alt=sample console output>
</p>
