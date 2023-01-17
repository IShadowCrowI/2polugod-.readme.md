for i in range(1,100):
    chislo=''
    num=(bin(i)[2:])
    if num.count('1' and '0')%2==0:
        chislo=num[:-2]+'110'

    if num.count('1' and '0')%2!=0:
        chislo=num[:-2]+'001'
    if int(chislo,2)>160:
        print (i, int(chislo,2))
        break
