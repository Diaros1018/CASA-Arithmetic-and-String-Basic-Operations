# Do not forget to change values for the variables fruit and s
# Do not forget to comment out the lines of code that will trigger Type and Index errors.


# Chapter 6.1 "A string is a sequence" code

fruit = 'orange'
letter = fruit[1]
print(letter)

x = 3
w = fruit[x - 1]
print(w)

# This line is commented because it causes a TypeError
# letter = fruit[1.5]


# Chapter 6.2 "Getting the length of a string using len" code

fruit = 'orange'
print(len(fruit))

length = len(fruit)
last = fruit[length - 1]
print(last)

# This line is commented because it causes an IndexError
# last = fruit[length]


# Chapter 6.3 "Traverse through a string with a loop" code

fruit = 'orange'
index = 0

while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

for letter in fruit:
    print(letter)


# Chapter 6.4 "String Slices" code

s = 'Hello Python'
print(s[0:5])
print(s[6:12])

print(s[:5])
print(s[6:])
print(s[:])
