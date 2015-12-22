import triangle
file = open("proj09-input.txt")

for line in file:
    line = line.strip()
    t = triangle.Triangle(line)
    print(t)
    if t.is_valid() == True:
        print(t)
        print(t.perimeter())
        print(t.area())
    else:
        print("Is not a Triangle")
