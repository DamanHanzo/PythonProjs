import math

class Vector( object ):
    

    def __init__(self, x=0,y=0):

        self.__length = 0
        self.__angle = 0

        if type( x ) == int and type( y ) == int:

            self.__length = x
            self.__angle = y

    def __repr__( self ):

        return "Vector: {},{}".format( self.__length, self.__angle )

    def __str__( self ):

        return "Vector: {0:.2f},{1:.2f}".format( self.__length, self.__angle)
    
    def magnitude( self ):

        V=float(math.hypot(self.__length,self.__angle))

        return V

    def __add__(self, other):
        
        
        if type(other) != Vector:
            other = Vector (other)

        addition1 = (self.__length+other.__length)
        addition2 = (self.__angle+other.__angle)

        return Vector(addition1,addition2)
    
    def __sub__(self, other):

        if type(other) != Vector:
            other = Vector (other)

        subs1 = (self.__length-other.__length)
        subs2 = (self.__angle-other.__angle)

        return Vector(subs1,subs2)

    def __mul__(self,other):

        if type(other) == Vector:

            mul1=(self.__length*other.__length)
            mul2=(self.__angle*other.__angle)
            mul3=(mul1+mul2)


            return mul3

        elif type(other) == int or float:

            a = self.__length*other.__length
            b= self.__angle*other.__angle

            return Vector(a,b)

    def __eg__(self, other):

        flag=False

        if type(other) != Vector:
            other= Vector(other)
        
        if self.__length==other.__length and \
           self.__angle==other.__angle:
                flag=True

        return flag

        
def main():

    a = Vector(7,1)
    b = Vector(4,1)

    print(a-b)
    print(a*b)
    print(a+b)
    print(a==b)
main()

        
        
