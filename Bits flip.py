#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Program to find minimum flips to convert message P to message Q
def flipped_bits(num1, num2):

    # initially flips is equal to 0
    flips = 0
    
    # & each bits of num1 && num2 with 1
    # if t1 != t2 then we will flip that bit
    while(num1 > 0 or num2 > 0):
        t1 = (num1 & 1)
        t2 = (num2 & 1)
        if(t1 != t2):
            flips += 1

        # right shifting num1 and num2
        num1>>=1
        num2>>=1
    
    return flips
    
def main():
    #input for num1
    num1 = int(input('Input the first integer:'))
    #input for num2
    num2 = int(input('Input the seconde integer:'))
    result = flipped_bits(num1, num2)
    print('The minimum number of flips is:',result)
if __name__ == "__main__":
    main()




# In[ ]:





# In[ ]:




