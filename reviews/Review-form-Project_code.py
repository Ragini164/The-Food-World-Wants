def push(lst, item):
       lst.append(item)
       return lst

##REVIEW FORM:
print('Hello, please let us know how your experience about our restaurant by filling out this survey!')
print('please tell us your name:)')
name=input()

print('Rate the food quality between 1 to 5, 1 as worst and 5 as excellent')
rate=int(input())
if rate==1:
       print('worst')
elif rate==2:
       print('Okay, Okay')
elif rate==3:
       print('Average')
elif rate==4:
       print('Good')
       
else:
       print('Excellent')
a=str(rate)+' '+'to our food quality'+'\n'


print('Rate the taste of our food between 1 to 5, 1 as worst and 5 as excellent')
rate=int(input())
if rate==1:
       print('worst')
elif rate==2:
       print('Okay, Okay')
elif rate==3:
       print('Average')
elif rate==4:
       print('Good')
else:
       print('Excellent')
b=str(rate)+' '+'to the taste of our food'+'\n'


print('Rate the presentation of our food between 1 to 5, 1 as worst and 5 as excellent')
rate=int(input())
if rate==1:
       print('worst')
elif rate==2:
       print('Okay, Okay')
elif rate==3:
       print('Average')
elif rate==4:
       print('Good')
else:
       print('Excellent')
c= str(rate)+' '+'to the presentation of our food'+'\n'



print('Rate our Service between 1 to 5, 1 as worst and 5 as excellent')
rate=int(input())
if rate==1:
       print('worst')
elif rate==2:
       print('Okay, Okay')
elif rate==3:
       print('Average')
elif rate==4:
       print('Good')
else:
       print('Excellent')
d=str(rate)+' '+'to our Service'+'\n'


lst=[]
print('Do you want to give any other comments(Yes, No)?')
inp=input()
if inp=='No' or inp=='no':
       print('Okay!\nThankyou!')
       e='No any other comments'
       push(lst,e)
elif inp=='Yes' or inp=='yes':
       print('Type here')
       z=input()
       print(z)
       zz='The comment given:'+z
       push(lst, zz)
       print('Thankyou!')
lst=''.join(lst)


data='\n'+name+':'+'\n'+a+b+c+d+str(lst)+'\n'
# print(data)
def saving_data(data):
       with open("review file.txt", "r+") as f:
              text=(f.read())
              f.write(data)
saving_data(data)
