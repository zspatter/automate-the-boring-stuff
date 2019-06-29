# Simple Countdown Program

Just like it’s hard to find a simple stopwatch application, it can be hard to find a simple countdown application. Let’s write a countdown program that plays an alarm at the end of the countdown.

At a high level, here’s what your program will do:
- Count down from 60
- Play a sound file (alarm.wav) when the countdown reaches zero

## Sample Output
<p align=center>
  <img src=./sample_output.gif alt=sample console output>
</p>

Ideas for Similar Programs
-
A countdown is a simple delay before continuing the program’s execution. This can also be used for other applications and features, such as the following:
- Use `time.sleep()` to give the user a chance to press CTRL-C to cancel an action, such as deleting files. Your program can print a “Press CTRL-C to cancel” message and then handle any KeyboardInterrupt exceptions with try and except statements
- For a long-term countdown, you can use timedelta objects to measure the number of days, hours, minutes, and seconds until some point (a birthday? an anniversary?) in the future
