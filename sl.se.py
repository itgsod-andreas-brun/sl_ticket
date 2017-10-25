def fares(age, student=False, senior=False, adult=False, discount=False):
    if age > 20 and age < 65:
        if adult==True:
            return "Fullprice 30kr"
        else:
            return "discount price 20kr"
    elif age <= 20 or age >=65:
        if student==True:
            return "discount price 20kr"
        elif senior==True:
            return "discount price 20kr"

        print "Djurgården"






print fares(10)
print fares(65,senior=True)
print fares(25,student=True)
print fares(64,adult=True)
