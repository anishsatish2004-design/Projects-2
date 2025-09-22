#!/usr/bin/env python
# coding: utf-8

# In[1]:


3+3


# In[2]:


a=10+3j
print(type(a))


# In[3]:


mystring="hello"
print(mystring)


# In[4]:


mysting="Hi How are you?"
mystring[0]


# In[6]:


mystring="Hi How are you?"
mystring.split(" ")[3]


# In[8]:


mystring="Hi/How/are/you?"
mystring.split("/")[2]


# In[9]:


mystring="Hi|How|are|you?"
mystring.split("|")[1]


# In[13]:


a=[254,547,5412,56]
a[:3]


# In[14]:


a=[254,547,5412,56]
a[0:2]


# In[15]:


a=[254,547,5412,56]
a[:-1]


# In[19]:


a=[254,547,5412,56]
a[::-1]


# In[20]:


x=[1,2,3]
z=x*221
print(z)


# In[1]:


teams={'Name':['sheldon','leonard','penny'],
      'age':[30,31,25],
       'course':['FBA','CMA','ACCA']
      }
teams.values()


# In[4]:


import pandas as pd
dt = {'ID': [11, 12, 13, 14, 15],
     'first name': ['David', 'Jamie', 'Stevart', 'John', 'Steve'],
     'company': ['Aron','TCS','Google','RBS', '.'],
     'salary': [74, 76, 96, 71, 78]}
mydt = pd.DataFrame(dt)
print(mydt)


# In[2]:


import pandas as pd
dt = {'REG NO': [100, 99, 86],
     'name': ['Adi', 'Adii', 'Adiii'],
     'age': [18, 18, 19],
     'course': ['Bcom', 'Bcom', 'Bcom'],
     'marks': [45, 48, 30]}
mydt = pd.DataFrame(dt)
print(mydt)


# In[13]:


import pandas as pd
dt={'regisno':[1,2,3],
    'Name':['sheldon','leonard','penny'],
      'age':[30,31,25],
       'course':['FBA','CMA','ACCA'],
    'marks':[100,90,80]
      }
mydt=pd.DataFrame(dt)
print(mydt)


# In[6]:


import pandas as pd
grades = pd.read_csv("C:\\Users\\anish\\Downloads\\grades.csv")
pd.DataFrame(grades)


# In[8]:


len(grades.final)


# In[9]:


grades.firstname.unique().shape


# In[7]:


grades['quiz1'].dtype


# In[13]:


grades.ethnicity.value_counts()


# In[14]:


grades.final.min()


# In[15]:


grades.final.max()


# In[16]:


grades.final.sum()


# In[17]:


grades.final.skew()


# In[18]:


grades.final.kurtosis()


# In[20]:


grades.sample(5)


# In[21]:


import matplotlib.pyplot as plt
plt.hist(grades.total, bins = 'auto')


# In[22]:


import matplotlib.pyplot as plt
plt.boxplot(grades.total)


# In[23]:


plt.boxplot(grades.total,0, 'rs', 0)


# In[2]:





# In[15]:


j=grades.sample(20)
print(j.head(3))
j.to_csv('C://Users//anish//OneDrive//Desktop//j.csv')


# In[1]:


#(1)
words = []
string_1 = "Hello World"
#(A)
print(string_1[0])
#(B)
print(string_1[-1])
#(C)
words = string_1.split()
print (words [0])


# In[7]:


#(2)
A = [1, 2, 3, 4]
B = [2, 4, 6, 8]
#(A)
list_1 = A + B
print(list_1)
#(B)
print(A[::-1])
#(C)
for i in B:
    if(i == 8):
        B.remove(8)
        B.append(10)
        print(B)


# In[1]:


#(3)
#(A)
num_1 = 4
num_2 = 6
print("The Maximum number is", max(num_1, num_2))
#(B)
matrix_1 = [[1, 2, 3],[5, 6, 7]]
matrix_2 = [[5, 6, 7],[8, 4, 9]]
matrix_add = [[0, 0, 0],[0, 0, 0]]
matrix_sub = [[0, 0, 0],[0, 0, 0]]
#(i)
for i in range(0, len (matrix_1)):
    for j in range(0, len (matrix_1[0])):
        matrix_add[i][j] = matrix_1[i][j] + matrix_2[i][j]
        
