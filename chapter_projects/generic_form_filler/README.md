# Automatic Form Filler

Of all the boring tasks, filling out forms is the most dreaded of chores. It’s only fitting that now, in the final chapter project, you will slay it. Say you have a huge amount of data in a spreadsheet, and you have to tediously retype it into some other application’s form interface—with no intern to do it for you. Although some applications will have an Import feature that will allow you to upload a spreadsheet with the information, sometimes it seems that there is no other way than mindlessly clicking and typing for hours on end. You’ve come this far in this book; you know that of course there’s another way.

The form for this project is a Google Docs form that can be found [here](http://autbor.com/form).

At a high level, here’s what your program should do:
- Click the first text field of the form
- Move through the form, typing information into each field
- Click the Submit button
- Repeat the process with the next set of data

This implementation relies on images of the name field and submit another link to locate the coordinates of these items on the form. Consequently, these images are not compatible across different resolutions. Replacing these images using the desired resolution will allow the program to run on different environments.
