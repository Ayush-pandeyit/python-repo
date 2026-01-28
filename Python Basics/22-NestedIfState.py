# What is a Nested IF Statement?
# A nested if statement is an if statement inside another if statement.
# It allows you to check multiple conditions in a hierarchy -you
# only check the inner condition if the outer condition is true first.

age = 20
has_license = True

if age >= 18:
    print("You are an adult")
    if has_license:
        print("You can drive!")
    else:
        print("But you need a license to drive")
else:
    print("You are too young to drive")

# Another Example: Grade System

score = 85
attendance = 90

if score >= 50:
    print("You passed!")

    if attendance >= 75:
        if score >= 90:
            print("Grade: A+ (Excellent attendance)")
        elif score >= 80:
            print("Grade: A (Good attendance)")
        else:
            print("Grade: B")
    else:
        print("Grade: C (Poor attendance)")
else:
    print("You failed")
