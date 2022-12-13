#introduction message
print ("In this program you must solve for the area of a rectangle.")

#get length from user
length = float(input("Enter the length of the rectangle (cm): "))

#get width from user
width = float(input("Enter the width of the rectangle (cm): "))

#calculate area
area = length * width

#ask user for their answer
answer = float(input("Enter the area of the rectangle (cm squared): "))

#if answer is right statement
if answer == area:
  print ("You are correct!")

#if anmswer is wrong statment
if answer > area:
  print ("You are wrong. The area of the rectangle is " + format(area) + "cm squared.")
  if answer < area:
    print ("You are wrong. The area of the rectangle is " + format(area) + "cm squared.")