# sample_dict = {"name": "Kelly","age": 25, "salary": 8000, "city": "New york"} 
# sample_dict.pop('salary')
# sample_dict.pop('name')

# remove=['name','salary']
# for x in remove:
#    sample_dict.pop(x)
# print(sample_dict)   

#Count the frequency of each character in a given string using a dictionary. 
# k={"suv","maahi","vivek"}
# freq={}
# for x in k:
#     for char in x:
#         if char in freq:
#             freq[char]+=1
#         else:
#             freq[char]=1
# print(freq)               

#Swap keys and values in a dictionary. 
# k={'a':1,'b':2,'c':3}
# tem={}
# for x,y in k.items():
#     tem[y]=x
# print(tem)    

#Write a program to sum all the values in a dictionary. 
# k={'a':1,'b':2,'c':3,'d':4,'e':5}
# sum=0
# res={}
# for x,y in k.items():
#     sum+=y
# print(sum)    

#Create a nested dictionary for student details (name, roll, marks). 
# res={'student1':{'name':'suvarna','roll':21,'marks':90},
#      'student2':{'name':"maahi",'roll':22,'marks':89},
#      'student3':{'name':'bunty','roll':23,'marks':99}}
# print(res)

#Write a program to store names as keys and their lengths as values. 
# k={}
# for x in range(4):
#     name=input("enter ur name:")
#     k[name]=len(name)
# print(k)    
    
#Create a dictionary for numbers 1 to 5, where the value is "even" if the number is even, and "odd" if the number is odd .
# k={}
# for x in range(6):
#     if x%2==0:
#         k[x]="even"
#     else:
#         k[x]="odd" 
# print(k)
 
# words = ["cat", "dog", "bat"] 
# reverse={}
# for i in words:
#     reverse[i]=i[::-1]
# print(reverse)    