# Archive Directory

This script has a function that compresses a directory (including all subdirectories and thier contents). The desired directory's path is an argument to the function. This will makes an effort to exclude the unneccesary directories from the absolute path (path starts at the argument's path). The .zip is of the same name as the directory being compressed. This mirrors the behavior of native features of all major OS's to compress files/folders from the file viewer.

Ideas for similar programs:
* Walk a directory tree and archive just files with certain extensions, such as .txt or .py, and nothing else
* Walk a directory tree and archive every file except the .txt and .py ones
* Find the folder in a directory tree that has the greatest number of files or the folder that uses the most disk space
