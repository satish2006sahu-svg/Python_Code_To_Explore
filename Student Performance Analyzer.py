id="AP24110011620"
key=input("Enter Admin ID:-->")
if(id==key):
    n = int(input("Enter Total Students: "))
    marks = [0] * n
    valid = 0
    fail = 0
    for i in range(n):
        marks[i] = int(input(f"Enter marks:{i + 1}-->"))
    print("Input Marks:", marks)
    for i in range(n):
        if (90 <= marks[i] <= 100):
            print(f"{marks[i]} → Excellent")
            valid += 1
        elif (75 <= marks[i] <= 89):
            print(f"{marks[i]} → Very Good")
            valid += 1
        elif (60 <= marks[i] <= 74):
            print(f"{marks[i]} → Good")
            valid += 1
        elif (40 <= marks[i] <= 59):
            print(f"{marks[i]} → Average")
            valid += 1
        elif (0 <= marks[i] <= 39):
            print(f"{marks[i]} → Fail")
            valid += 1
            fail += 1
        else:
            print(f"{marks[i]} → Invalid")
    print(f"Total Valid Students: {valid}")
    print(f"Total Failed Students: {fail}")
else:
    print("Invalid Admin ID")
