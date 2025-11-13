# def sum_numbers(a, b):
#     result = a + b
#     print(f"The sum of two numbers {a} and {b} is: {result}")

# # sum_numbers(5, 10)


# name = "Alice"
# def greet_user(name):
#     print(f"Hello, {name}! Welcome to our application.")
#     pass
    
# # greet_user("Bob")

# def get_user():
#     global name
#     name = "Charlie"
#     print(f"Fetching user name {name}")
    
# # get_user()


# def calculate_area(length, width):
#     area = length * width
#     if area > 50 and area < 200:
#         print("Large area")
#     elif area != 50:
#         print("Small area")
#     elif area ==100 or area ==150:
#         print("Medium area")
#     elif area <= 50:
#         print("Tiny area")
#     print(f"The area of the rectangle with length {length} and width {width} is: {area}")
    
# # calculate_area(1, 50)

# def display_message(message="Hello, World!"):
#     message_data = {
#         "sender":"Admin",
#         "content": message,
#         "timestamp":"2024-06-01 10:00:00",
#         "recepient":"User"
#     }
#     print(f"Sender: dict.get()") 

# # loops
# def print_numbers():
#     for i in range(1, 6):
#         print(f"Number: {i}")
        
# # print_numbers()

# # lists comprehension
# def square_numbers(numbers):
#     squared = [x**2 for x in numbers]
#     print(f"Squared numbers: {squared}")

# square_numbers([1, 2, 3, 4, 5])

# #generator expression
# def generate_squares(n):
#     squares = (x**2 for x in range(1, n+1))
#     for square in squares:
#         print(f"Square: {square}")
        
# generate_squares(5)




# def print_fibonacci(length):
#     if length <= 0:
#         return []
#     elif length == 1:
#         return [1]
#     else:
#         fib_list = [0, 1] 
#         while len(fib_list) < length:
#             next_in_list = fib_list[-1] + fib_list[-2]
#             fib_list.append(next_in_list)       
#         return fib_list

# print_fibonacci(9)    


dict_ex = {
    "Mapping": "An object type whose arbitraty values are stored in \
        random and accessed using immutable keys",
    0.5 : 'transparency in css' 
}

# print(dict_ex.get(0.6, "please pass in a valid search key"))

dict_ex["new"] = "I'm new here"
# print(dict_ex)
dict_ex["new"] = "New? Not anymore"
# print(dict_ex)
new_dict = {
    'cool' : "Oh yes i am",
    "rude" : "Regardless",
    "Mapping": "Already learnt"
}
dict_ex.update(new_dict)

# print(dict_ex)

# print([key for key in dict_ex])
# print([dict_ex[value] for value in dict_ex])
# print([item for item in dict_ex.items()]) #individual values
# print([key for key, value  in dict_ex.items()])
# print([value for key, value in dict_ex.items()])

# print(set([1,2,3]))
# print(set("this set is very ugly") & set("ugly"))
# print(set("this set is very ugly") - set("ugly"))

set_1 = {1,2,3}
set_2 = {3,4,5}

# print(set_1 -= set_2)
# print(set_1)
# print(set_2)