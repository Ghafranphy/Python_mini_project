#############################################################################################################################################
#This repository contains my Python programming practice exercises as I develop and strengthen my programming skills.
#I am learning Python from the fundamentals through practical coding examples and exercises.
#============== #
#Topics Covered #
#============== #
#Python Fundamentals: Variables, data types, operators, and type conversion.
#Conditional Statements: if, elif, and else.
#Loops: for loops, while loops, and nested loops.
#Functions: Defining functions, parameters, arguments, return statements, and default arguments.
#Lists and Tuples: Indexing, slicing, updating, and manipulating collections.
#Dictionaries and Sets: Working with key-value pairs and unique elements.
#List Comprehensions: Creating lists using concise expressions.
#String Methods: String manipulation, formatting, and built-in methods.
#Python Built-in Methods and Functions: Practicing commonly used Python operations.
#Lambda Functions: Introduction to anonymous functions.
#Data Visualization: Creating mathematical plots using NumPy and Matplotlib.
#Objective
#To build a strong foundation in Python programming through consistent practice, problem-solving, and hands-on coding exercises,
#with the long-term goal of applying Python to scientific computing, data science, and machine learning. """

####################################################################################################################################################
print(len('hello world'))

print('ghafran@gmail.com')
print('''Hi\t"print" 
      
      Ghafran ''')

x=3
print(x+3)

x=input("what is your name:\t")
print("you are is",x)

print("Hello".upper())

a=10  # Int
b=3.15  # float
print(a,b)
print(None)

i=""  # string but notning
ii= "  "  # string but with empty space

print(len("Hello"))

text="hi"
number=10

print(text)
print(type(number))
print(len(text))
print(text.upper())
print(number.bit_length())


print((10).bit_length())




name="Ghafran"
print(type(name))

age=24
print("your age is:"+str(age))
name='Ghafran'
print(len(name))

passwors="Ghafgran@1234"
print(passwors.count('3'))

text=""" Ghafran here
jagellionian uni.
Krakow
"""
print(text.count('a'))

data='2022-29-90'
print(data.replace('-','/'))

price="12324,56"

print(price.replace(",","/"))

first_name="Ghafran"
last_name="Khan"
print(first_name+" "+last_name)

name="Sam"
age=34
is_student=True

print(f"My name is {name},my age is {age},{is_student}")

name="Ghfran"
print(name.split("r"))

stamp="2026-09-20 14:30"

print(stamp.replace(":","/").split(" "))

name="ghafran"
print(name[-1])
print(name[:-3])
print(name[0:4])

name="  Ghafran"
print(name.lstrip())
name ="Ghafran   "
print(name.rstrip())

name="Ghafran   Khan"
print(name.replace("   ",""))

name="GHAFRANKHAN"
print(name.lower())

data="2026-10-19"
print(data.startswith("2026"))
data2="ghafran Khan"

print(data2.endswith("Khan"))

data33="ghafran Khan"
print("an" in data33)
print(data33.find("K"))

data="345566"
print(data.isnumeric())

a=3+5j
print(type(a))

