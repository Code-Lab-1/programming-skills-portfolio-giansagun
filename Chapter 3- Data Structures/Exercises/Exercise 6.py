guests = ['Gian Sagun', 'John Lubbui', 'Dan Franco']

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")


del(guests[1])
guests.insert(1, 'Arjay Visperas')


name = guests[0].title()
print(f"\n{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")


print("\nSorry, we can only invite two people to dinner.")

name = guests.pop()
print(f"Sorry, {name.title()} I can't invite you to the dinner.")


name = guests[0].title()
print(f"{name}, please come to dinner, you are still invited.")

name = guests[1].title()
print(f"{name}, please come to dinner, you are still invited.")

del(guests[0])
del(guests[0])


print(guests)