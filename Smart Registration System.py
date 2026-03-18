student_id=input("Enter Your Student ID: ")
email_id=input("Enter Your Email ID: ")
password=input("Enter Your Password: ")
code=input("Enter Your Referral code: ")
count1=email_id.count("")
digit_count=(password.count('0') + password.count('1') + password.count('2') + password.count('3') + password.count('4')
             + password.count('5') + password.count('6') + password.count('7') + password.count('8') + password.count('9'))
#student_id verifictaion
if(len(student_id)==7 and student_id[0]=='C' and student_id[1]=='S' and student_id[2]=='E' and student_id[3]=='-'
    and student_id[4].isdigit() and student_id[5].isdigit() and student_id[6].isdigit()) :
    #email_id verifictaion
    if(email_id.count("@")>=1 and email_id.count(".")>=1 and email_id[0]!='@' and email_id[count1-2]!='@'
       and email_id[count1-5]=='.' and email_id[count1-4]=='e' and email_id[count1-3]=='d' and email_id[count1-2]=='u') :
        #password verification
        if(len(password)>=8 and password[0].isupper() and digit_count>=1) :
            #Referral_code verification
            if(len(code)==6 and code[0]=='R' and code[1]=='E' and code[2]=='F' and code[3].isdigit() and code[4].isdigit() and code[5]=='@') :
                print("APPROVED")
            else :
                print("REJECTED")
        else :
            print("REJECTED")
    else :
        print("REJECTED")
else :
    print("REJECTED")
