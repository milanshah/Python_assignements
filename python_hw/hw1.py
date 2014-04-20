# Calculate the area of a circle or a square

def CalculateArea(geoType, len):
    """Calculate the area of a circle or a square. """

    if (geoType == "circle"):
        area = len * len * 3.14
        print(area)
        AreaLimit(area)
    elif (geoType == "suqare"):
        area = len * len
        print(area)
        AreaLimit(area)
    else:
        print("Unsupported Geo Type")


def AreaLimit(x):
    """If area is greater than 100 sq, print too big.
       If area is less than 10 sq, print too small."""

    if (x > 100):
        print ("too big")
    if (x < 10):
        print ("too small")
