import modules

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = modules.area(length, width)
peri = modules.perimeter(length, width)

print(f"Area of rectangle: {area} cm2")
print(f"Perimeter of rectangle is {peri}")
