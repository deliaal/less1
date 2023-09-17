var = -2 #int
a = 3.14 #float
string = 'My Text' #string
boolean = True #sau False = 0

#print(var)
#print(a)
#print(string)
#print(boolean)

#print(var * string)

#print(boolean + var)
#print(boolean - var)
#print(boolean * var)
#print(boolean / var)

#print(4/2)
#print(4/3)

#value_int = int(input("Enter a int\n")) #int
#value_float = float(input("Enter a float\n")) #float
#value_string = int(input("Enter a int\n")) #string
#value_boolean = bool(input("Enter a boolean\n")) #boolean
#print(value_float)

#str_var = "4"
#print(int(str_var))
#print(float(str_var))
#print(bool(str_var))

#major = 18
#var_input = int(input("Enter a number"))

#if major < var_input : #Condition 1
    #print(major , "<", var_input) ##True
#elif major == var_input : #Condition 2
    #print("=")
#else: #Else
    #print(">") #False

#var1 = "string"
#var2 = input("Enter a value")
#if var1 == var2 :
    #print("la fel")
#else:
    #print("diferite")

#for count in range(-10, 10) :
    #print(count)

#var = 55
#while var < 100:
    #print(var) #1
    #var = var + 10

import random

var_check = random.randint(0, 25)
var_in = int(input("Enter a number"))

while var_in != var_check:
    if var_in < var_check:
        print("Less than need")
    else:
        print("More than need")
    var_in = int(input("Enter a number"))