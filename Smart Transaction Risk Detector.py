n=int(input("Enter number of transaction:"))
transaction_amounts= [int(input(f"Enter transaction{i+1}:")) for i in range(n)]
print(transaction_amounts)
normal=0
large=0
high_risk=0
invalid=0
valid=0
inv_count=0
categorized={
    "normal":[],
    "large":[],
    "high_risk":[],
    "invalid":[]
}
total=0
for i in range(n):
    if(transaction_amounts[i]<=0):
        categorized["invalid"] = categorized["invalid"] + [transaction_amounts[i]]
        inv_count+=1
    elif(1<=transaction_amounts[i]<=500):
        categorized["normal"] = categorized["normal"] + [transaction_amounts[i]]
        normal+=1
        total+=transaction_amounts[i]
    elif(501<=transaction_amounts[i]<=2000):
        categorized["large"] = categorized["large"] + [transaction_amounts[i]]
        large+=1
        total+=transaction_amounts[i]
    else:
        categorized["high_risk"] = categorized["high_risk"] + [transaction_amounts[i]]
        high_risk+=1
        total+=transaction_amounts[i]
frequent=False
if (n>5):
    frequent=True
large_spending=False
if (total>5000):
    large_spending=True
suspicious=False
if (high_risk)>=3:
    suspicious = True

risk=""
if suspicious==True:
    risk="High Risk"
elif frequent==True and large_spending==True:
    risk="High Risk"
elif frequent==True:
    risk="Moderate Risk"
elif large_spending==True:
    risk="Moderate Risk"
else:
    risk="Low Risk"

print("Categorized Transactions:")
print("Normal:",categorized["normal"])
print("Large:",categorized["large"])
print("High Risk:",categorized["high_risk"])
print("Invalid:",categorized["invalid"])
print("Total Transaction Value:",total)
print("Number of Transactions:",n)
print("Risk Classification:",risk)
