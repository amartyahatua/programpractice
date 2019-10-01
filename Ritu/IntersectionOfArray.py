class Intersection:
    def findUnion(self, array1, array2):
        result = []
        while(len(array1)>0 and len(array2)>0):
            temp1 = array1[0]
            temp2 = array2[0]

            if(temp1 == temp2):
                result.append(temp1)
                array1.pop(0)
                array2.pop(0)
            elif(temp1<temp2):
                result.append(temp1)
                array1.pop(0)
            else:
                result.append(temp2)
                array2.pop(0)

        if(len(array1)>0):
            result.extend(array1)
        if(len(array2)>0):
            result.extend(array2)

        return result

    def findIntersection(self, array1, array2):
        result = []
        for i in range(len(array1)):
            temp = array1[i]
            if(temp in array2):
                result.append(temp)

        return result



array1 = [1, 2, 3, 4, 5]
array2 = [1, 2, 7, 8, 9]

inter = Intersection()
print(inter.findUnion(array1, array2))

array1 = [1, 2, 3, 4, 5]
array2 = [1, 2, 7, 8, 9]
print(inter.findIntersection(array1, array2))