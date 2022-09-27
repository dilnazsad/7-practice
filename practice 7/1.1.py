def areacalculator():
    _input_ = input("enter the shape you want to calculate area of: ")
    area = 0
    p = 3.14
    if _input_ == "square":
        side = int(input("enter the value of side: "))
        area = area + (side ** 2)
    elif _input_ == "circle":
        r = int(input("enter the value of r: "))
        area = area + (2 * p * r)
    elif _input_ == "rectangle":
        length = int(input("enter the value of length: "))
        width = int(input("enter the value of length: "))
        area = area + (length * width)
    elif _input_ == "triangle":
        base = int(input("enter the value of base: "))
        height = int(input("enter the value of height: "))
        area = area +(0.5 * base * height)
    else:
        print("select a valid shape")
    print("%.2f" % area)

areacalculator()
