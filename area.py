class poly:
    def __init__(self,a,b,c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

class Triangle(poly):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def getarea(self):
        s = (a+b+c) / 2

        return float((s*(s-a)*(s-b)*(s-c)) ** 0.5)

a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
# t = Triangle(a,b,c)

print(f"Area of the triangle is ", Triangle(a,b,c).getarea())