# Try these short programs to get some firsthand experience with Python's lists. 

# 1 Names: Store the names of a few of your friends in a list called names. Print each person's name by accessing each element in the list, one at a time.
friends = ['Mike','John','Daniel','Nate','Jackson']
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print(friends[4])

# 2 Greetings: Start with the list you used in Exercise 1 but instead of just printing each person's name, print a message to them. The text of each message should be the same, but each message should be personalized with the person's name. 
print(f"Hey {friends[0]}, we should catch up soon!")
print(f"Hey {friends[1]}, we should catch up soon!")
print(f"Hey {friends[2]}, we should catch up soon!")
print(f"Hey {friends[3]}, we should catch up soon!")
print(f"Hey {friends[4]}, we should catch up soon!")

# 3 Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statement about these items, such as "I would like to own a Honda motorcycle."
exotic_cars = ['Porsche','Lamborghini',"Ferrari","Aston Martin"]
print(f"I want my first splurge purchase to be a {exotic_cars[0]}.")
print(f"I'll really know that I have made it if I'm driving around in a {exotic_cars[1]}.")
print(f"And after that day comes, I'll have to decide if I want to take the {exotic_cars[2]} or the {exotic_cars[3]}.")

# 4 Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you'd like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner. 
guest_list = ['Will Swan','Marc Okubo', 'Jimi Hendrix']
print(f"Would you like to come to dinner {guest_list[0]}?")
print(f"Would you like to come to dinner {guest_list[1]}?")
print(f"Would you like to come to dinner {guest_list[2]}?")

# 5 Changing Guest List: You just heard that one of your guests can't make the dinner, so you need to send out a new set of invitations. You'll have to think of someone else to invite.
guest_list.pop(0)
guest_list.insert(2,'Jason Richardson')
print(f"Would you like to come to dinner {guest_list[0]}?")
print(f"Would you like to come to dinner {guest_list[1]}?")
print(f"Would you like to come to dinner {guest_list[2]}?")

# 6 More Guests: You just found a bigger dinner table, so now more space is available. Think of 3 more guests to invite to dinner
guest_list.insert(3,'Tom Morello')
guest_list.insert(4,'Dan Jacobs')
guest_list.append('Dan Sugarman')
print(f"Would you like to come to dinner {guest_list[3]}?")
print(f"Would you like to come to dinner {guest_list[4]}?")
print(f"Would you like to come to dinner {guest_list[5]}?")

# 7 Shrinking Guest List: You just found out that your new dinner table won't arrive in time for dinner, and you have space for only two guests.
# - start with your program from Exercise 6. Add a new line that prints a message saying that you can only invite two people for dinner.
# - use pop() to remove guests from your list one at a time until only two names remain on your list, print a message to that person letting them know you're sorry you can't invite them to dinner.
# - Print a message to each of the two people still on your list, letting them know they're still invited.
# - Use del to remove the last two names from your list, so you have an empty list
print('\n',guest_list)
for item in guest_list:
    print(f"I apologize {item} as I can actually only invite two guests for dinner tonight.")

popped_guest1 = guest_list.pop()
print(f"My deepest regrets that I cannot invite you tonight, {popped_guest1}.")

popped_guest2 = guest_list.pop()
print(f"My deepest regrets that I cannot invite you tonight, {popped_guest2}.")

popped_guest3 = guest_list.pop()
print(f"My deepest regrets that I cannot invite you tonight, {popped_guest3}.")

popped_guest4 = guest_list.pop()
print(f"My deepest regrets that I cannot invite you tonight, {popped_guest4}.")

print(guest_list)

for item in guest_list:
    print(f"I am very pleased to let you know that I am still able to invite you, {item}.")

del guest_list[1]
del guest_list[0]
print('\n', guest_list)

# 8 Seeing the World: Think of at least 5 places in the world you'd like to visit.
# - Store the locations in a list. Make sure the list is not in alphabetical order.
# - Print your list in its original order. 
# - Use sorted() to print your list in alphabetical order by printing it.
# - Show that your list is still in its original order by printing it.
# - Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
# - Show that your list is still in its original order by printing it again.
# - Use reverse() to change the order of your list. Print the list to show that its order has changed.
# - Use reverse() to change the order of your list again. Print the list to show it's back to its original order.
# Use sort() to change your list so it's stored in alphabetical order. Print the list to show that its order has been changed. 
locations = ['Paris','Chicago','Barcelona','Rome','Madrid']
print(locations)
print(sorted(locations))
print(locations)
locations.sort(reverse=True)
print(locations)
locations.sort(reverse=False)
print(locations)
locations.sort()
print(locations)

guest_list = ['Will Swan','Marc Okubo', 'Jimi Hendrix']
print(len(guest_list))

