#Find the grade based on marks
marks = float(input("Enter marks: "))
if marks >=90:
    print("A")
elif marks >= 80 and marks < 90:
    print("B")
elif marks >= 70 and marks <80:
    print("C")
else: 
    print("D")