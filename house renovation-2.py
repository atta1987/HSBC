#!/usr/bin/env python
# coding: utf-8

# In[7]:


#program that will chose the houses which will be renovated
def RenovateHouses (houses):
    #check if it is in the english alphabet
    ch='a'
    if (ch>='a' and ch<='z') or (ch>='A' and ch<='Z'):
        consonants = ['b', 'c', 'd', 'f', 'g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z',
                      'B', 'C', 'D', 'F', 'G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
        #assigning mylist the value of all the houses with consonants
        mylist = [item for item in houses if item in consonants]
        print('The houses that will not be renovated are:')
        return mylist
           
def main():
    houses = str(input('give the list of the houses:'))
    result=RenovateHouses(houses)
    print(result)
if __name__ == "__main__":
    main()
    
    


# In[ ]:





# In[ ]:




