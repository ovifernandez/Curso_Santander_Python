print("Hello World")

name = "Juan"
age = 25
height = 1.75
is_student = True
a = b = c = 10

grade = 85

if grade >= 90:
    print ("Excellent")

elif grade >= 80:
    print ("Very good")

elif grade >= 70:
    print ("Good")

else:
    print ("Needs improvement")


fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)

counter = 0

while counter < 5:

    print(counter)
    counter += 1

for i in range(10):

    if i % 2 == 0:
        continue
    print(i)