"""4 sub grade"""

sub1 = int(input("Enter the mark of sub1 out of 50"))
sub2 = int(input("Enter the mark of sub2 out of 50"))
sub3 = int(input("Enter the mark of sub3 out of 50"))
sub4 = int(input("Enter the mark of sub4 out of 50"))

total = sub3+sub2+sub1
if total==180:
    print(f"You have scored a total of {total}, you have secured A+ grade")
elif (total<=179) and (total>=160):
    print(f"You have scored a total of {total}, you have secured A grade")
elif (total<=159) and (total>=140):
    print(f"You have scored a total of {total}, you have secured B+ grade")
elif (total<=139) and (total>=120):
    print(f"You have scored a total of {total}, you have secured B grade")
elif (total<=119) and (total>=100):
    print(f"You have scored a total of {total}, you have secured C grade")
else:
    print("Failed")

