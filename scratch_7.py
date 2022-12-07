a=int (input ("enter the value of currency"))
b=input("choose the currency type")
c=input ("choose the currency type you would like yo change into")
if b == "rupee"and c=="dollar":
        print(a*82)
elif b == "rupee" and c == "euro" :
    print (a*83.65)
elif b== "rupee" and c=="CAD":
    print(a*60.76)
elif b=="rupee" and c=="cent":
    print(a*2.39)
elif b=="rupee" and c=="dhiram":
    print(a*22.25)
elif b=="rupee" and c=="pound":
    print(a*96.4)
elif b=="rupee" and c=="singapore dollar":
    print(a*59.12)
elif b=="rupee" and c=="taka":
    print(a*0.79)