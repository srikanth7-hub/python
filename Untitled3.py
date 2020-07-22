#!/usr/bin/env python
# coding: utf-8

# In[11]:


num=16
if num<0:
    print("enter a positive number")
else:
    
    sum=0
    while(num>0):
        sum+=num
        num-=1
        print("the sum is", sum)


# In[16]:


num=507
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            print(num,"is not a prime number")
            print(i,"times",num//i,"is",num)
            break
    else:
        print(num,"is aprime number")
else:
     print(num,"is not a prime number")


# In[ ]:





# In[ ]:





# In[ ]:




