# Scheduled Web Comic Downloader

Write a program that checks the websites of several web comics and automatically downloads the images if the comic was updated since the program’s last visit. Your operating system’s scheduler (Scheduled Tasks on Windows, launched on OS X, and cron on Linux) can run your Python program once a week. The Python program itself can download the comic and then copy it to a specified directory so that it is easy to find. This will free you from having to check the website yourself to see whether it has updated.

The script searches for new releases of the [Buttersafe webcomic](https://www.buttersafe.com/). This script can be easily expanded to include other webcomics as well.

### Sample First Request
<p align=center>
  <img src=./images/sampl_first_request.png alt=sample first request>
</p>

### Sample With Multiple New Comics
<p align=center>
  <img src=./images/sample_multiple_comics.png alt=sample with multiple new comics>
</p>

### Sample With No Updates
<p align=center>
  <img src=./images/sample_no_updates.png alt=sample with no updates>
</p>
