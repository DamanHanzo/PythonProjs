###################
# Damanpreet Singh
# Project 03
# singhdam
###################

#Checks if the initial input is a whole number
#Checks if the split value is whole number
#Checks if the initial number is divisible by the split value
#Splits the number initial whole number input into inputed split value
#Checks if the sequence is increasing or decreasing


while True:
    num=input("Input a large (whole number):")
    if num.isdigit():
        if num.isdigit()>0:
            break
    else:
        print("Please enter a whole number!")

while True:
    s=input("Input a split (whole number):")
    if s.isdigit():
        if len(num)%int(s)==0:    
            break
        else:
            print("Input a valid split value")
    else:
        print("Please enter a whole number!")

s=int(s)

final=""

increasing = True
prev = 0

for i in range(len(num)//s):
    final = final + num[i*s:(i+1)*s] + ', '
    if increasing:
        if int(num[i*s:(i+1)*s])<= prev:
            increasing = False
        else:
            increasing=True   
    prev = int(num[i*s:(i+1)*s])

final = final[:-2]
print(final)

if increasing:
    print("Squence is increasing")
else:
    print("Squence is not increasing")
