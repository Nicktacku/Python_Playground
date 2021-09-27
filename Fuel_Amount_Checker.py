Fuel_Amount = 0
Km = int(input("How many kilometer? "))

if Km > 0:
    Fuel_Amount =  Km * 100
    

    if Fuel_Amount < 1500:
        Fuel_Amount = 1500
        
        

else:
    print("Should be higher than 0")


print(Fuel_Amount)


