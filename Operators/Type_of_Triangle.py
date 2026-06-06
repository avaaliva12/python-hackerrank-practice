#Determine the type of triangle
s1 = float(input("Enter 1st side: "))
s2 = float(input("Enter 2nd side: "))
s3 = float(input("Enter 3rd side: "))

if s1+s2 > s3 and s2+s3 >s1 and s1+s3>s2:
    print("valid triangle")
    if s1 == s2 == s3:
        print("Equilateral Triangle")
    elif s1 == s2 or s2 == s3 or s1 == s3:
        print("Isoceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("not a valid triangle")

