# Modifying Elements in a list
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# Appending elements to the end of a list
motorcycles = ['honda','yamaha','suzuki']
motorcycles.append('ducati')
print(motorcycles)

# The append() method makes it easy to build lists dynamically. For example you can start with an empty list and then add items to the list using a series of append() calls.
motorcycles = []
motorcycles.append('honda'.title())
motorcycles.append('yamaha'.title())
motorcycles.append('suzuki'.title())
motorcycles.append('kawasaki'.title())
print(motorcycles)

# Inserting Elements into a list 
# You can add a new element at any position in your list by using the inser() method. 
motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(2, 'vitacci')
print(motorcycles)

# Removing elements from a list
# If you know the position element of the item you want to remove from a list, you can use the del statement.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

# Removing an item using the pop() method
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# Removing an Item by Value 
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

# You can also use the remove() method to work with a value that's being removed from a list.
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")