def UglyNumber(num):
    uglyNum = []
    uglyNum.append(1)

    numtwo = 2
    numtwoC = 1

    numthree = 3
    numthreeC = 1

    numfive = 5
    numfiveC = 1

    while(len(uglyNum) < num):
        genTwo = numtwo*numtwoC
        genThree = numthree*numthreeC
        genFive = numfive*numfiveC

        if((genTwo <= genThree) and (genTwo <= genFive)):
            numtwoC +=1
            if(genTwo not in uglyNum):
                uglyNum.append(genTwo)

        if((genThree <= genTwo) and (genThree <= genFive)):
            numthreeC +=1
            if(genThree not in uglyNum):
                uglyNum.append(genThree)

        if((genFive <= genThree) and (genFive <= genTwo)):
            numfiveC +=1
            if(genFive not in uglyNum):
                uglyNum.append(genFive)


    print(uglyNum)


num = 10
UglyNumber(num)
