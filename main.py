# Initializing variables
paint_coverage = 350    # Paint coverage in square feet per gallon (ft2/gal)
paint_cost = 42     # Cost of each gallon of paint ($CDN/gal)
labour_cost = 0
area = 0
room_number = 1
areaOfWall = 0



def compute_room_area():
    
    shape = int(input("Select the shape of the wall of the room from the following:\n Type '1' for Rectangular \n Type '2' for Square \n Type '3' for Custom: \n \n " ))
    if shape == 1:
        length = int(input("Enter the length of the room in feet: "))
        width = int(input("Enter the width of the room in feet: "))
        height = int(input("Enter the height of the room in feet: "))

        area = length * width
        print(area)
    elif shape == 2:
        compute_square_area()
        compute_windows_doors_area()
    elif shape == 3:
        number_of_dimensions = int(input("Enter the number of dimensions: "))








def compute_rectangle_walls_area():
    length = int(input("What is the length of the wall?"))
    width = int(input("What is the height of the wall?"))
    areaOfWall = length * width
    return areaOfWall

    length = int(input("What is the length of the wall?"))
    width = int(input("What is the height of the wall?"))
    areaOfWall = length * width
    return areaOfWall

    pass


def calculate_rectangle_area():
    for i in range(4):
        area += compute_rectangle_walls_area() - compute_windows_doors_area()
    return area

    pass




def compute_square_walls_area():
    length = int(input("What is the length of the wall? "))
    areaOfWall = length ** 2
    return areaOfWall
    
    

def compute_square_area():
    areaOfWall = compute_square_walls_area()
    
    totalArea = areaOfWall * 4
    print(f"The area of the wall is {areaOfWall} square feet")
    print(f"The total area of the walls is {totalArea} square feet")
    return totalArea


def compute_windows_doors_area():
    number_of_windowsOrDoors = int(input("How many windows and doors does the room contain? "))
    
    for i in range(number_of_windowsOrDoors):
        windowOrDoor_length = int(input("What is the length of the door or window? "))
        windowOrDoor_width = int(input("What is the width of the door or window? "))
        compute_square_area(totalArea) -= windowOrDoor_length * windowOrDoor_width
    


def compute_custom_walls_area():
    pass


def compute_gallons():
    AREAPERGALLON = 350
    totalGallons = area / AREAPERGALLON
    return totalGallons

    pass


def compute_paint_price():
    PRICEPERGALLON = 42
    totalPaintPrice = compute_gallons() * 42
    print(totalPaintPrice)

    pass


compute_room_area()
