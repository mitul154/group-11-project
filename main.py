# Initializing variables
paint_coverage = 350    # Paint coverage in square feet per gallon (ft2/gal)
paint_cost = 42     # Cost of each gallon of paint ($CDN/gal)
labour_cost = 0

area = 0
length = 0
width = 0

def computeRoomArea(room_number):
    shape = input("Select the shape of the wall of the room from the following:\n"
                  "Type '1' for Rectangular"
                  "Type '2' for Square"
                  "Type '3' for Custom")
    if shape == 1:
        length = int(input("Enter the length of the room in feet: "))
        width = int(input("Enter the width of the room in feet: "))
        height = int(input("Enter the height of the room in feet: "))

        area = length * width
        print(area)
    elif shape == 2:
        length = int(input("Enter the length of the wall"))
        area = length ** 2
    elif shape == 3:
        number_of_dimensions = int(input("Enter the number of dimensions: "))



def computeRectangleWallsArea():
    pass


def calculate_rectangle_area():
    pass


def compute_square_walls_area():
    pass


def compute_square_area():
    pass


def compute_windows_doors_area():
    pass


def compute_custom_walls_area():
    pass


def compute_gallons():
    pass


def compute_paint_price():
    pass
