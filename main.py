# Initializing variables
paint_coverage = 350  # Paint coverage in square feet per gallon (ft2/gal)
paint_cost = 42  # Cost of each gallon of paint ($CDN/gal)
labour_cost = 0  # Cost of labour is included in the paint cost
areas = []  # Empty list used for storing total area cost
two_wall = 2    # Next 3 variables are used to reduce hard coding
four_walls = 4
factor_of_square = 2


def compute_room_area(room_number, current_room):
    area_of_rectangular_walls = 0
    area_of_square_walls = 0
    area_of_custom_walls = 0
    shape = int(input("Select the shape of the wall of the room from the following:\n"
                      "Type '1' for Rectangular\n"
                      "Type '2' for Square\n"
                      "Type '3' for Custom (more or less than 4 walls, all square or rectangles)\n"))
    if shape == 1:
        area_of_rectangular_walls = compute_rectangle_walls_area()
    elif shape == 2:
        area_of_square_walls = compute_square_walls_area()
    elif shape == 3:
        compute_custom_walls_area()
        area_of_custom_walls = sum(areas)
    compute_windows_doors_area()
    area_of_doors_windows = sum(areas)
    total_area = area_of_rectangular_walls + area_of_square_walls + area_of_custom_walls - area_of_doors_windows
    total_gallons = compute_gallons(total_area)
    total_cost = compute_paint_price(total_gallons)
    print(f"For Room: {current_room}, the area to be painted is {total_area:.1f}: square ft and will require {total_gallons:.2f} "
        f"gallons to paint. This will cost the customer ${total_cost:.2f}")


def compute_rectangle_walls_area():
    length = int(input("Enter the length of the room in feet: "))
    width = int(input("Enter the width of the room in feet: "))
    height = int(input("Enter the height of the room in feet: "))
    area_of_wall = calculate_rectangle_area(length, height) * two_wall
    area_of_wall += calculate_rectangle_area(width, height) * two_wall
    return area_of_wall


def calculate_rectangle_area(length, width):
    return length * width


def compute_square_walls_area():
    length = int(input("Enter the length of the room in feet: "))
    return (length ** factor_of_square) * four_walls


def compute_square_area(length):
    return length ** factor_of_square


def compute_windows_doors_area():
    areas.clear()
    number_of_windows_doors_area = int(input("How many windows and doors does the room contain?: "))
    for i in range(number_of_windows_doors_area):
        length = int(input(f"Enter window/door length for window/door {i + 1} in feet: "))
        width = int(input(f"Enter window/door width for window/door {i + 1} in feet: "))
        area = length * width
        areas.append(area)


def compute_custom_walls_area():
    number_of_walls = int(input("How many walls are there in the room: "))
    for i in range(number_of_walls):
        height = int(input(f"Enter the height of wall {i + 1} in feet: "))
        length = int(input(f"Enter the length of wall {i + 1} in feet: "))
        area_of_wall = height * length
        areas.append(area_of_wall)


def compute_gallons(area):
    AREAPERGALLON = 350
    total_gallons = area / AREAPERGALLON
    return total_gallons


def compute_paint_price(gallons):
    PRICEPERGALLON = 42
    total_paint_price = gallons * PRICEPERGALLON
    return total_paint_price


print("Welcome to Shiny Paint Company for indoor painting!")
number_of_rooms = int(input("How many Rooms do you want to paint:\n"))
print("Thank you!")
for i in range(number_of_rooms):
    print(f"Room: {i + 1}")
    compute_room_area(number_of_rooms, i + 1)
