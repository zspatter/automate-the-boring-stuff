# throwaway script used to generate sample files
import random

for x in range(1, 6):
    with open(f'sample_text{x}.txt', 'w') as text:
        for y in range(1, random.randint(3, 15)):
            text.write(f'Line {y}: sample line in sample_text{x}.txt\n')
