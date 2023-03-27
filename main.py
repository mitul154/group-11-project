# Initializing variables

area = 0
length = 0
width = 0
height = 0

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
    area = length * height * 2
    area2 = width * height * 2
    totalRoomArea = area + area2
    return totalRoomArea

    pass


def calculateRectangleArea():
    pass


def computeSquareWallsArea():
    pass


def computeSquareArea():
    pass


def computeWindowsDoorsArea():
    pass


def computeCustomWallsArea():
    pass


def computeGallons():
    pass


def computePaintPrice():
    pass