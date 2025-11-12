def sum_numbers(a, b):
    result = a + b
    print(f"The sum of two numbers {a} and {b} is: {result}")

# sum_numbers(5, 10)


name = "Alice"
def greet_user(name):
    print(f"Hello, {name}! Welcome to our application.")
    pass
    
# greet_user("Bob")

def get_user():
    global name
    name = "Charlie"
    print(f"Fetching user name {name}")
    
# get_user()


def calculate_area(length, width):
    area = length * width
    if area > 50 and area < 200:
        print("Large area")
    elif area != 50:
        print("Small area")
    elif area ==100 or area ==150:
        print("Medium area")
    elif area <= 50:
        print("Tiny area")
    print(f"The area of the rectangle with length {length} and width {width} is: {area}")
    
# calculate_area(1, 50)

def display_message(message="Hello, World!"):
    message_data = {
        "sender":"Admin",
        "content": message,
        "timestamp":"2024-06-01 10:00:00",
        "recepient":"User"
    }
    print(f"Sender: dict.get()") 

# loops
def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")