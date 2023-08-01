print("\n")
print('\033[1m' +"HI, WELCOME TO HUSSAIN'S BINARY-DECIMAL CONVERTER")
print ('\033[0m')
val=0
def bdconverter():
    global val
    print("choose the option",'\n','1.binary to decimal','\n','2.decimal to binary','\n','3.exit','\n')
    val=int(input("enter your option:",))
    try:
        if(val==1):
            a=str(input("enter the binary number: "))
            if all(i in ('1','0') for i in a):
                deci_num=0
                for i in range(len(a)):
                  digit = int(a[i])
                  deci_num += digit * 2**(len(a)-i-1)
                print("decimal of",a,"=", deci_num)
            else:
                print("please check your entry")
            print("________________________________________________________________________________________________________________________________")
        elif(val==2):
            b=int(input("enter the decimal number: "))
            if(type(b)is int):     
                def decimal_binary(b):
                    if int(b) >= 1:
                        decimal_binary(int(b) // 2)
                        print(int(b) % 2, end = '')
                print("binary of",b,'=')
                decimal_binary(b)
            else:
                print("please enter a decimal")
        
            print("\n","________________________________________________________________________________________________________________________________")
        elif val ==3:
                def exit():
                    ans= str(input("Are you sure you want to exit?. Type yes or no:: "))
                    if ans == "yes":
                        print('\033[1m' +"THANK YOU FOR USING bd converter.","\n","HAVE A NICE DAY")
                        print ('\033[0m')
                    elif ans=="no":
                        print("_____________________________________________________________________________________________________")
                        bdconverter()
                    else:
                        print("enter a valid answer")
                        exit()
                exit()                  
        else:
            print("enter a valid number")               
    except ValueError:
            print("please enter only valid entries")
            print("____________________________________________________________________________________________________________________")
while(val >=0 and val!=3):    
    bdconverter()