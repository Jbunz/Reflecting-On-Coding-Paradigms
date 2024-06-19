from functools import reduce

# Function to flatten an array
def flatten(arr):
    flat_list = []
    for item in arr:
        if isinstance(item, list):
            flat_list.extend(flatten(item))  
        else:
            flat_list.append(item)
    return flat_list

# Function to sort an array
def sort(arr):
    return sorted(arr)

# Main function to flatten and sort an array
def flatten_and_sort(arr):
    return sort(flatten(arr))

# Testing the function
array = [3, [2, 1], [4, [6, 5]]]
print(flatten_and_sort(array))  

# Thought Questions

# 1. How does this solution ensure data immutability?
#    - This solution ensures data immutability by not modifying the original array. It creates new arrays instead of altering the input array.

# 2. Is this solution a pure function? Why or why not?
#    - Yes, this solution is a pure function because it always produces the same output given the same input and does not have any side effects.

# 3. Is this solution a higher-order function? Why or why not?
#    - No, this solution does not use higher-order functions explicitly.

# 4. Would it have been easier to solve this problem using a different programming style?
#    - It depends on familiarity. Some may find it easier to use imperative style for this problem.

# 5. Why is functional programming helpful for this problem?
#    - Functional programming emphasizes immutability and pure functions, making code more predictable and easier to debug.


# Podracer class definition
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"

# AnakinsPod class definition
class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed *= 2

# SebulbasPod class definition
class SebulbasPod(Podracer):
    def flame_jet(self, other_podracer):
        other_podracer.condition = "trashed"

# Testing the classes
# Creating a Podracer instance
pod = Podracer(500, "trashed", 30000)
pod.repair()
print(pod.condition)  

# Creating an AnakinsPod instance with a max_speed of 2
anakins_pod = AnakinsPod(2, "perfect", 50000)
anakins_pod.boost()
print(anakins_pod.max_speed)  

# Creating a SebulbasPod instance
sebulbas_pod = SebulbasPod(700, "perfect", 60000)
sebulbas_pod.flame_jet(pod)
print(pod.condition)  

# Thought Questions

# 1. How does this solution demonstrate the four pillars of OOP?
#    - Encapsulation: Attributes are encapsulated within classes.
#    - Abstraction: Internal workings of methods are hidden from the user.
#    - Inheritance: AnakinsPod and SebulbasPod inherit from Podracer.
#    - Polymorphism: Methods can interact with different types of Podracer instances.

# 2. Would it have been easier to implement a solution to this problem using a different coding style?
#    - OOP is suited for modeling real-world entities like podracers.

# 3. How did Object Oriented Programming assist in solving this problem?
#    - OOP allows for clear, reusable, and organized code that models real-world objects and interactions.
