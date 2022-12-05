sandwich_orders = ['pastrami', "hamburger", "cheese burger", 'pastrami', "chicken sandwich", 'pastrami', "big mac", "whopper burger"]
finished_sandwiches =[]

print("The Deli has run out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print()
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made a " + current_sandwich)
    finished_sandwiches.append(current_sandwich)
print()
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title() + " is done")