# To generate random numbers you should import the random library like this.
import random

'''
Here, we create a variable named d20 (for 20-sided-die)
and we generate a random number between 1 and 20 with the randint() function from the random library
'''
d20 = random.randint(1, 20)

# Here we print out the random number's value.
print(d20)

for x in range(100):
    print(random.randint(1, 50))