print("The addition of the matrices is : ", matrix_add)
#(ii)
for i in range(0, len (matrix_1)):
    for j in range(0, len (matrix_1[0])):
            matrix_sub[i][j] = matrix_1[i][j] - matrix_2[i][j]
            
print("The subtraction of the matrices is : ", matrix_sub)
        
        
    


# In[1]:


#(4)
import pandas as pd
dict_1 = {"Name" : ["Vinay", "Kushal", "Aman", "Gill", "Della", "Jim"],
         "Age" : [22, 25, 24, 25, 22, 28],
         "Occupation" : ["Engineer", "Doctor", "Accountant", "Lab Tech", "Tech Support", "Teacher"],
         "Salary" : [35000, 30000, 25000, 20000, 28000, 38000]}
database = pd.DataFrame(dict_1)
#(A)
print(database.head(5))
#(B)
print(database.tail(5))
#(C)
print(database.describe())
#(D)
print(type(database))
#(E)
print(database.shape)
#(F)
print(database.Salary.max())
#(G)
print(database.Salary.sum())
#(H)
for i in database.Salary:
    if(i <= 30000):
        print(i)
        
#(I)
dict_2 = {'Names' : dict_1['Name'], 'Salary' : dict_1['Salary']}



# In[2]:


#(5)
import matplotlib.pyplot as plt
import pandas as pd

cs2m = pd.read_csv('C:\\Users\\anish\\Downloads\\cs2m.csv')
pd.DataFrame(cs2m)


plt.hist(cs2m. BP)
plt.xlabel('BP')
plt.ylabel('Count')
plt.title('Histogram')


# In[3]:


#(6)
import matplotlib.pyplot as plt 
import pandas as pd
cs2m = pd.read_csv('C:\\Users\\anish\\Downloads\\cs2m.csv')
pd.DataFrame(cs2m)
plt.boxplot(cs2m.BP)
plt.xlabel('Count')
plt.ylabel('BP')
plt.title('Boxplot')


# In[4]:


#(7)
import matplotlib.pyplot as plt
import pandas as pd 
cs2m = pd.read_csv('C:\\Users\\anish\\Downloads\\cs2m.csv')
plt.scatter(cs2m.Age, cs2m.BP, color = "red")
plt.xlabel('Age')
plt.ylabel('BP')
plt.title('Scatterplot')


# In[5]:


#(8)
desktop_file = cs2m.sample(20)
print(desktop_file.head(3))
desktop_file.to_csv('C:\\Users\\anish\\Downloads\\.csv')


# In[1]:


mystring="I want Pizza"
print(mystring)


# In[5]:


mystring="I want pizza"


# In[3]:


mystring="Hello World"
mystring[0]


# In[4]:


mystring="Hello World"
mystring[10]


# In[5]:


mystring="Hello World"
mystring.split(" ")[0]


# In[6]:


A = [1,2,3,4]
B = [2,4,6,8]

list = A + B
print(list)


# In[7]:


A = [1,2,3,4]
A[::-1]


# In[8]:


num1 = 4
num2 = 6

print("The maximum number is", max(num1, num2))


# In[10]:


import pandas as pd
list1 = {"Name" : ["Annie", "Aaraa", "Anie", "Aara", "Aarannie"],
         "Age" : [18, 19, 20, 21, 22],
         "Occupation" : ["Accountant", "Doctor", "ABC", "CBA", "Teacher"],
         "Salary" : [35000, 26000, 40000, 50000, 60000]}
database = pd.DataFrame(list1)

print(database.head(5))
print(database.tail(5))
print(database.describe())
print(type(database))
print(database.shape)
print(database.Salary.max())
print(database.Salary.sum())

for i in database.Salary:
    if(i <= 30000):
        print(i)
        
list1 = {'Names' : list1['Name'], 'Salary' : list1['Salary']}


# In[15]:


desktop_file = cs2m.sample(20)
print(desktop_file.head(3))
desktop_file.to_csv('C:\Users\anish\Downloads\desktop_file.csv')


# In[ ]:




