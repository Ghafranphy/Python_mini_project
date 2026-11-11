print("Hi this is my \"first python code\" ")
print('Hi "python" ')
print("C:\\user")
print("newline \n")
print('t \t tt')

print('''ghfr
      ghh''')

x = "my is bara"

print(x)


input("Enter your name:")

imputvale = input("what is your name:")
country= input("Which country you belong")
print('you name is:' ,imputvale + 'and my country is:' ,country)






text='hi'
number=10

print(len(text))

print(text.upper())           ## method
print(number.bit_length())    ## method



name ="Bara"

print(type(name))


age=24
print(type(age))

print("ypur age is :" + str(age))


passwaord="123a"

print(len(passwaord))

if len(passwaord) <8:
      print("ypur password is too short")
      
        
text="""
python is easy to learn.
python is poweful.
many people love python.          
        """ ## python is very case sensitive 
print( text.count("python"))          




price="123/56"
print(price.replace("/",","))

pricew="$123,345.56"
print(pricew.replace("$","").replace(",",""))      


first_name= "Michael"
last_name= "Scot"

last_name= first_name+" "+last_name
print(last_name)

name= "sam"
age= 34
is_student = False

print(f"{{name {age} {is_student}}}")


text= "ghafran/is/bad/boy"

print(text.split("/"))


csv="1234-MAx"
print(csv.split("-"))




print("ha"*3)
print("=" * 30)

text= "python"

# Extract the first one

print(text[0])
print(text[5])

# extract

print(text[3])


data="2026-09-20"
print(data[0:4])
print(data[:4])
# Extract the Month
print(data[5:7])


# Extract the day

print(data[8:])
print(data[-2:])

dta2="  dat"
print(dta2.strip())


data33="%%%% data %%%".strip("%").lstrip()
print(data33)

data3="PYYYython".upper()
print(data3)


phone="+49-176-12345"
print(phone.startswith("+49"))

email="bara@gamil.com"

print(email.endswith("gamil.com"))


file="data-backup.csv"

print(file.endswith(".csv"))
print("@" in email)

url="hrrps:/api.company"
print("/api" in url)


phone=  "+48-176-12345"
phone2="+48-654-16548"

print(phone[phone.find("-")+1:])



country = "USA"

print(country.isalpha())


phone ='01234'
print(phone.isnumeric())



phone ='01.234'
print(phone.isnumeric())


phone=3

print(type(float(phone)))


x=3
y=4


