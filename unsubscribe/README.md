# Auto Unsubscriber

This program scans through your email account, finds all the unsubscribe links in all your emails, and automatically opens them in a browser. This program will have to log in to your email provider’s IMAP server and download all of your emails. It uses BeautifulSoup to check for any instance where the word *unsubscribe* occurs within an HTML link tag.

Once the script gathers a list of these URLs, it opens each link individually using `webbrowser.open()` to load the pages in a browser.

You’ll still have to manually go through and complete any additional steps to unsubscribe yourself from these lists. In most cases, this involves clicking a link to confirm.

But this script saves you from having to go through all of your emails looking for unsubscribe links. You can then pass this script along to your friends so they can run it on their email accounts.
