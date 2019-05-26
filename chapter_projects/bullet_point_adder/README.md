# Adding Bullets to Markup

The bullet_point_adder.py script will get the text from the clipboard, add a star and space to the beginning of each line, and then paste this new text to the clipboard. For example, if I copied the following text (for the Wikipedia article “List of Lists of Lists”) to the clipboard:

```
Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars
```
and then ran the bullet_point_adder.py program, the clipboard would then contain the following:
```
* Lists of animals
* Lists of aquarium life
* Lists of biologists by author abbreviation
* Lists of cultivars
```
This star-prefixed text is ready to be pasted into a Wikipedia article (or Markdown .md) as a bulleted list.

This script demonstrates how to use python to manipulate text and how to leverage the clipboard. This script can be altered to remove trailing spaces from the end of lines, convert to upper/lower case, or any other text manipulation. Whatever your needs, you can use the clipboard for input and output.