weight = int(input())
height = float(input())
x = weight/float(height*height);
if x < 18.5:
    print("Malnourished")
if x>=18.5 and  x<25:
    print("Normal")
if x>=25 and x<30:
    print("Fat")
if x>= 30:
    print("Obese")