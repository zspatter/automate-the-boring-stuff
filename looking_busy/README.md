# Looking Busy

Many instant messaging programs determine whether you are idle, or away from your computer, by detecting a lack of mouse movement over some period of time—say, ten minutes. Maybe you’d like to sneak away from your desk for a while but don’t want others to see your instant messenger status go into idle mode. Write a script to nudge your mouse cursor slightly every ten seconds. The nudge should be small enough so that it won’t get in the way if you do happen to need to use your computer while the script is running.

This program nudges the mouse slightly then immediately returns the mouse to it's original position. The relative X and Y values as well as the duration of each move are chosen randomly to reduce the predictability of the program. Additionally, the interval between nudges is chosen randomly between half of the specified interval and the specified interval in seconds. 

Furthermore, this program randomly chooses a function key bound to no action (F15-F24) to simulate keyboard input after each mouse nudge.
