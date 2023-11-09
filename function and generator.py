#!/usr/bin/env python
# coding: utf-8

# In[1]:


l=[4,5,6,'a','v']


# In[2]:


l.reverse()


# In[3]:


l


# In[4]:


l.remove(6)


# In[5]:


l


# In[6]:


l=l[::-1]


# In[7]:


l


# In[8]:


l.sort()


# In[12]:


l=[2,22,3,15,122,23]


# In[13]:


l.sort()


# In[14]:


l


# In[15]:


l.index(3)


# In[16]:


l.count()


# In[17]:


l.count(22)


# In[18]:


l.count(21)


# In[19]:


s='sudh'


# In[20]:


s[0]='a'


# In[21]:


s[0]


# In[22]:


s.replace('s','t')


# In[23]:


s


# In[24]:


l.replace(2,190)


# In[25]:


t=(2,3,4,5,"w","e","u",False,True,[2,3,4])


# In[26]:


type(t)


# In[27]:


t[-1]


# In[28]:


len(t)


# In[29]:


t["w",4]


# In[30]:


t[0,12]


# In[31]:


t[::-1]


# In[32]:


t


# In[37]:


s={23,12,34,'we',(2,3,4),[2.2,4]}


# In[34]:


s


# In[38]:


s={7,2,2,3,"we"}


# In[39]:


s


# In[40]:


s


# In[41]:


s.pop(2)


# In[42]:


s.pop


# In[43]:


s


# In[44]:


s.add(23)


# In[45]:


s


# In[46]:


s[1:3]


# In[47]:


d={}


# In[48]:


type(d)


# In[49]:


type(s)


# In[50]:


d={'name':"asim",'contact':"88650",'class':"m.tech"}


# In[51]:


d


# In[52]:


d1={1:'asim'}


# In[53]:


type(d1)


# In[56]:


d2={1we:"as"}


# In[57]:


d[1]


# In[58]:


d['name']


# In[63]:


d4 ={'name':'asim','mail_id':'asimmd',"name":['alam','aman','asif']}


# In[64]:


d4


# In[61]:


d4['name']


# In[65]:


d4['name']


# In[66]:


d4['name'][2]


# In[67]:


d4['mentor']=['saif','arif','areeb']


# In[68]:


d4


# In[69]:


del d4['name']


# In[70]:


d4


# In[74]:


list(d4.keys())


# In[75]:


d4.items()


# In[76]:


d4.pop('mentor')


# In[77]:


d4


# In[86]:


marks= int(input('enter your marks'))
if marks >= 80:
    print('you will be a part of A1 batch')
elif marks >=60 and marks <80:
    print('you will be in A2 batch')
elif marks >=40 and marks <60:
    print('you will be part of A3 batch')
else:
    print('you will be in A4 batch')


# In[87]:


marks


# In[88]:


l=[2,3,4,5,6,7]


# In[90]:


l1=int(l[])


# In[93]:


l1=[]


# In[96]:


l1.append(l[0]+1)


# In[97]:


l1


# In[98]:


for i in l:
    print (i)


# In[99]:


l


# In[103]:


for i in l:
    print (l[i]+1)
    i=i+1


# In[104]:


l=['sudh','kumar','shree']


# In[109]:


l1=[]
for i in l:
    print(i)
    l1.append(i.upper())


# In[110]:


l1


# In[111]:


l=[1,2,3,4,4,'sudh','kumar',324,234,23.23,'abc']


# In[115]:


l1=[]
l2=[]
for i in l:
    if type(i)==int or type(i)==float:
        l1.append(i)
    else :
        l2.append(i)


# In[116]:


l1


# In[117]:


l2


# In[118]:


def pass1():
    print('this is first program')


# In[119]:


pass1()


# In[120]:


def pass2():
    return 'this is new program'


# In[121]:


pass2()


# In[122]:


pass2()+"asim"


# In[123]:


pass1()+123


# In[124]:


def main():
    return('this is not good')


# In[125]:


main()


# In[126]:


main()+' asim'


# In[127]:


def test():
    return 'asim',42,23.21,[21,23,21]


# In[128]:


tset()


# In[129]:


test()


# In[130]:


a,b,c,d=test()


# In[131]:


a


# In[132]:


b


# In[133]:


c


# In[134]:


d


# In[135]:


a,b,c,d=test()


# In[136]:


def test1():
    a=2+3/4
    return a


# In[137]:


test1()


# In[138]:


def test2(a,b):
    d=a+b
    return d


# In[139]:


test2(3,4)


# In[140]:


def test3(a,b):
    return a+b


# In[141]:


test3('asim','alam')


# In[142]:


test3(2.'asim')


# In[172]:


l=[1,2,3,4,"asim","alam",[1,2,3,4,5,6]]


# In[177]:


def test8(a):
    """this is function for list sepaetion"""
    l1=[]
    for i in a:
        if type(i)==list:
            for j in i:
                l1.append(j)
        else:
            if type(i)==int:
                l1.append(i)
    return l1


# In[166]:


l1


# In[176]:


test8(l)


# In[173]:


l


# In[178]:


def test9(*args):
    return args


# In[179]:


test9(1,2,3,'asim','alam',[1,2,3,3])


# In[180]:


def test(**abc):
    return abc


# In[181]:


test(a=[1,2,3],b='asim')


# In[191]:


def test(n):
    a=0
    b=1
    for i in range(n):
        yield a
        a,b=b,a+b


# In[192]:


for i in test(10):
    print(i)


# In[193]:


l=[1,2,3,4,5]


# In[194]:


next(l)


# In[195]:


s1=iter(l)


# In[196]:


next(s1)


# In[197]:


next(s1)


# In[200]:


type(test)


# In[201]:


x=test(10)


# In[202]:


x


# In[ ]:




