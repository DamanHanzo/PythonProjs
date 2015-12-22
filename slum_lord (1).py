class Apartment(object):

    def __init__(self,number,bed_rooms,price,available=True):
        """initialize an apartment given:
              number - the apartment number (a string)
              bed_rooms - the number of bed rooms (int)
              price - the rental price (float)
              available - True, if the apartment is available; False, if its rented
        """
        self.number_ = number
        self.bed_rooms_ = bed_rooms
        self.price_ = price
        self.avail_ = available
    def __repr__(self):
        return "Apt. {}, # rooms {}, $$ {}, Living {}".format(self.number_,self.bed_rooms_,self.price_,self.avail_)
    def __str__(self):
        return self.__repr__()
        
    def get_number(self):
        """return the number of this apartment"""
        return self.number_

def testdriver1():
    A1 = Apartment("102",5,500,False)
    A2 = Apartment("A",2,650)
    A3 = Apartment("B",4,1000,True)
    print(A1)
    print(A2)
    print(A3)
    
        
class Building(object):

    def __init__(self,address,apartment_lst=[]):
        """initialize a building given:
                address - the street address (a string)
                apartment_lst - a list of the apartments in the building
        """
        self.address = address
        self.contents = {a.get_number():a for a in apartment_lst}
    def __repr__(self):
        final_str = ""
        for value in self.contents.values():
            final_str += str(value) + "\n"
        return final_str
    def __str__(self):
        return self.__repr__()

        
    
def testdriver2():
    bldg1 = Building("100 Main St", [Apartment("1B",1,450,False),
                                     Apartment("1A",2,650,True),
                                     Apartment("3",4,1500,False)])
    print(bldg1)
    
def building_dict(fname,bldg_dict):
    """store building information in a dict, which is keyed on the address
       Here:
         fname - name of file containing the building information (input)
         bldg_dict - dictionary to add the information to (input/output)
    """
    f_object = open(fname)
    cnt_bld = 1
    building_num = int(f_object.readline())
    while cnt_bld!=building_num:
        key = f_object.readline()
        aprt_info = f_object.readline().split(",")
        cnt=0
        aprt_ls = []
        while cnt!=len(aprt_info):
            aprt_ls.append(Apartment(aprt_info[cnt],aprt_info[cnt+1],aprt_info[cnt+2],aprt_info[cnt+3]))
            cnt+=4
        cnt_bld+=1
            
        
        
        
    ##NOTE!!!! This still needs to be made into the building class. This is not a finished copy!!!!!!         
    

def testdriver3():
    
    properties = {}
    building_dict('data.txt',properties)

    if properties:
        for addr in properties:
            print(properties[addr])
            print()
    else:
        print("No properties")
   

def manage_property(fname):
    pass        # replace with code
        

        
        
                  
        
            
