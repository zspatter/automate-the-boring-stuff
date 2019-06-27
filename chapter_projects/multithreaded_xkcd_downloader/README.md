# Multithreaded XKCD Downloader

[XKCD downloader](../xkcd_downloader/) was a single-threaded program: It downloaded one comic at a time. Much of the program’s running time was spent establishing the network connection to begin the download and writing the downloaded images to the hard drive. If you have a broadband Internet connection, your single-threaded program wasn’t fully utilizing the available bandwidth.

A multithreaded program that has some threads downloading comics while others are establishing connections and writing the comic image files to disk uses your Internet connection more efficiently and downloads the collection of comics more quickly.

## Sample Output
<p align=center>
  <img src=./sample_output.png alt=sample console output height=1000>
</p>
