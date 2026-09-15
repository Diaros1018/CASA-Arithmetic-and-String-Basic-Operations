# Do not forget to change values for the variables fruit and s
# Do not forget to comment out the lines of code that will trigger Type and Index errors.


# Chapter 6.1 "A string is a sequence" code

fruit = 'orange'
letter = fruit[1]
print(letter)

letter = fruit[0]
print(letter)

# This line causes a TypeError, so it is commented out
# letter = fruit[1.5]


# Chapter 6.2 "Getting the length of a string using len" code

fruit = 'orange'
print(len(fruit))

length = len(fruit)

# This line causes an IndexError, so it is commented out
# last = fruit[length]

last = fruit[length - 1]
print(last)

print(fruit[-1])
print(fruit[-2])


# Chapter 6.3 "Traverse through a string with a loop" code

fruit = 'orange'

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

for char in fruit:
    print(char)


# Chapter 6.4 "String Slices" code

s = 'Hello Python'
print(s[0:5])
print(s[6:12])

fruit = 'orange'
print(fruit[:3])
print(fruit[3:])
print(fruit[3:3])