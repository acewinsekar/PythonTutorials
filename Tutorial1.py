#import NumPy

#import SciPy

pi = 1.57

print("Hello, World")


if pi > 2:
    print("Pi is > 2")
else:
        print("pi is not > 2")

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x, y, z)

print (type(x), type(y), type(z))

x = "John"
# is the same as
y = 'John'

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python"
y = "is "
z = "awesome"
print(x + y + z)

#global variables = outside,
#local variables inside functions
x = "really awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

print(x)
def myfunc():
    global x
    x = "globally fantastic"

# call the myfunc function to assign the new global value of x
# else it won't get called
myfunc()

print ("Python is " + x)

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#e indicates raised to the power 10
print (x, y, z/100)


a = "Hello, World!"
print(len(a))


txt = "The best things in life are free!"
print("free" in txt)
#above, the "free in txt" parses to the boolean true/false

#Print only if "free" is present:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

b = "Hello, World!"
print(b[-5])
