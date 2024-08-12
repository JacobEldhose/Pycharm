"""A student will not be able to sit for the exam if his/her attendance is less than 75%.
Take the following input from the user No. of classes held, No. of classes attended and print class percentage, is
student allowed to sit for the exam"""


classes = int(input("Enter the number of class held: "))
att = int(input("Enter the number of classes attended"))

att_perc = (att/classes)*100
if att_perc < 75:
    print(f"Your attendance percentage is {att_perc}, You will not be able to attend the exam")
else:
    print(f"Your attendance percentage is {att_perc}, You will be able to attend the exam")
