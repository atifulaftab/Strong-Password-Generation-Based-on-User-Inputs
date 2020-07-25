# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 19:42:06 2019
@author: atifulaftab & farhanazamanglory
"""

import numpy as np
import random
import string
import time


input_string = input("Enter your favorite five words and two numbers:\n ")
data  = input_string.split(",")
start=float(time.time())
print("\n")
print(data)

def capitalize_nth(s, n):
    return s[:n].lower() + s[n:].capitalize()
#data =["owl","ana","oct","vow","xeva","27","13"]
first_index= np.random.randint(0,4)
second_index= 0

for x in range(0,1000,1):
    second_index= np.random.randint(0,4)
    if(second_index!=first_index):
        break
    else:
       #print(first_index,second_index)
        print("\n")
       
       
first_string=data[first_index]
second_string=data[second_index]

uppper_bound=len(first_string)
uppper_bound=np.random.randint(1,uppper_bound)

first_string=capitalize_nth(first_string,uppper_bound)

y=np.random.randint(5,6)
number=data[y]
string_list=[number,first_string,second_string]
a=np.random.randint(0,2)
for x in range(0,1000,1):
    b= np.random.randint(0,2)
    if(a!=b):
        break
    else:
       #print(first_index,second_index)
        print("\n")
for x in range(0,3,1):
    if(a!=x and b!=x):
        c=x
password_characters = string.punctuation
final_String=string_list[a]+string_list[b]+random.choice(password_characters)+string_list[c]

for letter in final_String:
    if(letter=='a'):
        final_String=final_String.replace('a','@')
        break
    elif(letter=='A'):
        final_String=final_String.replace('A','@')
        break
    elif(letter=='s'):
        final_String=final_String.replace('s','$')
        break
    elif(letter=='S'):
        final_String=final_String.replace('S','$')
        break
    elif(letter=='i'):
        final_String=final_String.replace('i','!')
        break
    elif(letter=='I'):
        final_String=final_String.replace('I','!')
        break
    elif(letter=='r'):
        final_String=final_String.replace('r','#')
        break
    elif(letter=='R'):
        final_String=final_String.replace('R','#')
        break
    elif(letter=='x'):
        final_String=final_String.replace('x','%')
        break
    elif(letter=='X'):
        final_String=final_String.replace('X','%')
        break
    elif(letter=='q'):
        final_String=final_String.replace('q','&')
        break
    elif(letter=='Q'):
        final_String=final_String.replace('Q','&')
        break
    elif(letter=='c'):
        final_String=final_String.replace('c','(')
        break
    elif(letter=='C'):
        final_String=final_String.replace('C','(')
        break
    elif(letter=='j'):
        final_String=final_String.replace('j',')')
        break
    elif(letter=='J'):
        final_String=final_String.replace('J',')')
        break
    elif(letter=='k'):
        final_String=final_String.replace('k','<')
        break
    elif(letter=='K'):
        final_String=final_String.replace('K','<')
        break
    elif(letter=='l'):
        final_String=final_String.replace('l','|')
        break
    elif(letter=='L'):
        final_String=final_String.replace('L','|')
        break
    elif(letter=='v'):
        final_String=final_String.replace('v','^')
        break
    elif(letter=='V'):
        final_String=final_String.replace('v','^')
        break
    else:
        break

final_String=final_String+random.choice(password_characters)

print("\nOur generated password for you is:\n")
print(final_String)
end=float(time.time())
print("\nTotal time needed to generate it is:\n")
print(float(end-start))






























