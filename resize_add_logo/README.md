# Adding a Logo

Say you have the boring job of resizing thousands of images and adding a small logo watermark to the corner of each. Doing this with a basic graphics program such as Paintbrush or Paint would take forever. A fancier graphics application such as Photoshop can do batch processing, but that software costs hundreds of dollars. Let’s write a script to do it instead.

At a high level, here’s what the program should do:
- Load the logo image
- Loop over all .png and.jpg files in the working directory
- Check whether the image is wider or taller than 500 pixels
- If so, reduce the width or height (whichever is larger) to 500 pixels and scale down the other dimension proportionally
- Paste the logo image into the corner
- Save the altered images to another folder

## Sample Output

Before
-
<p align=center>
  <img src=./images/zophie.png alt=original image height=500>
</p>

After
-
<p align=center>
  <img src=./images/zophie_with_logo.png alt=image with logo height=500>
</p>

## Ideas For Similar Programs
Being able to composite images or modify image sizes in a batch can be useful in many applications. You could write similar programs to do the following:

- Add text or a website URL to images
- Add timestamps to images
- Copy or move images into different folders based on their sizes
- Add a mostly transparent watermark to an image to prevent others from copying it

