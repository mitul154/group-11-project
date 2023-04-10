# Initializing variables
paint_coverage = 350    # Paint coverage in square feet per gallon (ft2/gal)
paint_cost = 42     # Cost of each gallon of paint ($CDN/gal)
labour_cost = 0  # Cost of labour per hour ($CDN/hr) Value is 0 because it is calculated in the cost of paint
areas = []  # List to store the areas of the windows and doors
two_wall = 2  # Number of walls that are rectangular
four_walls = 4  # Number of walls that are square
factor_of_square = 2  # Factor of square
areas_ = []
gallons = []
price = []


def compute_room_area(current_room):  # Function to compute the area of the room
    area_of_rectangular_walls = 0 # Initializing variables
    area_of_square_walls = 0 # Initializing variables
    area_of_custom_walls = 0 # Initializing variables
    shape = int(input("Select the shape of the wall of the room from the following:\n"  # User input to select the shape of the room
                      "Type '1' for Rectangular\n" 
                      "Type '2' for Square\n"
                      "Type '3' for Custom (more or less than 4 walls, all square or rectangles)\n"))
    if shape == 1:  # If the shape is rectangular
        area_of_rectangular_walls = compute_rectangle_walls_area()  # Call the function to compute the area of the rectangular walls
    elif shape == 2:  # If the shape is square
        area_of_square_walls = compute_square_walls_area()  # Call the function to compute the area of the square walls
    elif shape == 3:  # If the shape is custom
        compute_custom_walls_area()  # Call the function to compute the area of the custom walls
        area_of_custom_walls = sum(areas)  # Sum the areas of the custom walls
    compute_windows_doors_area()  # Call the function to compute the area of the windows and doors
    area_of_doors_windows = sum(areas)  # Sum the areas of the windows and doors
    total_area = area_of_rectangular_walls + area_of_square_walls + area_of_custom_walls - area_of_doors_windows  # Compute the total area of the room
    total_gallons = compute_gallons(total_area)  # Compute the total gallons of paint required
    total_cost = compute_paint_price(total_gallons)  # Compute the total cost of the paint
    areas_.append(total_area)
    gallons.append(total_gallons)
    price.append(total_cost)
    print(f"For Room: {current_room}, the area to be painted is {total_area:.1f} square ft and will require {total_gallons:.2f} "  # Print the total area of the room, the total gallons of paint required and the total cost of the paint
          f"gallons to paint. This will cost the customer ${total_cost:.2f}")  # Print the total cost of the paint rounded to 2 decimal places


def compute_rectangle_walls_area():  # Function to compute the area of the rectangular walls
    length = int(input("Enter the length of the room in feet: "))  # User input to enter the length of the room
    width = int(input("Enter the width of the room in feet: "))  # User input to enter the width of the room
    height = int(input("Enter the height of the room in feet: "))  # User input to enter the height of the room
    area_of_wall = calculate_rectangle_area(length, height) * two_wall  # Compute the area of the two rectangular walls
    area_of_wall += calculate_rectangle_area(width, height) * two_wall  # Compute the area of the two rectangular walls
    return area_of_wall # Return the area of the rectangular walls


def calculate_rectangle_area(length, width):  # Function to compute the area of a rectangle
    return length * width # Return the area of the rectangle


def compute_square_walls_area():  # Function to compute the area of the square walls
    length = int(input("Enter the length of the room in feet: "))  # User input to enter the length of the room
    return compute_square_area(length) * four_walls  # Return the area of the square walls


def compute_square_area(length):  # Function to compute the area of a square
    return length ** factor_of_square  # Return the area of the square


def compute_windows_doors_area(): # Function to compute the area of the windows and doors
    areas.clear()  # Clear the list of areas
    number_of_windows_doors_area = int(input("How many windows and doors does the room contain?: "))  # User input to enter the number of windows and doors
    for i in range(number_of_windows_doors_area): # For loop to compute the area of each window and door
        length = int(input(f"Enter window/door length for window/door {i+1} in feet: "))  # User input to enter the length of the window or door
        width = int(input(f"Enter window/door width for window/door {i+1} in feet: "))  # User input to enter the width of the window or door
        area = length * width  # Compute the area of the window or door
        areas.append(area)  # Append the area of the window or door to the list of areas


def compute_custom_walls_area():  # Function to compute the area of the custom walls
    areas.clear()
    number_of_walls = int(input("How many walls are there in the room: "))  # User input to enter the number of walls
    for i in range(number_of_walls):  # For loop to compute the area of each wall
        height = int(input(f"Enter the height of wall {i+1} in feet: "))  # User input to enter the height of the wall
        length = int(input(f"Enter the length of wall {i+1} in feet: "))  # User input to enter the length of the wall
        area_of_wall = height * length  # Compute the area of the wall
        areas.append(area_of_wall)  # Append the area of the wall to the list of areas


def compute_gallons(area):  # Function to compute the total gallons of paint required
    AREAPERGALLON = 350  # Constant to store the area per gallon
    total_gallons = area / AREAPERGALLON  # Compute the total gallons of paint required
    return total_gallons  # Return the total gallons of paint required


def compute_paint_price(gallons):  # Function to compute the total cost of the paint
    PRICEPERGALLON = 42  # Constant to store the price per gallon
    total_paint_price = gallons * PRICEPERGALLON  # Compute the total cost of the paint
    return total_paint_price  # Return the total cost of the paint


print("Welcome to Shiny Paint Company for indoor painting!")  # Welcome message
number_of_rooms = int(input("How many Rooms do you want to paint:\n"))  # User input to enter the number of rooms
print("Thank you!")  # Thank you message
for i in range(number_of_rooms):  # For loop to compute the area of each room
    print(f"Room: {i+1}")  # Print the room number
    compute_room_area(i+1)  # Call the function to compute the area of the room

print(f"\nArea to be painted is {sum(areas_):.2f} square ft and will"
      f" require {sum(gallons):.2f} gallons to paint. This will cost the customer ${sum(price):.2f}")
