##############################
# singhdam                   #
# proj 04                    #
##############################


initial_input=input("Enter a prefix:")
initial_str=str(initial_input)
try:
    fp=open(initial_input+".old.txt",'r')
except FileNotFoundError:
    print("Please Enter a Valid Prefix!")

w_fp=open(initial_input+".new.txt",'w')
       
def get_number(one_line):
    return one_line[0:6].strip()
def get_balance(one_line):   
    return one_line[7:17].strip()
def get_name(one_line):
    return one_line[18:]
def equal_floats(x_flt,y_flt):
    if abs(x_flt-y_flt)<=1.0e-8:
        return True
    else:
        False
  
        

  
for line in fp:
    gn=get_name(line)
    gb=get_balance(line)
    gnum=get_number(line)
    
    while True:       
        trans_command=input("Please enter a transaction code(a,c,d,w): ")
        if trans_command=='d':
            deposit_input=input("Please Enter deposit amount:")
            try:
                deposit_input=int(deposit_input)
            except ValueError:
                print("Please enter a valid deposit amount")
                break
            if float(deposit_input)>=9999999.99:
                print("Cannot deposit amount bigger than '9999999.99'!")
                continue
            else:
                True
            account_balance=float(deposit_input)+float(gb)
            print(account_balance)
            gb=account_balance

        elif trans_command=='a':
            multiple=11-len(str(gb))
            new_line=(gnum + " "*multiple+ str(gb) + " " +gn)
            w_fp.write(new_line)
            print(("Name:{:<6s}Balance:{:<10}Account Number:{:<18}".format(gn,gb,gnum)))
            break
        elif trans_command=='w':
            withdraw_input=input("Please Enter the amount you would like to withraw:")
            if float(withdraw_input)<=float(gb):
                True
            else:
                print("Can't withdraw more money than currently available in the account!")
                continue
            account_balance=float(gb)-float(withdraw_input)
            print(account_balance)
            gb=account_balance
        elif trans_command=='c':
            if equal_floats(float(gb),0):
                print("Your account has been closed!","Good day!","Sir/M'am")
                break
            else:
                print("Still money in the account, can't close!")
            break
        else:
            print("Please enter a valid transaction code!")
            
w_fp.close()
fp.close()

        

    
