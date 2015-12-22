
def make_new_row(old_row):
    if old_row==[]:
        return [1]
    if old_row==[1]:
        return [1,1]
    new_row=[1]

    
    for i in range(len(old_row)-1):
        new_row.append(old_row[i]+old_row[i+1])

    new_row.append(1)
    return new_row

user_input=int(input("Enter the desired height of Pascal's triangle:"))

empty_list=[]


for i in range(user_input):
    if i==0:
       a = make_new_row([])
       empty_list.append(a)
       #print(a)
    else:
       a = make_new_row(a)
       empty_list.append(a)
       #print(a)

##for item in empty_list:
##    print(item)

print(empty_list)
           
    

    
