def student1():

    name1 = input("Enter your name: ")
    grades1 = int(input("enter your grades: "))
    grades2 = int(input("enter your grades: "))
    grades3 = int(input("enter your grades: "))
    grades4 = int(input("enter your grades: "))
    grades5 = int(input("enter your grades: "))

    gradest1 = [float(grades1), float(grades2), float(grades3), float(grades4), float(grades5)]
    average = sum(gradest1) / len(gradest1)

    print("")
    print("Name:", name1)
    print("Average:", average)

    if average > 90:
        print("Letter Grade: A")
    elif average > 80:
        print("Letter Grade: B")
    elif average > 70:
        print("Letter Grade: C")
    elif average >= 60:
        print("Letter Grade: D")
    else:
        print("Letter Grade: F")
    print("")



student1()
student1()
student1()
student1()
student1()
student1()
student1()