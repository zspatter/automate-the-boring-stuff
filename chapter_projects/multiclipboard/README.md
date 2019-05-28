# Multiclipboard
This scipt stores the clipboard history enabling users to re-copy entries preivously copied to the clipboard. This is a quality of life improvement over the standard implementation of the clipboard as it allows users to reference multiple entries quickly and easily.

The program will save each piece of clipboard text under a keyword. For example, when you run py mcb.pyw save spam, the current contents of the clipboard will be saved with the keyword spam. This text can later be loaded to the clipboard again by running py mcb.pyw spam. And if the user forgets what keywords they have, they can run py mcb.pyw list to copy a list of all keywords to the clipboard.

Here's what the program does:
* The command line argument for the keyword is checked
* If the argument is `save`, then the clipboard contents are saved to the keyword
* If the argument is `list`, then all the keywords are copied to the clipboard
* Otherwise, the text for the keyword is copied to the clipboard
