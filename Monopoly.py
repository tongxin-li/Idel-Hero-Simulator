import numpy as np
import random

""""
Version: Monopoly-01

Description:
A simple monopoly simulator for the Easter event of Idel Hero

"""

class Maze:

    def __init__(self, num_dice=78):
        # Basic parameters
        self.num_dice = num_dice
        self.num_lucky_dice = 0
        self.pos = 0
        self.card = []
        self.star = 0
        self.level = [0,0,0]
        self.done = False

    def use_ordinary_dice(self):
        # toss a dice
        result = random.randint(1, 7)
        self.num_dice -= 1
        self.forward(result)

    def use_lucky_dice(self, selection):
        self.num_lucky_dice -= 1
        self.forward(selection)

    def forward(self, step):

        pos_temp = self.pos

        # move forward
        # karma hut
        if self.pos == 15 and self.num_dice % 2 is not 0:
            self.pos -= step
        # this won't make pos negative
        else:
            self.pos += step

        # check if the imp completes a full cycle
        if self.pos > 20:
            self.pos = self.pos - 20

        # check starry mushroom
        # upgrade

        if self.pos == 4:
            self.level[0] = min(2, self.level[0]+1)

        if self.pos == 11:
            self.level[1] = min(2, self.level[0] + 1)

        if self.pos == 18:
            self.level[2] = min(2, self.level[0] + 1)

        # increase stars

        if self.pos >= 4 > pos_temp:
            self.star += self.level[0] + 3

        if self.pos >= 11 > pos_temp:
            self.star += self.level[1] + 3

        if self.pos >= 18 > pos_temp:
            self.star += self.level[2] + 3

        # check huts

        # wishing hut
        if self.pos == 5:
            self.num_dice += 1

        # fortune hut
        # to be completed

        # lucky hut

        if self.pos == 20:
            self.num_lucky_dice += 1

        # Check state
        if self.num_dice == 0 and self.num_lucky_dice == 0:
            self.done = True

# Let's test it
num_Monte_Carlo = 100000
star_list_A = []
star_list_B = []

for i in range(num_Monte_Carlo):
    if i % 100:
        print("Running ... completed " + str(i * 100) + "iterations")

    # Define policies:
    # Policy-A: use lucky dice when the imp is close to the lucky hut
    # Policy-B: use lucky dice when the imp is close to the wishing hut
    # Note that the two polices are just toy examples. Feel free to design your strategies

    # Implement Policy-A:

    maze = Maze(78)

    while maze.done is False:

        # targeting the lucky hut (if possible)
        if 19 >= maze.pos >= 17 and maze.num_lucky_dice > 0:
            maze.use_lucky_dice(20-maze.pos)
        elif maze.num_dice > 0:
        # use ordinary dice
            maze.use_ordinary_dice()

        # use up all dices
        if maze.num_dice is 0 and maze.num_lucky_dice > 0:
            maze.use_lucky_dice(6)

    star_list_A.append(maze.star)


    # Implement Policy-B:

    maze = Maze(78)

    while maze.done is False:

        # targeting the lucky hut (if possible)
        if 4 >= maze.pos >= 0 and maze.num_lucky_dice > 0:
            maze.use_lucky_dice(5-maze.pos)
        elif maze.num_dice > 0:
        # use ordinary dice
            maze.use_ordinary_dice()

        # use up all dices
        if maze.num_dice is 0 and maze.num_lucky_dice > 0:
            maze.use_lucky_dice(6)

    star_list_B.append(maze.star)


A = np.array(star_list_A)
B = np.array(star_list_B)
print(np.mean(A))
print(np.mean(B))

# Plot distributions

import matplotlib.pyplot as plt



plt.hist(A, color = 'blue', edgecolor = 'black')
plt.tight_layout()
plt.show()


plt.hist(B, color = 'blue', edgecolor = 'black')
plt.tight_layout()
plt.show()