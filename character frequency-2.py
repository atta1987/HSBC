#!/usr/bin/env python
# coding: utf-8

# In[1]:


# program that return most frequent character in a string given a range [L,R]
def mostFrequent(strS, pairList):
    # Length of the String
    ls = len(strS)
    # Number of queries
    Q = len(pairList)
    # Prefix array
    pre = [[0 for i in range(256)]
            for i in range(ls)]

    # Iterate for all the characters
    for i in range(ls):

    # Increase the count of the character
        pre[i][ord(strS[i])] += 1

        if (i):

        # Update the prefix array
            for j in range(256):
                pre[i][j] += pre[i - 1][j]

    # Answer every query
    for i in range(Q):

        # Range
        l = pairList[i][0]
        r = pairList[i][1]
        m = 0
        c = 'a'

        # Iterate for all characters
        for j in range(256):
    
            # Times the lowercase character
            # j occurs till r-th index
            times = pre[r][j]

            # Subtract the times it occurred
            # till (l-1)th index
            if (l):
                times -= pre[l - 1][j]

            # Max times it occurs
            if (times > m):
                m = times
                c = chr(j)
                 
        print("Query ", i + 1,':',c)
    return 
    

            
def main():
    strS = str(input('input the string:'))
    pairList = []
    pairList_rows,pairList_cols = map(int, input().split())
    for idx in range (pairList_rows):
        pairList.append(list(map(int,input().split())))
        print(pairList)
    mostFrequent(strS,  pairList)
if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




