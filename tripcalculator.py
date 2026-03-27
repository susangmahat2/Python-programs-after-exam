def hotelcost(nights):
    return 140*nights

def planeridecost(city):
    if "Charlotte" == city:
        return 183
    elif "Tampa" == city:
        return 220
    elif "Pittsburgh" == city:
        return 222
    elif "Los Angeles" == city:
        return 475
    
def rentalcarcost(days):
    if days >= 7:
        return 40*days-50
    elif days >= 3:
        return 40*days-20
    else:
        return 40*days
def tripcost(city,days,nights):
    return planeridecost(city)+hotelcost(nights)+rentalcarcost(days)
print ("Cost of car rental:",rentalcarcost(5))
print("cost of plane ride:",planeridecost("Tampa"))
print("Cost of hotel:",hotelcost(5))
print("Total trip cost:",tripcost("Tampa",5,5))
print("Total trip cost:",tripcost("Los Angeles",5,5))
    

