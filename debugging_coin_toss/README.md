# Debugging Coin Toss

The following program is meant to be a simple coin toss guessing game. The player gets two guesses (it’s an easy game). However, the program has several bugs in it. Run through the program a few times to find the bugs that keep the program from working correctly.
```python
import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    if toss == guess:
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
```

This is just a simple debugging exercise. I chose to add some logging to the script which indicates where control currently is as well as variable values.

## Sample Output
<p align=center>
  <img src=./sample_output.png alt=sample console output>
</p>
