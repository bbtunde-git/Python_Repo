R = int(input("Please Enter Your Score: "))
if (R >= 85) and (R <= 100):
    print("A Grade")
elif (R < 85) and (R >= 80):
    print("A- Grade")
elif (R < 80) and (R >= 70):
    print("B Grade")
elif (R < 70) and (R >= 65):
    print("B- Grade")
elif (R < 65) and (R >= 50):
    print("C Grade")
elif (R < 50) and (R >= 0):
    print("Below Average")
else:
    print("Out Of Range")
