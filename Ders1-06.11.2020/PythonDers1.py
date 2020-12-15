#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Merhaba Dünya") # String bir ifadeyi tırnak işareti arasına alarak ekranda çıktıyı alıyorum.


# In[3]:


print(5) #integer sayı değerini ekrana bas
print(5.5) #float sayı değerini ekrana bas


# In[1]:


type(5) #hangi veri tipinde olduğunu öğrenmek için type() fonksiyonu kullandım
        # int ----> integer(tam sayı)


# In[5]:


type(2.5)   #float---->ondalık sayı


# In[6]:


print(5+5)
print(5-2)
print(5*2)
print(10/2)


# In[7]:


print(5/2)
print(5//2)


# In[8]:


x=5%2  #Kalan hesabı için
print(x)


# In[9]:


first=10
second=20
print(first+second)


# In[10]:


first="10"
second="20"
print(first+second)  #Ekrana 30 değerini basmadı çünkü (string) olarak tanımladık.


# In[11]:


a=3
b=2
print(a*b)


# In[12]:


a="3"
print(a*3)


# In[13]:


a=123
a=a+1
print(a)


# In[14]:


a="123"
a=a+1
print(a)  #Sayıya bir ekleyemedik çünkü a değişkeni string olarak tanımlandı.


# In[15]:


print(int("3")*3)


# In[16]:


name=input("Enter your name:")  #input ile kullanıcıdan veri aldık.
print(name)


# In[18]:


number=input("Enter a number:")
print(number*5)


# In[19]:


number=int(input("Enter a number:")) #Kullanıcıdan sayı değişkenini alırken int tipinde olduğunu gösterdik.
print(number*5)


# In[21]:


print("Merhaba\nDünya") #\n alt satıra geçmemizi sağladı


# In[22]:


a=5
b=2
print("{} - {} nin sonucu: {}".format(a,b,a-b))


# In[23]:


print(2**2)  # ** ile üs ifadesini belirttik.


# In[24]:


print(5**2)


# In[25]:


print(25**0.5)


# In[28]:


#EXAMPLE 1

x=float(input("enter a number:"))
y=float(input("enter a number:"))
z=float(input("enter a number:"))
average=((x+y+z)/3)
result=((x*y*z)**0.5)
print(average)
print(result)


# In[31]:


#EXAMPLE 2

r=int(input("enter a r:"))
pi = 3.1415926
area=pi*r*r
print(area)


# In[32]:


#EXAMPLE 3

hour=int(input("Enter a hours: "))
minute=int(input("enter a minute: "))
second=int(input("enter a second: "))
result=(hour*3600+minute*60+second)
print(result)


# In[2]:


#EXAMPLE 4

F=float(input("Enter a F:"))
celcius=((F-32)/(1.8))
print(celcius)


# In[ ]:




