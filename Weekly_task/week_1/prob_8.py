
"""Create a Python program that prompts the user to enter their age and checks if
they are eligible to vote. Use logical operators to check if the age is greater than or equal
to 18 and less than or equal to 120. Print a message indicating whether the person can vote or not."""

age=int(input("Enter your age :"))

if(age>=18)and(age<=120):
    print("Eligible to vote")
else:
    print("Not eligible to vote")
