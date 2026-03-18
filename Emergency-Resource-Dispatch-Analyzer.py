m=int(input("Enter Total Size: "))
request=[0]*m
for i in range(m):
    request[i]=int(input(f"Enter Element {i}: "))
print(f"Your List: {request}")
low_demand=[]
moderate_demand=[]
high_demand=[]
invalid_request=[]
name=input("Enter Your Full Name: ")
L=len(name)-name.count(" ")
PLI=L%3
invalid=0
no_demand=0
a,b,c=0,0,0
for i in range(m):
    if(request[i]<0):
        invalid+=1
        n=request[i]
        invalid_request=invalid_request+[n]
    elif(request[i]==0):
        no_demand+=1
    elif(1<=request[i]<=20):
        a+=1
        n=request[i]
        low_demand=low_demand+[n]
    elif(21<=request[i]<=50):
        b+=1
        n=request[i]
        moderate_demand=moderate_demand+[n]
    else:
        c+=1
        n=request[i]
        high_demand=high_demand+[n]

print("Before filtering")
print(f"Invalid_Request:{invalid_request}")
print(f"Low_Demand:{low_demand}")
print(f"Moderate_Demand:{moderate_demand}")
print(f"High_Demand:{high_demand}")
print(f"Total Valid Request Before filtering:{no_demand+a+b+c}")
print("after filtering")
if(PLI==0):
    print(f"Invalid_Request:{invalid_request}")
    low_demand=[]
    print(f"Low_Demand:{low_demand}")
    print(f"Moderate_Demand:{moderate_demand}")
    print(f"High_Demand:{high_demand}")
    print(f"Total Valid Request after filtering:{no_demand+b+c}")
    print(f"Removed Due to PLI: {a}")
    print(f"L:{L}")
    print(f"PLI:{PLI}")
if(PLI==1):
    print(f"Invalid_Request:{invalid_request}")
    print(f"Low_Demand:{low_demand}")
    print(f"Moderate_Demand:{moderate_demand}")
    high_demand=[]
    print(f"High_Demand:{high_demand}")
    print(f"Total Valid Request after filtering:{no_demand+a+b}")
    print(f"Removed Due to PLI: {c}")
    print(f"L:{L}")
    print(f"PLI:{PLI}")
if(PLI==2):
    print(f"Invalid_Request:{invalid_request}")
    low_demand=[]
    print(f"Low_Demand:{low_demand}")
    print(f"Moderate_Demand:{moderate_demand}")
    high_demand=[]
    print(f"High_Demand:{high_demand}")
    print(f"Total Valid Request after filtering:{no_demand+b}")
    print(f"Removed Due to PLI: {a+c}")
    print(f"L:{L}")
    print(f"PLI:{PLI}")
print(f"Total Invalid requests: {invalid_request}")
print(f"Requests with No Demand: {no_demand}")


