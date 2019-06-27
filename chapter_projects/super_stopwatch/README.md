# Super Stopwatch

Say you want to track how much time you spend on boring tasks you haven’t automated yet. You don’t have a physical stopwatch, and it’s surprisingly difficult to find a free stopwatch app for your laptop or smartphone that isn’t covered in ads and doesn’t send a copy of your browser history to marketers.

At a high level, here’s what your program will do:
- Track the amount of time elapsed between presses of the ENTER key, with each key press starting a new “lap” on the timer
- Print the lap number, total time, and lap time

## Sample Output
<p align=center>
  <img src=./sample_output.png alt=sample console output>
</p>

Ideas for Similar Programs
-

Time tracking opens up several possibilities for your programs. Although you can download apps to do some of these things, the benefit of writing programs yourself is that they will be free and not bloated with ads and useless features. You could write similar programs to do the following:

- Create a simple timesheet app that records when you type a person’s name and uses the current time to clock them in or out
- Add a feature to your program to display the elapsed time since a process started, such as a download that uses the `requests` module
- Intermittently check how long a program has been running and offer the user a chance to cancel tasks that are taking too long
