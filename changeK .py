#!/usr/bin/env python
# coding: utf-8

# In[66]:


#strs is the given string.
#changek is the number of changes you can make,

def longSubseg(str_s, change_k):
     # represents the current window's starting index
    left = 0
    # stores the total number of zeros in the current window
    count = 0 
    # stores the maximum number of continuous 1's found
    window = 0 
    # stores the left index of maximum window found so far
    left_index = 0   
 
    # maintain a window `[left…right]` containing at most `k` zeroes
    for right in range(len(str_s)):
        if str_s[right] == "0":
            count = count + 1
        while count > change_k:
            if str_s[left] == "0":
                count = count - 1
            left = left + 1
        if right - left + 1 > window:
            window = right - left + 1
            left_index = left
 
    # no sequence found
    if window == 0:
        return
    print("The longest sequence is from index",
        left_index, "to index", (left_index + window - 1),"and it's length is:")
    return window
def main():
    #input for str$
    str_s = str(input ("input the binary string:"))
    #input for changeK
    change_k = int (input ("input the number of 0s to change to 1:"))
    if change_k >=0 and change_k <= len(str_s):
                    result = longSubseg(str_s, change_k)
                    print(result)
    else:
                    print("input a number between 0 and lenght of the string")

    
if __name__ == "__main__":
    main()





