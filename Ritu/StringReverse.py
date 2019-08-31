def doreverese(str, nstr):
    if(len(str)>1):
        nstr = doreverese(str[1:len(str)], nstr)
    nstr = nstr + str[0]
    return nstr



str="abcd"
nstr=""

print(doreverese(str, nstr))
