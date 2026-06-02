def student_result():

    # Taking input from user
    percentage = float(input("Enter your percentage: "))

    # List
    details = ["Student Percentage", percentage]

    # For Loop
    for i in details:
        print(i)

    # Control Flow
    if percentage >= 90:
        print("Grade: A+")
        print("Excellent Performance!")

    elif percentage >= 75:
        print("Grade: A")
        print("Very Good Performance!")

    elif percentage >= 50:
        print("Grade: B")
        print("Good Performance!")

    elif percentage >= 40:
        print("Grade: C")
        print("You Passed!")

    else:
        print("Grade: F")
        print("You Failed!")


# Function Call
student_result()
