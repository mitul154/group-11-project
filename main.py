# Initializing variables

area = 0
length = 0
width = 0


def computeRoomArea(room_number):
    shape = input("Select the shape of the wall of the room from the following:\n"
                  "Type '1' for Rectangular"
                  "Type '2' for Square"
                  "Type '3' for Custom")
    if shape == "Rectangular".casefold():
        area = length * width
    elif shape == "Square".casefold():
        area = length ** 2
    elif shape == "Custom".casefold():
        pass



def computeRectangleWallsArea():
    length = int(input("What is the length of the wall?"))
    width = int(input("What is the height of the wall?"))
    areaOfWall = length * width
    return areaOfWall


def calculateRectangleArea():
    for i in range(4):
        area += computeRectangleWallsArea - computeWindowsDoorsArea
    return area


def computeSquareWallsArea():
    pass


def computeSquareArea():
    pass


def computeWindowsDoorsArea():
    pass


def computeCustomWallsArea():
    pass


def computeGallons():
    AREAPERGALLON = 350
    totalGallons = area / AREAPERGALLON
    return totalGallons


def computePaintPrice():
    PRICEPERGALLON = 42
    totalPaintPrice = computeGallons() * 42
    print(totalPaintPrice)