print(7 // 2)   # floor division

print(7 % 2)    # reminder

print(7**2)


xx=3
xx+=3
print(xx)


x=4

x*=2

print(x)


print(round(2.14))
  
import math

print(math.trunc(2.6667))

print(int(2.456))

import math, random
print(random.random())
print(random.randint(1,6))

x=7.1

print(x.is_integer())

x=70

print(isinstance(x,int))


print(True)
print(False)

print(type(True))

print(bool())

print(bool("Hi"))

print(bool(0))

print(bool(None))



email= ""
phone= "0334908181"
username=  ""
# Allows registration
# if any field is filled

print(any([email, phone, username]))

# becuase phone is integers

email= ""
phone= ""
username=  ""
# Allows registration
# if any field is filled

print(any([email, phone, username]))



email= "gjkka"
phone= "017"
username=  "ghafra"
# Allows registration
# if any field is filled

print(all([email, phone, username]))


print(isinstance(123,int))

print(isinstance(True,bool))


print("4589".endswith("9"))



print("4589".startswith("4"))

print(10!=10)

print(7>3)
print("a" < "b")


print(1<4>6)

age=20

print(18 < age <=230)

x=5
print(x>1 or x>24) 


cpu_usage= 70
memrory_usage=90

print(not cpu_usage> 90 or not memrory_usage>700)

print(not 3>2)


print(not 0)


cpu_usage= 70
memrory_usage=90

print( cpu_usage> 90 and (memrory_usage>700 or memrory_usage>900) )

# Allow acces only if the user in logged in
# or they are guest
# but they must not banned.


is_lggged_in= True
guest= False
banned= True


print((is_lggged_in or guest)  and  not banned)


print('Ghafran'  in ["Ghafran","Khan"])


domain= 'gmail.com'
baned_domain= ["spam.com","fake.orge"]

print(domain not in baned_domain)




a=[1,2,3]
b=[1,2,3]
print(a is b)

x=['a','b','c']
y=['a','b','c']

print(x is y)

x="a"
y="b"
print(x is y)


x=['a','b','c']
y=x
print(x is y)


email= None
print(email !="")



score =100
if score == -200:
      print("Good job"),
elif score <= 0:
      print("Nothing")
elif score<=0:
      print("Nothing")
else:
      print("Nothing")

      
score=300
if score ==400:
      print("nothing")
else: 
      if score ==300:
            print("score")
      else:
            print("Nothing")
            
            
score=400;
submitted_asig=True;
            
if score ==400:
      if submitted_asig:
            print("pass")
      else:
            print("nothing")
            
score=400;
submitted_asig=True;

if score ==0 and submitted_asig:
      print("pass")
else:
      print("fail")                

score = 50
submitted_asig=True;

if score >= 90:
      print("Pass")
else:
      print("Fail")

if  submitted_asig:
      print("Project submitted")
else:
      print("Project is not submitted")
      
score=100      
grade="pass" if score>=100 else "f"
print(grade)  
            
country= "Egypt"

match country:
      case "United stes" | "USA":
            print("US")
      case "India":
            print("IN")
      case "Egypt":
            print("EG")
      case _:
            print("Unknown country")
                  
email= "bara@gm@ail.com"
valid= True
email=email.strip()
if email=="":
      print("Email cannot be empty")
      valid= False
if not ( "," in email and "@" in email):
      print("Email must contain . and @")
      valid= False
if email.count("@") !=1:
      print("email must contain exactly one @.")
      valid= False
if not email.endswith((".com","org",".net")):
      print (" Email must end with .com, .org , or .net")
      valid= False
if len(email) > 254:
      print("Email must not be longer than 254 characters")
      valid= False
if not (email[0].isalnum() and email[-1].isalnum()):
      print("Email must start and end with a letter or digit")
      valid= False
if valid:
      print("Email is valid")   
                  
for i in range(1,10):
      print(i)


for round in range(1,6):
      print("Round:",round)

for check in [1,2,3,4,5]:
      print(check)
for i in " python":
      print(i)
import numpy as np
for p in np.arange(1,5,0.5):
      print(p)
      
scores= [80,50,60,75]
total=0

for score in scores:
      total+=score
      print(total)
print(total)      


files=[" report.csv ", "Data.csv ","final.TXT "]

for  file in files:
      file=file.strip().lower().replace(".txt",".csv")  # dont write in capital because we lower the case 
      print(file)

for i in (1,2,3,4,5):
   if i <= 3:
         break
   print(i)
   
   
names = ["khan", "jhons","maria","","cccc","dddd"]

for name in names:
      if name == "":
           break  # break must inside the if statement other break for from the start
      print(name)   

   
names = ["khan", "jhons","maria","","cccc","dddd"]

for name in names:
      if name == "":
            print("Empty value is detected")
            continue  
      print(name)           
      
names = ["khan", "jhons","maria","","cccc","dddd"]      
for name in names:
      if name == "":
            #print("Empty value is detected")
            pass #todo: Handle Empty value
            name=name.replace("","unknown")
      print(name) 
      
      
days=["Mon","Sun","Wed","Tue"]

for day in days:
      if day in ["Sat", "Sun"]:
       continue
      print(F"Workday: {day}")      
      
emails=['data@gamil.com','bara@outloos=k.de','Drop table user;','maria@gamil.com']      


emails=['data@gamil.com','bara@outloos=k.de','Drop table user;','maria@gamil.com']      


for email in emails:
      if ';' not in email:
            print(email) 
      else:
            print("hacker attack") 
            break  #Exit of  loop once it executed
else:
      print("loops ended")

names = ['kamra','Tuba', None, 'Mounkia']
        
for name in names:
      if name is None:
            print("Found a missing name")
            break
else:
      print("All names are avliable")
      
files= ['data.csv','data2.csv','data3.csv','pdf']

for file in files:
      if not file.endswith(".csv"):
       print(file," is not a csv")
       break
else:
      print("All files are CSV")

for x in range(3):  # outer loop
      for y in range(2):  # inner loop
            print(f"({x},{y})") 
            
colors=['red','green','blue']
size = ['L', 'M','S']

for color in colors:
      for siz in size:
            print(f"({color},{siz})")

years=[2026,2027]
months= ['Jan','Feb']
days = range(1,29)

for year in years:
      for month in months:
            for day in days:
                  print(f"report_({year}_{month}_{day})")
                  
tables = ['customers','orders','products','prices']
columns=['id','create_date']

for table in tables:
      for col in columns:
            print(f"select count(*) from {table} where {col} is Null;")
            
            
i=1   # initalization
while i<=4:   # condition
      print(i)
      i+=1   # update mechanism
      
      
answer=""

while answer != "yes":
      answer= input("Do you agree?(yes/no): ")
print("Thank you")            

while True:
      answer = input("Do you agree?(yes/no): ") 
      if answer == "yes":
            break          
print("Tank you")      



# 3 attempts
# yes within three attempts -> "Glad we are on the same page"
# Otherwise "3 strikes. You are out"
attempts=0
while attempts < 3:
      answer = input("Do you agree? (yes/no): ")
      if answer == "yes":
            print("Glad we are on the same page")
            break
      attempts +=1
else:      
    print("Thank you")      

# Create Lists
empty=[]

print(empty)

print(type(empty))

letter=['a','b','c']
print(letter)


number=[1,2,3]
print(number)

mixlist=[1,2,3,"True",None,"a"]
print(mixlist)


empty=list()
print(empty)

letter=list('python')   # python create list
print(letter)

numbers=list(range(5))
print(list(numbers))




matrix=[['a','b','c'],['d','e','f']]
print(matrix)
print(type(matrix))

mixedmatrix=[['a','b','c'],[1,2,3,4],[True]]   # python is flexible with dimensions
print(mixedmatrix)


# Acces $ Read

lst=['a','b','c','d']
print(f'{lst[-1]} {lst[-2]}')


matrix=[
      ['a','b','c'], # Row1
      ['d','e','f'], # Row2
      ['g','h','i'] # Row3
]

print(matrix[1:])
print(matrix[2][:2])


person=['Maria',29,'Data Engineer', 'Spain']

#name=person[0]
#age=person[1]
#role=person[2]
#country=person[3]

name,age,role,country ,city=person

print(role)

person1=['Maria',29,'Data Engineer', 'Spain']

*detail,city=person1

print(*detail)


person=['Maria',29,'Data Engineer', 'Spain']

name, *_, country=person

print(country)
print(name)


numbers= [1,5,2,4,3,'a']
print(any(numbers))
print(numbers.count(2))
print(numbers.index(1))



numbers= [1,5,2,4,3,'a']
numbers=[1,5,2,4,3,'a']
print(numbers is numbers)

letters= ['a','b','c']
letters.extend(['x','y'])
print(letters)

letters= ['a','b','c']
letters.insert(5,'x')
print(letters)


matrix=[
      ['a','b','c'],
      ['d','e','f'],
      ['g','h','i']
]
matrix.append(['x','y','z'])
matrix.insert(0,['a','aa','aaa'])
print(matrix)

matrix=[
      ['a','b','c'],
      ['d','e','f'],
      ['g','h','i']
]
matrix[1].append('x')
matrix[0].insert(0,'zz')
matrix[0].insert(0,'')
print(matrix)

letters= ['a','b','c']
letters.remove('b')
letters.pop(1)
print(letters)


matrix=[
      ['a','b','c'],
      ['d','e','f'],
      ['g','h','i']
]

matrix.remove(['a','b','c'])
matrix[0].pop(1)
print(matrix)


letters=['a','b','c']
letters[0]='x'
letters[1]='y'
print(letters)

matrix=[
      ['a','b','c'],
      ['d','e','f'],
      ['g','h','i']
]

matrix[2]=['x','xx','xxx']
matrix[0][0]= '-'
matrix[1][2]='-'
print(matrix)



letters=['c','a','b']
letters.sort(reverse=True)
print(letters)

matrix=[
      ['a','b','c'],
      ['d','e','f'],
      ['g','h','i']
]

matrix[0].sort(reverse=True)
print(matrix)

letters=['c','a','b']
new_list=sorted(letters)
print(new_list)


letters=['c','a','b']
letters.reverse()
new_list=list(reversed(letters))
print(new_list)

letters=['c','a','b']
copylist=letters.copy()  # shallow copy
copylist.pop()
print(copylist)
print(letters)



letters=['c','a','b']
copylist=letters.copy()  # shallow copy
copylist.pop()
print(copylist)
print(letters)


import copy
matrix=[
      ['a','b','c'],
      ['d','e','f'],
      ['g','h','i']
]
matrix_copy=copy.deepcopy(matrix)
matrix.pop()
matrix_copy[0].append('z')
print(matrix_copy)
print(matrix)

import copy
list1=[
      ['a','b'],
      ['c','d']
]
copy1=list1
print(copy1 is list1)

# shallow copy
copy2=list1.copy()
print(copy2 is list1)

print(list1[0] is copy2[0])

deep_copy=copy.deepcopy(list1)
print(deep_copy is list1)




#combining

letters= ['a','b','c']
numbers =[1,2,3]

comb=letters+numbers
print(comb)

print(letters*2)

comb2=[letters,numbers]
print(comb2)

letters= ['a','b','c']
numbers =[1,2,3]
numbers.extend(letters)
print(numbers)

letters= ['a','b','c']
numbers =[1,2,3]
comb=list(zip(letters,numbers))
print(comb)


id=[101,102,103]
names=['Ali','Sara','Jhon']

comd2=list(zip(id,names))
print(comd2)

letters= ['a','b','c']
new_list=[]
for l in letters:
      new_list.append(l.upper())
      print(new_list)
      

letters= ['a','b','c']
print(list(enumerate(letters,start=1)))

letters= ['a','b','c']
for index, value in enumerate(letters):
      print(index,value)
      
letters= ['a','b','c']
print(list(reversed(letters)))

letters= ['a','b','c']
for l, value in enumerate(reversed(letters)):
      print(l,value)
        
letters= ['a','b','c']
numbers=[1,2,3]

print(list(zip(numbers,letters)))    

letters= ['a','b','c']
numbers=[1,2,3]
for l,n in zip(letters,numbers):
      print(l,n)

letters= ['a','b','c']
print(list(map(str.upper,letters)))     

numbers=['1','2','3']
print(list(map(int,numbers)))

names=[' Marium ', 'Jhon ', ' Kumar']

print(list(map(str.strip,names)))
  
names=[' Marium ', 'Jhon ', ' Kumar']     
for n in map(str.strip,names):
      print(n)


letters= ['a','b',True,'','c']
print(list(filter(bool,letters)))


items=['sql','123','python','42']

print(list(filter(str.isalpha,items)))

items=['sql','123','python','42']
for i in filter(str.isalpha,items):
      print(i)
      
multiply = lambda x: x*2      

print(multiply(2))


addition =lambda x,y: x+y

print(addition(1,2))

check=lambda i: i in "python"

print(check("n"))

price = ['$12.50','$9.99','$100.00']

print(list(map(lambda p: float(p.replace('$','')),price)))
 


price = ['$12.50','$9.99','$100.00']
fun=lambda p: map(lambda x :float(x.replace('$','')),p)
print(list(fun(price))) 


prices=[120,13,0,300,80]

print(list(filter(lambda p: p >= 100,prices)))

prices=[120,13,0,300,80]


chec= lambda x: filter(lambda p: p>=100,x)

print(chec(prices))


prices = [120, 13, 0, 300, 80]

chec = lambda x: filter(lambda p: p >= 100, x)

print(list(chec(prices)))


students=[['Maria',85],
          ['Kumar',90],
          ['Max',60]
          ]

print(list(filter(lambda row:row[1] >70,students)))

students=[['Maria',85],
          ['Kumar',90],
          ['Max',60]
          ]
print(students[2][0].startswith('M'))

print(list(filter(lambda row: row[0].startswith('M'),students)))



domain=['www.google.com',
        'openai.com',
        'localhost',
        'WWW.DATAWITHBARAA,COM']

Cleaned= [
      d.lower().replace('www.','')
      for d in domain
      if '.' in d
]

print(Cleaned)    


domain=['www.google.com',
        'openai.com',
        'localhost',
        'WWW.DATAWITHBARAA,COM']

Cleaned2= [d for d in domain if '.' in d]

print(Cleaned2)

my_list=[10,30,20,10]

print(my_list[1])   # orderded
my_list[3]=40
print(my_list)  # mutabble   # every thing is allowed



# tuple
my_list=(10,30,20,10)
print(my_list)  # orderded  duplicates
print(my_list[1])
my_list[3]= 40
print(my_list)   # immutable


my_list=(10,30,20,10)
print(sorted(my_list))   # output is list not tuple


my_set= {10,30,20,10}
print(my_set)   # make the set ordered
print(my_set)  # remove the duplicates
print(my_set[2])   # Not indexed


my_set= {10,30,20,10}
print(my_set.remove(30))


a={10,20,30,40}
a.add(50)
print(a)


a={10,20,30,40}
a.update({2,3})
print(a)


a={10,20,30,40}
a|={1,2}
print(a)


a={10,20,30,40}
a.remove(10)
print(a)


a={10,20,30,40}
a.discard(50)
print(a)


a={10,20,30,40}
b={30,40,50,60}

#mathematical operation

print(a.union(b))
print(a | b)
print(a.intersection(b))
print(a & b)
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
print(a.isdisjoint(b))   ## check not overlap


my_dictonary={
      'a':10,
      'b':20,
      'c':20,
      'a':40
}

print(my_dictonary)  # orderded
   # keys are unique vales allow duplicates


print(my_dictonary['b'])  # Not index but keyed

my_dictonary={
      'a':10,
      'b':20,
      'c':20,
      'a':40
}
my_dictonary['c']=80
print(my_dictonary)

user={'id':1,'age':30,'city':'berlin'}

#acess

print(user.get('age'))

# check
print('age' in user)
      
user={'id':1,'age':30,'city':'berlin'} 

# View objects
print(user.keys())    
print(user.values()) 
print(user.items())
print(user)

user={'id':1,'age':30,'city':'berlin'} 

for u in user:
      print(u,user[u])


user={'id':1,'age':30,'city':'berlin'} 
for  u,v in user.items():
     print(u,v)      

user={'id':1,'age':30,'city':'berlin'} 

user["name"]="Jhon"
user["age"]=35
user.update({"age":60,"city":"paris"})

print(user)

user={'id':1,'age':30,'city':'berlin'} 
user.pop("age",'not found')

print(user)

user={'id':1,'age':30,'city':'berlin'} 
user.popitem()
print(user)

user={'id':None,
      'name': None,
      'age': None,
      'city':None
      }

user=dict.fromkeys(['id','name','age','city'],None)
print(user)

row= {
      'id':101,
      'name':'Jhon',
      'country':'DE',
      'age':29,
      'status':'active'
}

user={"id":1,"name":"Jhon","age":30,"city":"Berlin"}

user_str={
      k.upper():v.upper() #Expression
      for k,v in user.items()
            if isinstance(v,str)#Loop
      #Filter
}
print(user_str)

def make_coffe():
      print('Start Macibe')
      print('make Coffee')
      print('Enjoy it')
      print('Add milk')
      print('Enjoy it') 

make_coffe()

def greet():
      print("Hello and Welcome")

greet() 

case_rule="lower"
def clean_name(name):
      cleaned=name.strip().lower() # localvariable
      if case_rule=="lower":
       cleaned=cleaned.lower()
      print(cleaned)

clean_name('Ghafran')
clean_name('Kumar  ')
clean_name(' ')


def clean_name(first_name,last_name,country='n/a'):
      first=first_name.strip().lower()
      last=last_name.strip().lower()
      full_name=first+" "+last
      print(full_name, "From", country)

clean_name('GHAFRAN','KHAN','PAKISTAN')      # positional Arguments 

clean_name(first_name=" Ghafran ", country=' pakistan', last_name= " Khan ")  # keyword Arguments 


clean_name(' Ghafran',last_name='  Khan')


# calculate the total  of multiple values
def total(*args):
      print(sum(args))
 
total(2,3,4,5,6) 


# user profile
def create_user(**kwargs):
      print(kwargs)
 
create_user(first_name="Mo",
            last_name="salar",
            age=33,
            country='Egypt') 

def clean_name(name):
      
       lo_cleaned=name.strip().lower()
       up_cleaned=name.strip().upper()
       return lo_cleaned,up_cleaned      

lo_name,up_name=clean_name("GHAFRAN")   
print(lo_name,up_name) 

def write_log(message):
      with open(r"C:\Users\Ghafran\Downloads\SQL\python_learning\app.log", "a")  as file:
            file.write(message + "\n") 
        
write_log("App Started")            
write_log("user log in")

# Cleans email addresses and splits then into structured data
#return username and domain

def clean_and_split_email(email):
      cl_email=email.strip().lower()
      #sara@gamil.com
      username, domain=cl_email.split("@")
      return {"username": username,
              "domain": domain}

print(clean_and_split_email("Sara@gmail.com"))


#Checks whether the password meets the minimum requirement of 8 charachter

def is_valid_password(password):
      return len(password)>=8

print(is_valid_password("1234"))

def is_valid_email(email):
      return "@" in email and "." in email
print(is_valid_email("Sqrq@gamial.com"))      

def calculating_discount(price:float,rate:float)->float:
  """
  Calcuting the price after applying a discount
  Args:
   price(float): Original Product Price.
   rate(float): Discount Rate as numbers (e.g 20 for 20%)
   return:
    final price after applying discount
  """
  
  final_price =price-(price* rate/100)
  return final_price
  
calculating_discount(100,5) 
