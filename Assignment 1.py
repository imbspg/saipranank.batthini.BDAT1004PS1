#!/usr/bin/env python
# coding: utf-8

# # Q1) Finding Data Type
# 

# In[1]:


# 5
data = 5
print(type(data))


# Hence the data type is "Integer"

# In[2]:


# 5.0
data = 5.0
print(type(data))


# Hence the data type is "Float"

# In[14]:


# 5 > 1
data = 5 > 1
print (data)
print(type(data))


# Hence the data type is "Boolean"

# In[4]:


# '5'
data = '5'
print(type(data))


# Hence the data type is "String"

# In[15]:


# 5 * 2
data = 5 * 2
print(data)
print(type(data))


# Hence the data type is "Integer"

# In[16]:


# '5' * 2
data = '5' * 2
print(data)
print(type(data))


# Hence data type is "String"

# In[17]:


# '5' + '2'
data = '5' + '2'
print(data)
print(type(data))


# Hence data type is "String"

# In[18]:


# 5 / 2
data = 5 / 2
print(data)
print(type(data))


# Hence data type is "Float"

# In[20]:


# 5 % 2
data = 5 % 2
print(data)
print(type(data))


# Hence data type is "Integer"

# In[21]:


# {5,2,1}
data = {5,2,1}
print(type(data))


# Hence data type is "Set"

# In[24]:


# 5 == 3
data = 5==3
print(data)
print(type(data))


# Hence data type is "Boolean"

# In[25]:


# pi (3.15)
data = pi(3.15)
print(data)
print(type(data))


# # Q2) Python Expression for following questions:

# In[27]:


# A) How many letters are there in 'Supercalifragilisticexpialidocious'?
text = len("Supercalifragilisticexpialidocious")
print (text)


# Hence there are 34 letters in the word 'Supercalifragilisticexpialidocious'

# In[28]:


# B) Does 'Supercalifragilisticexpialidocious' contain 'ice' as a substring? 
text = 'Supercalifragilisticexpialidocious'
#Now to find the 'ice' in the string
finalresult = text.find('ice')
print (finalresult)


# Hence the above text contains 'ice' after the 18th position

# In[29]:


# C) Which of the following words is the longest: Supercalifragilisticexpialidocious, Honorificabilitudinitatibus, or Bababadalgharaghtakamminarronnkonn?
text1 = 'Supercalifragilisticexpialidocious'
print(len(text1))

text2 = 'Honorificabilitudinitatibus'
print(len(text2))

text3 = 'Bababadalgharaghtakamminarronnkonn'
print(len(text3))


# Hence the longest words are 'Supercalifragilisticexpialidocious' and 'Bababadalgharaghtakamminarronnkonn'

# In[3]:


# D) Which composer comes first in the dictionary: 'Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'. Which one comes last?
dict= {'Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'}
print(min(dict) + 'comes fordt in the dictionary while ' + max(dict) + ' comes last in the dictionary ' )


# # Q3) Implementing triangle Area Formula

# In[43]:


# Sides of triangle are A,B and C
# To input the values
A = float(input("Enter first side value: "))
B = float(input("Enter Second side vlaue: "))
C = float(input("Enter Third side value: "))

#first of all semi perimeter is calculated

d = (A+B+C) / 2

#now calculate the area

area = (d*(d-A)*(d-B)*(d-C)) ** 0.5

print (area)


# Hence the area of triangle is 1.7320508075688772

# # Q4) Python Program to seperate odd and even integers
# 

# In[58]:



numbers = []

#now asking user to enter the numbers
a = int(input("Enter number of elements: "))
    
#now looping the elements and appending it to the numbers

for x in range (1, 1+a):
    elements = int(input("enter the element: "))
    numbers.append(elements)
    
    #now seperating the elements as odd and even number
    #for even number, the element should be even number
    
evenlist = []
oddlist = []
    
for e in numbers:
    if e % 2 == 0: #divisible by 2
        evenlist.append(e)
    
    else:
            oddlist.append(e)
        

#now printing evenlist and oddlist

print ("Even Numbers are: ", evenlist)
print ("Odd Numbers are: ", oddlist)
    
    

    
    


# Hence, the above is the answer of odd numbers and even numbers

# # Q5 - A) Write a function inside(x,y,x1,y1,x2,y2) that returns True or False depending on whether the point (x,y) lies in the rectangle with lower left corner (x1,y1) and upper right corner (x2,y2).

# In[65]:


#defining the findpoints
def inside(x1, y1, x2, y2, x, y) :
    if (x > x1 and x < x2 and y >y1 and y < y2):
        return True
    else:
        return False

#allowing code to run
if __name__ == "__main__" :    
    
    x1, y1, x2, y2, = 0, 0, 2, 3
    
    #for x and y = -1 , -1
    x, y = -1, -1



    if inside(x1, y1, x2, y2, x,y):
        print("True")
    else:
        print("False")
        
   


# # Q5 - B) Use function inside() from part a. to write an expression that tests whether the point (1,1) lies in both of the following rectangles: one with lower left corner (0.3, 0.5) and upper right corner (1.1, 0.7) and the other with lower left corner (0.5, 0.2) and upper right corner (1.1, 2).

# In[67]:


def inside(x1, y1, x2, y2, x, y) :
    if (x > x1 and x < x2 and y >y1 and y < y2):
        return True
    else:
        return False

