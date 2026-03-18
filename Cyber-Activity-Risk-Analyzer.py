m=int(input("Enter Total Size: "))
activity_score=[0]*m
for i in range(m):
    activity_score[i]=int(input(f"Enter Element {i}: "))
print(f"Your List: {activity_score}")
low_risk=[]
medium_risk=[]
high_risk=[]
critical_risk=[]
D=int(input("Enter Last Digit of Your Reistration Id: "))
valid=0
invalid=0
j=0
k=0
for i in range(m):
    if(activity_score[i]<0):
        invalid+=1
    elif(0<=activity_score[i]<=30):
        valid+=1
        n=activity_score[i]
        low_risk=low_risk+[n]
        j=j+1
    elif(31<=activity_score[i]<=60):
        valid+=1
        n=activity_score[i]
        medium_risk=medium_risk+[n]
    elif(61<=activity_score[i]<100):
        valid+=1
        n=activity_score[i]
        high_risk=high_risk+[n]
    else:
        k=k+1
        valid+=1
        n=activity_score[i]
        critical_risk=critical_risk+[n]

print(f"Register Digit (D):{D}")

print("Before Personalized Filtering: ")
print(f"Low_Risk: {low_risk}")
print(f"Medium Risk: {medium_risk}")
print(f"High Risk: {high_risk}")
print(f"Critical Risk: {critical_risk}")

print("After Personalized Filtering: ")
if(D%2==0):
    low_risk=[]
    print(f"Low_Risk: {low_risk}")
else:
    print(f"Low_Risk: {low_risk}")
print(f"Medium Risk: {medium_risk}")
print(f"High Risk: {high_risk}")
if(D%2!=0):
    critical_risk=[]
    print(f"Critical Risk: {critical_risk}")
else:
    print(f"Critical Risk: {critical_risk}")
print(f"Total Valid Entries: {valid}")
print(f"Ignored Entries: {invalid}")
if(D%2==0):
    print(f"Removed Due to Personalization: {j}")
else:
    print(f"Removed Due to Personalization: {k}")

