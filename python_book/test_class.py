from random import randint


class Die:
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        print(randint(1, self.sides))


q = Die()
# for i in range(10):
#     q.roll_die()

w = Die()
w.sides = 10
w.roll_die()
