name=input("Enter Your Full Name: ")
email=input("Enter Your Email: ")
number=input("Enter Your Phone Number: ")
age=int(input("Enter Your Age: "))
count1=name.count(" ")
count2=email.count("@")
count3=email.count(".")
count4=number.count("")
count5=name.count("")
digit_count=(number.count('0')+number.count('1')+number.count('2')+number.count('3')
             +number.count('4')+number.count('5')+number.count('6')+number.count('7')
             +number.count('8')+number.count('9'))
if(count1 and name[0]!=" " and name[count5-2]!=" ") :
    if(count2 and count3 and email[0]!="@") :
        if(count4==11 and number[0]!="0" and digit_count==10) :
            if(age>=18 and age<=60) :
                print("User Profile is VALID")
            print("User Profile is INVALID")
        print("User Profile is INVALID")
    print("User Profile is INVALID")
else :
    print("User Profile is INVALID")



