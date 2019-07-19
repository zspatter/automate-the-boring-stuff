# “Just Text Me” Module

Texting is a great way to send yourself notifications when you’re away from your computer. If you’ve automated a boring task with a program that takes a couple of hours to run, you could have it notify you with a text when it’s finished. Or you may have a regularly scheduled program running that sometimes needs to contact you, such as a weather-checking program that texts you a reminder to pack an umbrella.

This implementation relies on environment variables to store the API key, auth token, and send/receive phone numbers.

This simple function can be used by other programs by placing this file in the same directory as the Python executable. To use this function, simple add the following:

```python
from notifications import text_myself

text_myself(message='Sample message: task complete.')
```
