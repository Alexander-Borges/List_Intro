#Accessing Elements in a list
bicycles = ["trek","cannondale","redline","specialized"]
print(bicycles)

print(bicycles[0].title()) #will return Trek with the first letter capitalized

print(bicycles[1]) # will return cannondale
print(bicycles[3]) # will return specialized

print(bicycles[-1]) # accesses the last element in a list, thus will return specialized

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
