x = int(input("enter first number: "))
y = int(input("enter second number: "))
z = int(input("enter third number: "))
if x+y>z and x+z>y and y+z>x:
    print(f"yes , it is possible to make a triangle using {x},{y},{z} as the sides of a traingle.")
else:
    print(f"no , traingle cannot be formed using {x},{y},{z} as the sides")


