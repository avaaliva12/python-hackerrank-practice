#Check if a triangle is valid
s1 = float(input("Enter 1st side: "))
s2 = float(input("Enter 2nd side: "))
s3 = float(input("Enter 3rd side: "))

if s1+s2 > s3 or s2+s3 >s1 or s1+s3>s2:
    print("valid triangle")
else:
    print("not a valid triangle")