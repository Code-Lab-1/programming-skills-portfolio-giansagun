while True:
    age = input("How old are you? ")
    
    age = int(age)
    if age < 3:
        print("Your fee for Cinema ticket is free")
    elif age < 12:
        print("Your fee for cinema ticket is $10") 
    else:
        print("Your fee for cinema ticket is $15")