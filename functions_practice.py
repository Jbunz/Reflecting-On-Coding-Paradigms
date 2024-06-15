# functions_practice.py

# Function to print a greeting
def hello():
    print("Hello, user!")

# Function to pack three items into a list
def pack(item1, item2, item3):
    return [item1, item2, item3]

# Function to simulate eating lunch
def eat_lunch(lunch_items):
    if not lunch_items:
        print("My lunchbox is empty!")
    else:
        for i in range(len(lunch_items)):
            if i == 0:
                print(f"First I eat {lunch_items[i]}")
            else:
                print(f"Next I eat {lunch_items[i]}")

# Test the hello function
hello()

# Test the pack function
packed_list = pack('sandwich', 'chips', 'water')
print("Packed list:", packed_list)

# Test the eat_lunch function with a non-empty list
eat_lunch(['sandwich', 'chips', 'water'])

# Test the eat_lunch function with an empty list
eat_lunch([])
