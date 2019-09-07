class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y


def calculateArea(r1, l1, r2, l2):
    area1=(abs(l1.x-r1.x))*(abs(l1.y-r1.y))
    area2=(abs(l2.x-r2.x))*(abs(l2.y-r2.y))

    common=(max(r1.x,r2.x) - min(l1.x,l2.x)) * (max(r1.y,r2.y) - min(l1.y,l2.y))

    result=(area1+area2)-common

    return result

r1=Point(2,2)
l1=Point(5,7)

r2=Point(3,4)
l2=Point(6,9)

print(calculateArea(r1,l1,r2,l2))