#allowing code to run
if __name__ == "__main__" : 
    
    #for rectangle with lower left corner 0.3, 0.5 and upper right corner 1.1, 0.7
    x1, y1, x2, y2, = 0.3, 0.5, 1.1, 0.7
    
    #for x and y = 1 , 1
    x, y = 1, 1



    if inside(x1, y1, x2, y2, x,y):
        print("True")
    else:
        print("False")
        
    #for rectangle with upper right corner 0.5, 0.2 and upper right corner 1.1, 2
    x1, y1, x2, y2, = 0.5, 0.2, 1.1, 2
    
    #for x and y = 1 , 1
    x, y = 1, 1



    if inside(x1, y1, x2, y2, x,y):
        print("True")
    else:
        print("False")
        
        
        


# # Q6) Turning word into pig-Latin

# In[11]:


print ('Please enter a word')
x = input()
y = x.lower()
z = y[0]
a = ['a','e','i','o','u']
b = len (y)
c = str(z in a)
d = 1
e = b-1
f =''
while (d<=e):
    f = f+y[d]
    d = d +1

e = ''
if (c=='True'):
    e = b + 'way'
else:
    e = f + z + 'ay'
print('The pigLatin of ' + x + ' is: ' + e) 


# # Q7) Question 7 File bloodtype1.txt records blood-types of patients (A, B, AB, O or OO) at a clinic.Write a function bldcount() that reads the file with name name and reports (i.e.,prints) how many patients there are in each bloodtype.

# In[68]:


#defining the function
def bldcount(bloodgroup):
    
    #now breaking the given bloog group string
    
    bloodgroup_list = bloodgroup.split()
    
    #giving the set to the bloodgroup_list
    
    test = set(bloodgroup_list)
    
    for x in test :
        print("There are", bloodgroup_list.count(x), "patients of blood group type", x)

        # to run code
if __name__ == "__main__":
    
    bloodgroup = 'AB AB B O A A AB O AB A O O A A A O O O AB O A A A A A AB AB A AB O AB O A O O O AB O AB AB AB A A O '
    
    #finally calling the bldcount function
    
    bldcount(bloodgroup)


# # Q8) Currency Converter

# In[13]:


a = int(input("Enter the amount to convert in USD: "))
print('select option from below')
print ("A: AUD to USD")
print ("B: CHF to USD")
print ("C: CNY to USD")
print ("D: DKK to USD")
print ("E: EUR to USD")
print ("F: GBP to USD")
print ("G: HKD to USD")
print ("H: INR to USD")
print ("I: JPY to USD")
print ("J: MXN to USD")
print ("K: MYR to USD")
print ("L: NOK to USD")
print ("M: NZD to USD")
print ("N: PHP to USD")
print ("O: SEK to USD")
print ("P: SGD to USD")
print ("Q: THB to USD")

con = input("Select the type of converstion: ")
if con == 'A':
    print ('The USD Rate is',a*0.72)
if con == 'B':
    print ('The USD Rate is',a*1.04)
if con == 'C':
    print ('The USD Rate is',a*0.15)
if con == 'D':
    print ('The USD Rate is',a*0.14)
if con == 'E':
    print ('The USD Rate is',a*1.07)
if con == 'F':
    print ('The USD Rate is',a*1.26)
if con == 'G':
    print ('The USD Rate is',a*0.13)
if con == 'H':
    print ('The USD Rate is',a*0.013)
if con == 'I':
    print ('The USD Rate is',a*0.0079)
if con == 'J':
    print ('The USD Rate is',a*0.015)
if con == 'K':
    print ('The USD Rate is',a*0.23)
if con == 'L':
    print ('The USD Rate is',a*0.11)
if con == 'M':
    print ('The USD Rate is',a*0.65)
if con == 'N':
    print ('The USD Rate is',a*0.019)
if con == 'O':
    print ('The USD Rate is',a*0.10)
if con == 'P':
    print ('The USD Rate is',a*0.73)
if con == 'Q':
    print ('The USD Rate is',a*0.029)

print("Thank you for using converter")


# # Q9) Identifying the Exception

# In[70]:


#A) Adding 6 + 'a'

test = 6 + 'a'
print (test)


# Integer and String cannot be added

# In[77]:


#B) Referring 12th item of a list having 10 items

test = ['A','B','C','D','E','F','G','H','I','J','K','L','M']
print (test[13])


# The error is known as Index Error i.e the list index is out of range while calling 13th position variable

# In[82]:


#C) Using a value that is out of range for a function’s input, such as calling math.sqrt(-1.0)
import math
math.sqrt(-1.0)


# The error is "Math Domain"

# In[84]:


#D) Using an undeclared variable, such as print(x) when x has not been defined 

print(z)


# Error is "Z" not defined. Hence the variable is not defined

# In[86]:


#E) Trying to open a file that does not exist, such as mistyping the file name or looking in the wrong directory. 
test = open("saipranank.txt", "r")
print(test.read())


# Error is : No suuch file or directory exisits.

# # Q10) Encryption is the process of hiding the meaning of a text by substituting letters in the message with other letters, according to some system. If the process is successful, no one but the intended recipient can understand the encrypted message. Cryptanalysis refers to attempts to undo the encryption, even if some details of the encryption are unknown (for example, if an encrypted message has been intercepted). The first step of cryptanalysis is often to build up a table of letter frequencies in the encrypted text. Assume that the string letters is already defined as 'abcdefghijklmnopqrstuvwxyz'. Write a function called frequencies() that takes a string as its only parameter, and returns a list of integers, showing the number of times each character appears in the text. Your function may ignore any characters that are not in letters. 

# In[14]:


import string
z = dict.fromkeys(string.ascii_lowercase, 0)
a = 'apple'
for x in a:
    x = a.lower()
    if x in z:
        z[x] += 1
        print(list(z.values()))


# In[ ]:





# In[ ]:




