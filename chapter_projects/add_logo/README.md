# Adding a Logo

Say you have the boring job of resizing thousands of images and adding a small logo watermark to the corner of each. Doing this with a basic graphics program such as Paintbrush or Paint would take forever. A fancier graphics application such as Photoshop can do batch processing, but that software costs hundreds of dollars. Let’s write a script to do it instead.

At a high level, here’s what the program should do:
- Load the logo image
- Loop over all .png and.jpg files in the working directory
- Check whether the image is wider or taller than 300 pixels
- If so, reduce the width or height (whichever is larger) to 300 pixels and scale down the other dimension proportionally
- Paste the logo image into the corner
- Save the altered images to another folder
