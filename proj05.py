####################################################################################################
#Section 5  
#Computer Project #5     
####################################################################################################

#checks for the correct file name or else gives an error and ask for a filename again
#Gets the line from the file
#Indexes the line into id, name, latitude, longitude, diameter
#Ignores the first the three lines of the file 
#eligibility for the crater is defined
#if crater meets the eligibility then it is added to eligible list
#formats the eligible list and writes it to the file named craters.txt
#crater list calls read_craters function
#eligible_crater_list calls the get_eligible_craters function




def get_crater_tuple(line_str):
    line_str = line_str.split('\t')
    return (int(line_str[0]), line_str[1], float(line_str[2]), float(line_str[3]), float(line_str[4]))

def read_craters(filename):
    while True:
        try:
            file_obj=open(filename,'r')
            crater_list=[]
            file_obj.readline()
            file_obj.readline()
            file_obj.readline()
            for line in file_obj:
                crater_list.append(get_crater_tuple(line))
            file_obj.close()
            return crater_list
            break
        except IOError:
            print("Enter a valid filename")
            filename=input("Enter a filename:")
            

def get_eligible_craters(crater_list):
    eligible_list=[]
    for tup in crater_list:
        if tup[2]>-40 and tup[2]<50:
            if tup[3] >40 and tup[3]<135:
                if tup[4]>=60:
                    eligible_list.append(tup)
        #check if eligible, if so, add tup to eligible_list
    return eligible_list

def write_craters(eligible_crater_list):
    
    file_obj_write=open("craters.txt",'w')
    writer='{:>3}{:>15}{:>10}{:>10}{:>9} \n'.format("ID",'Name','Latitude','Longitude','Diameter')
    print(writer)
    file_obj_write.write(writer)
    for crater in eligible_crater_list:
        writer1=('{:>3d}{:>15s}{:>9.2f}{:>9.2f}{:>9.2f}\n'.format(crater[0],crater[1], crater[2],crater[3],crater[4]))
        file_obj_write.write(writer1)
        print(writer1)
    file_obj_write.close()
        
filename = input("Enter a filename: ") 
crater_list = read_craters(filename) 
eligible_crater_list = get_eligible_craters(crater_list)
write_craters(eligible_crater_list)

##Thanks for using my program!!