print(7 // 2)
print(8 % 2)

print(2 ** 3)

a=3
a+=3
print(a)

a=-3.15
print(round(-a))
import math
print(math.trunc(1.5))

print(math.sqrt(1.5))

import random
print(random.random())
print(random.randint(1,6))

a=20
print(isinstance(a,int))


a=20
if a >50 :
      print(a)
else:
      print("Unknown")


a=20
if a>20:
      print(a)
elif  a==20:
      print(10)
elif a<20:
      print("unknown")
else:
      print("no doing")

email=""
phone="123-345"
username=""
print(all([email,phone,username])) 

print(isinstance(123,int))           

a=2
print(2==int(2))

print(2>=20)
print("a">"b")

print(1<4>5)

a=20
a =10
print(a>20 or a>1)

print(not 3<2)

print(5==5 and (8>5 or 8==6))

email=["ghafran@yahoo.com","ghafran.khan@doctoral.uj.edu.pl"]
print("ghafran@yahoo.com" in email)

a=[1,1,3]
b=[1,1,3]
print(a is b)
a=5
b=5
print(a is b)


a=30

if a==10:
      print("Ture")
else:
      if a>10:
            print("True")
      
            

                  
score=50                  

print("A" if score>30 else "B" if score==90 else "F")


country ="United Sates"
if country== "United Sates":
       print("US")
else:
       print("Unknown")
   

email= "bara@ragmail@gamil.com"
email=email.strip()
if email =="":
      print("Email cannot b empty")
if not("." in email and "@" in email):
      print("Email must contain . and @")
if email.count("@") !=1:
      print("email must conatin at leat @")
if not email.endswith((".com",".org",".net")):
      print("email must conat .com")
if len(email) > 254:
      print("Email must not be longer then 254")
if not (email[0].isalnum() and email[-1].isalnum()):
      print("Email start with letter")
else:
      print("Email is valid :")            
      


for i in range(1,10,2):
      print(f"Round : {i}")   


files=['Report.CSV','Data.csv','final.text'] 

for file in files:
       file=file.strip().lower().replace('.text','csv')
       print(file) 
                  

                         
a=[1,2,3,4,5,6,7]

for aa in a:
      if aa==2:
            break
      print(aa)
                       
names=["Ghafran",'','Khan','Khattak','family']

for name in names:
      if name== "":
            continue
      print(name)
print("loop break")  


names=["Ghafran",'','Khan','Khattak','family']

for name in names:
      if name== "":
            pass
      print(name)
print("loop break") 

emails =['datagmail.com',
        'baraa@outlook.de',
        'Drop tables user;',
        'maria@gmail.com']     
                             
for email in emails:
      if ';' in email:
            print('Alert')
            break
else:             
 print(f"processing email: {email}")   
 

aa= [1,2,4,5,6,7,7
      ]                         
for a in aa:
      print(a)
      break
else:
      print("loop ended")  
      
aa=[1,2,3]
bb=[4,5,6]

for a in aa:
      for b in bb:
            print(f'Both number: {a,b}')  

tables=['customers','orders','products','pries']      

i=1
while i<4:
      print(i)  
      i+=1  

answer=""
while answer != "yes" :
      answer=input("write:") 
      if answer == "yes":
       break                                 

a =[10,20,30,30,40]
print(sum(a)) 
a=range(1,10)
print(list(a))

empty=list('python')
print(empty)

matrix=[[1,2,3],[5,6,7]]
print([[1,2,3],[5,6,7]])

matrix=[
      [1,2,3],
        [5,6,7],
        [8,9,10]
        ]
print(matrix[1])

lst=['a','b','c']
print(lst[:2])



matrix=[
      [1,2,3],
        [5,6,7],
        [8,9,10]
        ]
print(matrix[1][0:2])


personal=['Maria', 29,'Data Enginner','Spain']

name, age, role, country=personal
print(name)

personal=['Maria', 29,'Data Enginner','Spain']

name,*details,country=personal

print(name)
print(details)
print(country)

personal=['Maria', 29,'Data Enginner','Spain']

name,*_,=personal

print(name)

numbers=[10,45,56,500,200]

print(max(numbers))
print(sum(numbers))
print(len(numbers))
print(all(numbers))
print(any(numbers))

print(numbers.count(10))
print(numbers.index(500))
print(10 in numbers)

numbers=[1,2,3]
numbers.append(4)
numbers.insert(0,-1)
print(numbers)



matrix=[
      [1,2,3],
        [5,6,7],
        [8,9,10]
        ]
matrix.append([11,12,12])
matrix[1].insert(0,[11,22,33])
matrix.clear()
print(matrix)


leter=[1,2,3,4,5,6,7,8,9]
leter.remove(4)
removed=leter.pop(2)
print(removed)


matrix=[
      [1,2,3],
        [5,6,7],
        [8,9,10]
        ]
matrix[0][1]=4
print(matrix)
numbers=[4,2,5,1]
numbers.sort(reverse=True)
print(numbers)


matrix=[
      [1,2,3],
        [5,6,7],
        [8,9,10]
        ]
matrix[0].sort(reverse=True)
print(matrix)

numbers=['c','b','z']
new_number=sorted(numbers)
print(new_number)
numberss=[1,2,3,4,5,6,7]
rev=reversed(numberss)
print(list(rev))

numbers=[1,2,3,4,5]

numbers3=numbers.deepcopy()
print(numbers3==numbers)

import copy
matrix=[['a','b'],
        ['c','d']
        ]
matrix_copy=copy.deepcopy(matrix)
matrix_copy[0].append('dd')
print(matrix_copy)

matrix=[['a','b'],
        ['c','d']
        ]

print('a' is matrix[0][0])

letters=['a','b','c']
numbers=[1,2,3]
letters.extend(numbers)
print(letters)


letters=['a','b','c']
numbers=[1,2,3,4,5]
comb=list(zip(letters,numbers))
print(comb)

id=[101,102,103,104]
name=['Ghafran',"khan","salma","zeeshan"]
comb=list(zip(id,name))
print(comb)

letters=['a','b','c']
new_list=[]
for l in letters:
      new_list.append(l.upper())
      print(new_list)

letters=['a','b','c']
for  index,value in enumerate(letters):
      print(index,value)  


letters=['a','b','c']
numbers=[1,2,3]
for i in zip(letters,numbers):
      print(i)

letters=['a','b','c']
print(list(map(str.upper,letters)))
  
numbers=['1','2','3']
print(list(map(int,numbers)))


name=['maria','  jhon']

for n in map(str.strip,name):
      print(n)

comb=['a','','b',None,False] 
print(list(filter(bool,comb)))

items=['sql','123','python','42']
print(list(filter(str.isalpha,items)))
     
     
for i in filter(str.isalpha,items):
     print(i)      

multiply = lambda x: x*2     

print(multiply(2))

addition = lambda x, y: x+y

print(addition(2,3))
check =lambda i: i in "python"

print(check('y'))

prices=['$12.50','9.999','$100.00']

#print(list(map(lambda p: float(p.replace('$','')),prices)))

trans=map(lambda p: float(p.replace('$','')),prices)
print(list(trans))

price=[120,130,300,80]

print(list(filter(lambda p: p >=100,price)))

students=[['Maria',85],
          ['Kumar',90],
          ['Max',60]
          ]
print(list(filter(lambda row : row[1]>70,students)))

print(students[0][1]>70)



students=[['Maria',85],
          ['Kumar',90],
          ['Max',60]
          ]
print(list(filter(lambda row: row[0][:].startswith("M"),students)))

domains=['www.ggogle.com',
         'openai.com',
         'localhost',
         'WWW.DATAWITHBARAA.COM']

cleaned=[
      d.lower().replace('www.','')
      # Data tranformatio
      for d in domains
      if '.' in d
]

print(cleaned)

my_list=[10,20,30,40,10]
my_list[0]=30
print(my_list)

my_list=(10,20,30,10)

print(sorted(my_list))

my_set={1,2,4,6,7,7}
my_set.remove(4)
print(my_set)

a={10,30,30,45}

a.add(50)
a.update([1,2,3,4,5])
a |= {1,3}
print(a)

a={10,30,30,45}
a.discard(10)
print(a)

a={10,20,30,40}
b={30,40,50,60}
print(a.union(b))
print(a|b)


a={10,20,30,40}
b={30,40,50,60}
print(a.intersection(b))

print(a&b)

a={10,20,30,40}
b={30,40,50,60}
print(a.difference(b))
print(a-b)



a={10,20,30,40}
b={30,40,50,60}
print(a.symmetric_difference(b))
print(a^b)

a={10,20,30,40}
b={30,40,50,60}
print(a.issubset(b))
print(b.issubset(a))
print(b.isdisjoint(a))


my_dict={'a':10,
         'b':20,
         'c':30,
         'a':40
         }

print(my_dict['b'])
my_dict['c']=140
print(my_dict)

user={'id':1,'age':30,'city':"Berlin"}


print(user.get('name','Unknown'))
print('age' in user)

print(user.keys())
print(user.values())

user={'id':1,'age':30,'city':"Berlin"}
print(user.items())

user={'id':1,'age':30,'city':"Berlin"}
for u in user:
      print(u,user[u])
      
user={'id':1,'age':30,'city':"Berlin"}
for key, value in user.items():
      print(key,value)      

user={'id':1,'age':30,'city':"Berlin"}
user['name']='jhon'
user['age']=35
user.update({'age':40,'city':'paris'})
print(user)

user.pop('age','Not found')
print(user)

user={'id':1,'age':30,'city':"Berlin"}
user.popitem()
print(user)

user={'id':None,'age':None,'city':None
      }
user=dict.fromkeys(['id','age','city']
                  , 'unknown')
print(user)

row={ 'id':101,
     'name':'jhon',
     'country':'DE',
     'age':29,
     'status':'active'
      
}

user={'id':1,'name':'jhon','age':30,'city':'Berlin'}


user_str={
      k:v.upper()#Expression
      for k,v in user.items()  # Loop
      if isinstance(v,str)#Filter
}

print(user_str)





def addition(x,y):
      print(x+y)

addition(1,2)  

def fun():
      print('Hello')

fun()    

def quest(y):
      if y == 'Ghafran':
            print('True')
      else:
            print('False')
 
quest('Zeeshan')

import math 
print(math.floor(4.21)) 

name='  MariA '          
name.strip
print(name)

def names(first_name,last_name,country):
      first_name=first_name.strip().lower()
      last_name=last_name.strip().lower()
      full_name=first_name+' '+last_name
      print(full_name,country)
   
      
names("   GhafRAn","Khan",'Germany')     # positional argumement  
names(first_name="Ghafra,",last_name="Khan",country='Germnany')  # Keyword

names("Ghafran","Khan",'Germnany')  # Keyword


def names(first_name,last_name,country="n/a"):
      first_name=first_name.strip().lower()
      last_name=last_name.strip().lower()
      full_name=first_name+' '+last_name
      print(full_name,country)

names("Ghafran","Khan") 

# cal the total of values

def total(*args):
      print(sum(args))
total(1,2,3,4,5,6,7,8,9)  

def create_user(**kwargs):
      print(kwargs)

create_user(first_name="Mo",last_name="Salah",age=33,country="Egypt") 

def names(first_name):
       lo_name=first_name.strip().lower()
       up_cleaned = first_name.strip().upper()
       return lo_name, up_cleaned

lo_cleaned_name, up_names=names("   Ghafran")
print(up_names) 

def write_log(message):
      with open(r"C:\Users\Ghafran\Downloads\SQL\python_learning\app.log","a") as file:
            file.write(message + "\n")

#write_log("App Started")
write_log("User login")


def cleaned_and_split(email):
      cl_email = email.strip().lower()
      #sara@gmail.com
      username, domain = cl_email.split("@")
      return {"username:", username, 
              "domain", domain
              }
      
print(cleaned_and_split("  sara@gmail.com"))    


def is_valid_password(password):
      return len(password) >=8  
             
print(is_valid_password("123456"))  



def is_valid_email(email):
      return "@" in email and '.' in email            

print(is_valid_email("saragmail.com"))



aa=[1,2,3,4]
print(aa[2])

alphabates=['a','b','c']
print(alphabates)

mixed=['a',21,'cccc']
print(mixed)
number=list(range(1,9))
print(number)

matrix=[[1,2,3,4],
        [5,6,7,8,9]]  # nested list
print(matrix)

mixmatrix=[['a','b'],
        [5,6,7,8,9]]  # nested list
print(mixmatrix)

print(mixmatrix(0)[1:3])



mixmatrix=['a','b']  # nested list
print(mixmatrix[0:2])

matrix=[['a','b','c'],
        ['e','f','g'],
        ['h','i','j']
        ]

print(matrix[0:4])

print(matrix[2][0:2])


data1=["Maria",29,'Data enginer','Berlin']

name,age,role,country= data1
print(name)

data1=["Maria",29,'Data enginer','Berlin']


name,*details,country=data1
print(details)

name,*details=data1
print(*details)

data2=["Maria",29,'Data enginer','Berlin']

*data11,country=data2

print(data11)

data2=["Maria",29,'Data enginer','Berlin']

name,_,role,_=data2
print(name)

data33=[1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
name,*_,country=data33
print(name)


data44=[33,44,55,66]
print(33 in data44)

data44=["Ghafran"]
print("G" in data44[0])

data1=[4,5,6]
data2=[4,6,8]
print (data1 == data2)

data55=[2,3,4,5,6]
data55.append(5)
print(data55)
data66=[2,3,4,5,6]
data66.insert(0,4)
print(data66)

matrix=[['a','b','c'],
        ['d','e','f'],
        ['g','h','f']
        ]
matrix.append(['i','j','k'])
matrix.insert(0,['a','c'])
print(matrix)

matrix=[['a','b','c'],
        ['d','e','f'],
        ['g','h','f']
        ]
matrix[1].append('x')
matrix[2].insert(2,'x')
print(matrix)


aaa=['a','b','c','d']
aaa.remove('b')
print(aaa)

aaa=['aa','bb','cc','dd']
aaa1=aaa.pop(-1)
print(aaa1)


matrix=[['a','b','c'],
        ['d','e','f'],
        ['g','h','f']
        ]
matrix[0].pop(-1)
matrix[1].remove('f')
matrix[2].remove('f')
print(matrix)

data333=['a','b','c','d']

data333[3]='ee'
print(data333)


matrix=[['a','b','c'],
        ['d','e','f'],
        ['g','h','f']
        ]

matrix[1][1]=['ss','ff','jj']
print(matrix)

data3=['5','3','1','2']
data3.sort()
print(data3)

data3=['z','e','c','e']
data3.sort()
print(data3)

matrix=[['a','b','c'],
        ['z','x','y'],
        ['g','h','f']
        ]
matrix[2].sort()

print(matrix)


data3=['z','e','c','e']
data4=sorted(data3,reverse=True)
print(data4)

data33=['4','3','1','2']
data33.reverse()
data44=list(reversed(data33))
print(data44)

data44=[1,2,3,4,5]
data55=data44.copy()
data55.append(6)
print(data55,data44)


matrix=[['a','b','c'],
        ['z','x','y'],
        ['g','h','f']
        ]
matrix.remove(['z','x','y'])
import copy
matrix_copy=copy.deepcopy(matrix)
print(matrix)



matrix=[['a','b'],
        ['z','x'],
        ]
copy1=matrix
copy2=matrix.copy()
print(copy2[0] is matrix[0])


data=['a','b','c']
data1=[1,2,3]
combine=data1+data
combine1=data1*2
print(combine1)

data=['a','b','c']
data1=[1,2,3,4,5,6]

data1=zip(data,data1)
print(list(data1))

Ids=[101,102,103]
names=['Ali','Sara','Jhon']
combine=zip(Ids,names)
print(list(combine))

letters=['a','b','c']

for l in letters:
      print(l.upper())
      
letters=['a','b','c']
print(list(enumerate(letters,start=1)))      

for l,n in enumerate(letters,start=1):
      print(l,n)

letters=['a','b','e','c']
number=[1,2,3,4,5]

for l,n in zip(letters,number):
      print([l,n])
      
      
letters=['a','b','e','c']
print(list(map(str.upper,letters)))

number=['1','2','3']

print(list(map(int,number)))

names=['  maria','Jhon  ']

for n in map(str.strip,names):
      print(n)


data1=['a','10','b','c']
data2=list(filter(str.isalpha,data1))
print(data2)      
      
data1=['a','10','b','c']

for  f in filter(str.isalpha,data1):
      print(f)


multiply=lambda x: x*2

print(multiply(2))      

addition=lambda x,y: x^2*y^2

print(addition(2,3))

check=lambda h: h in 'python'

print(check('y'))

prices = ['$12.60','$9.99','$100.00'] 

print(list(map(lambda p: float(p.replace('$','')),prices)))

p='$12.50'
print(float(p.replace('$','')))





print(list(map(lambda p: float(p.replace('$','')),prices)))

prices=[123,123,156,80]

print(list(filter(lambda p: p>=100,prices)))


students=[['Maria', 85],
          ['Kumar',90],
          ['Max',90]
          ]

print(list(filter(lambda row: row[1] > 70,students)))

print(list(filter(lambda row: row[0].startswith('M'),students)))



domain=['wwww.google.com',
        'openai.com',
        'WWW.DATAWITHBARAA.COM'
        ]

cleaned = [ 
            d.lower().replace('WWW.','')    # Data transformatio
           for d in domain         # For Loop
           if '.' in d             # Data Filtering 
]

print(cleaned)

my_list=[10,30,20,10]
print(my_list)

tuple=(1,2,3,4,5,6,6,6)

print(sorted(tuple))

set={10,30,20,10}
set.remove(20)
print(set)

a={10,20,30,40}
a.add(50)
a.update([70,80])
a|={-1,-2}
print(a)

a={10,20,30,40}
a.remove(20)
a.discard(10)
print(a)



a={10,20,30,40}
b={30,70,50,60}

print(a.union(b))
print(a|b)

print(a.intersection(b))
print(a & b)

print(a.difference(b))
print(a-b)

a={10,20,30,40}
b={30,70,50,60}

print(a.symmetric_difference(b))
print(a^b)

a={10,20,30,40}
b={30,70,50,60}
print(a.issubset(b))
print(b.issuperset(a))
print(a.isdisjoint(b))

dictiont={"Ghafran":33,
          "Kumar":30,
          "Khan":20,
          "Khan":20
          }

print(dictiont["Kumar"])
dictiont["Kumar"]=90
print(dictiont)

user={"id":1, "age":30,"city":"berlin"}

print(user.get("age","Unknown"))
print('age' not in user)

user={"id":1, "age":30,"city":"berlin"}
print(user.keys())
print(user.values())
print(user.items())
print(user)

user={"id":1, "age":30,"city":"berlin"}

for  u,v in user.items():
      print(u,v)
      
user={"id":1, "age":30,"city":"berlin"}
user["id"]=3
user.update({'age':40,'city':'Paris'})
user.pop("city","Not found")
user.popitem()
print(user) 


user={"id":None,
      "name":None,
      "age":None,
      "city":None}

user=dict.fromkeys(["id","name","age","city"],None)     
print(user)

user={"id":1,"name":"Jhon","age":30,"city":"Berlin"}

user_string={
      k:v.upper() # Expressions
      for k,v in user.items() # Loop
      if isinstance(v,str)#Filter
}

print(user_string)


def Ghafran(x):
      if isinstance(x,str):
       return   print("True")
      
Ghafran('G')

def hi(x):
      print(x)
      
hi('Ghafran')
import math
print(math.ceil(4.2))

def cleaned(first_name,last_name,country="Pakistan"):
      clc_first_named=first_name.strip().lower()
      clc_last_named=last_name.strip().lower()
      print(clc_first_named+' '+clc_last_named+' '+"From"+' '+country)
      

cleaned(last_name="Khan",first_name=" GHAFRAN") 

#clc the total of multiple of value

def total(*args):
      print(sum(args))

total(1,2,3,4,5,6,7,8,9)      


def create_user(**kwargs):
      return kwargs

user=create_user(first_name="Ghafran",
            last_name="Khan",
            age=33,
            country="egypt")      

print(user)

  


def clean_name(first_name,last_name):
      cleaned=first_name.strip().lower()
      cleaned_2=last_name.strip().lower()
      return cleaned,cleaned_2 

first_clc,last_name=clean_name("    GHAFRAN","     KHAN")
print(first_clc,last_name) 


def write_log(message):
      with open(r"C:\Users\Ghafran\Downloads\SQL\python_learning\app.log", "a") as file:
            file.write(message+ "\n") 
            
write_log("App Started") 


def cleaned_and_split_email(email):
      cl_email = email.strip().lower()
      #sara@gmail.com
      username, domain =cl_email.split("@")
      return {username,domain}

clc_email2=cleaned_and_split_email("sara@gmail.com")           
print(clc_email2)


def check_password(password):
      valid_email=len(password) >=8
      return valid_email

pass2=check_password('12345678')
print(pass2)



def  is_valid_email(email):
      return "@" in email and "." in email

correct=is_valid_email('SARARA')
print(correct)


email= input("Please enter your email")
def process_user_email(email):
 write_log('App Started')

 is_valid_email(email)
 if not is_valid_email(email):
       write_log(f'invalid email recieve:{email}')
 else:
      clc33=cleaned_and_split_email(email)
      write_log(f'processed email: {clc33}')
 write_log("App Stopped") 
 

      
      
email= input("Please enter your email: ")
process_user_email(email)


for i,k in enumerate(range(1,9,2)):
      print(f'Round : {i},sequence : {k}')

for i in "Ghafran":
      print(i)

scores=[80,50,60,75] 
total=0
for score in scores:
      total+=score
print(f'Total score : {total}')  

files=['Report.csv','DATA.csv','final.TXT']

for file in files:
      file=file.strip().lower().replace('.txt','.csv')
      print(f'Processions : {file}')   

scores=[30,40,60,89,30]

for score in scores:
      print(score)
      if score>=70:
        break

names= ['jhon','maria','','kumar']

for name in names:
      if name == '':
            print('Empty value detected')
            continue
      print(name)  
  
days=['Mon','Sun','Wed','Tue']

for day in days:
      if day in ['Sat', 'Sun']:
            continue
      print(F'Working : {day}')
      
emails = [
      'data@gmail.com',
      'baraa@outlook.de',
      'DROP TABLE USER;'
      'maria@gamil.com'
]      

for email in emails:
      if ";" in email:
            print(f'SQL injection : Hacker Attack')
            break
      print(f'processing Email : {email}')
else:
      print('Stopped')

        
for i in (1,2,3):
      if i==2:
       break
      print(i)
else:
      print('end') 
      
names= ['Kamara', 'Tuba',None,'Mounika']

for name in names:
      if name is None:
            print("Found a missing name")
            break
else:
      print('All names are avaiable')    
      

files=['data1.csv',
       'report.pdf',
       'data2.txt'
       'report2.csv']

for file in files:
      if file.endswith('.csv'):
            print(f'{file} is not CSV')
            continue
else:
      print('All files are csv')       
      
for i in (1,2,3):
      for j in (4,5,6):
            print(i,j) 
        
years=[2026,2027]
months=['Jan','Feb']
days=range(1,29)

for year in years:
      for month in months:
            for d in days:
                  print(f"report_{year}_{month}_{d}") 
                  
 
 
i=1
while i<4:
   print(i)
   i+=1 
                                  
answer=''
while  answer != 'yes':
      answer=input('do you agree') 
print('Thank you')   

while True:
      answer= input('do you agree') 
      if answer== "yes":
            break                  
print('Thnak you')  

attempts=0
while attempts <3:
      answer= input("Do you agree ? (yes/no)")
      if answer =='yes':
            print("Glad we are on the same page")
            break
      attempts+=1
else:
      print("Thank you") 
      

list=[1,2,3,4,5]
list[3]=20
list.insert(1,9)
print(list)  

name=['Ghafran','Khan','Ayesha','Mustajab','Nadeem',23]
name.append("KKKhan")
name.insert(0,"KKKhan")
print(name)

numbers=list(range(1,20))
print(numbers)

numbers2=[[1,2,3,4],
          [34,67,89,0]]
numbers2.append([34,56,78])
numbers2.insert(0,[22,222,222,222])
print(numbers2)
         

numbers2=[[1,2,3,4],
          [34,67,89,0]]
print(numbers2[0][2:4])


numbers2=[1,2,33,4]
numbers2.sort()
print(max(numbers2))         
               
name=['Ghafran','Khan','Ayesha','Mustajab','Nadeem',23]

names,_,_,_,_,_=name    
print(names)           

numbers2=[1,2,33,'Ghafran','True']
print(any(numbers2))

print(all(['a','',23]))

name=['Ghafran','Khan','Ayesha','Mustajab','Nadeem',23]
names2=name.count('Ghafran')
print('Ghafran' in name)

name=['Ghafran','Khan','Ayesha','Mustajab','Nadeem',23]
name.remove('Ghafran')
name.pop(-1)
print(name)

numbers2=[[1,2,3,4],
          [34,67,89,0]]
numbers2[0].remove(3)
print(numbers2)


numbers2=[[1,2,3,4],
          [34,67,89,0]]
numbers2[1][2]=[2,3,4,5,6]
print(numbers2)


numbers2=[[1,2,3,4],
          [34,67,89,0]]
numbers2[1].sort()
print(numbers2)

stringsss=['Ghafran','Ali','Jackel']
stringsss.reverse()
print(stringsss)
import copy
stringsss=['Ghafran','Ali','Jackel']
str2=copy.deepcopy(stringsss)
print(str2)
import copy
numbers2=[[1,2,3,4],
          [34,67,89,0]]
numb33=copy.deepcopy(numbers2)
print(numb33)

list1=[1,2,3,4]
list2=[1,2]
combine=list1+list2
combine.extend([2,3,4,5,6])
combine44=list(zip(list1,list2))
print(combine44)


letters=['a','b','c']
new_list=[0]*len(letters)

for l,m in enumerate(reversed(letters)):
      new_list[l] =m.upper()
print(new_list)      

list1=['a','b','c']
print(list(map(str.upper,list1)))

list1=['a','b','c','']
print(list(filter(str.isalpha,list1)))

text = lambda price: price*12
print(text(12))

check= lambda text: print(text) if text =="True" else None
      
list1=['a','b','c','']



p='$12.50'

print(float(p.replace('$','')))

price=["$12.50","$9.99","$100"]

print(list(map(lambda p: float(p.replace('$','')),price)))


prices=[122,130,300,80]

print(list(filter(lambda p: p>100,prices)))


domain=['www.google.com',
        'openai.com',
        'localhost',
        'WWW.DATAWITHBARA.COM']
cleande=[
      d.lower().replace('www','')
       for d in domain
      if '.' in d 
      
]
print(cleande)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits if "a" in x]

print(newlist)

numbers=[1,2,3,4,9,10]

new_number=[num*2 if num<8 else None for num in numbers ]
print(new_number)

word = "Python"
vowels = "aeiou"

# find vowel in the string "Python"
result = [char for char in word if char in vowels]

print(result)

tuple=(10,2,3,4,5,5)

print(sorted(tuple))

sets={1,2,3,4,6,5}
sets.add(7)
sets.update({"HIIII"})
sets|={3333}
sets.discard(3)
print(sets)

sets={1,2,3,4,6,5}
sets1={3,4,5,6,7,8,9,0}
print(sets.union(sets1))


sets={1,2,3,4,6,5}
sets1={3,4,5,6,7,8,9,0}
print(sets.intersection(sets1))


sets={1,2,3,4,6,5}
sets1={3,4,5,6,7,8,9,0}
print(sets.difference(sets1))


sets={1,2,3,4,6,5}
sets1={3,4,5,6,7,8,9,0}
print(sets.symmetric_difference(sets1))


sets={1,2,3,4,6,5}
sets1={3,4,5,6,7,8,9,0}
print(sets.issubset(sets1))


sets={1,2,3,4,6,5}
sets1={3,4,5,6,7,8,9,0}
print(sets1.issuperset(sets))



sets={1,2,3,4,6,5}
sets1={3,4,5,6,7,8,9,0}

print(sets.isdisjoint(sets1))

dic={"Ghafran":10,"Khan":30,"Salma":40,'Ghafran1':10}

print(dic.get("Salma",'unknown'))


dic={"Ghafran":10,"Khan":30,"Salma":40,'Ghafran1':10}

print( 'Khan' in dic)

dic={"Ghafran":10,"Khan":30,"Salma":40,'Ghafran1':10}

print(dic.values())
print(dic.items())

dic={"Ghafran":10,"Khan":30,"Salma":40,'Ghafran1':10}

for d,e in dic.items():
      print(d,e)

dic={"Ghafran":10,"Khan":30,"Salma":40,'Ghafran1':10}

dic["Khan23"]="Mustjab"
dic.update({"mm":45,"ff":65})
dic.pop('ff')
print(dic)

dic={"Ghafran":10,"Khan":30,"Salma":40,'Ghafran1':10}

dic1=dict.fromkeys(['dd','ee'],None)
print(dic1)

user={"id":1,"name":"Jhon","age":30,"city":"Berlin"}


user1={
      u:v.upper()
      for u,v in user.items()
            if isinstance(v,str)
} 

print(user1)


a=[10,11,12,45,56]
aa=[]
for i in a:
      if i > 10:
            aa.append(i)
      else:
            print("Outof range")
print(aa)  

aa=[10,11,12,45,56]

for a in aa:
 if a==10:
      print("fair")
 elif a==11:
      print("Nice")
 elif a ==12:
      print("very Good")
 elif a==20:
      print('Very Good')
 else:
       print("Fail")
                  
