

# ! strings

str = "hello" ;

# print(str[1:4])
# print(str[: 3])
# print(str[-5 : -1])
# print(str[::-1])

#  ! lists 
ls = ["apple" , "banan" , "grapes"]
ls.append("pear")
ls.extend(["jamun","chickuu"])
ls.insert(0 , "stawberry") #  replace nah i hota hai bas shoft ho jata hai 
ls.remove("apple")
ls.pop() # *  removes and return the last element  
# print(ls.index("pear"))   # ? return the index if not exist it will give error 
# print(ls.count("pear"))  #? return  how much times the elelment is repeated 
ls.sort(reverse=True)  # ? if you pass reverse True it will be in descending order other wise ascending order 
ls.reverse()
# newLs = ls.copy() # ? it is real copy 
newLs = ls # ? it is reference now 
ls.clear() 

# print(newLs)
# print(ls);



# ? Tuple : immutable 

tpl = (2,3,4)
# print(tpl.count(3)) # ? return the how much that element is repeate in the tuple 
# print(tpl.index(2)) # ? retrun in which index is the element  present 

# there are two method for tuples 

# you  u  want to add or remove or make changes in tuples you can do like this 
lstp = list(tpl) 
lstp.append("hello")
tpl  = lstp
# print(tpl)


# ! Member ship operator  
ls2 = [2,3,4,5,6,7]

# print(2 in ls2) # check if 2 is exist in ls2 
# print(2 not in ls2) # check if 2  do not  is exist in ls2 

# ! Identity 
c = 10 
d = c 

# print( c is not d ) # ? check is it is refernce or not 

# ! Dictonaries

dict = {
    "name":"nitesh",
    "age":18,
    21:"hello" ,
    "nested":{
        "first": "kushwaha"
    }
}


#  * Accesing the values 
# print(dict[21])
# print(dict["21"]) # ❌
# print(dict["name"])
# print(dict[name]) # ❌
# print(dict["nested"]['first'])

# print(dict.get("name")) # ! retrun the value fo the  provieded key 
# print(dict.items())  # ! retrun   list of tuple , ("key" , "value")

# for item , val in dict.items():
#         print(f"{item} : {val}")

# print(dict.keys()) # ! return the list of keys 
# print(dict.pop('name')) #! return  and removes the key that is provied with the value also 

# dict.setdefault("rakesh" , 10000) # ! retrun the value  of the key if exist 
# dict.values() #! retrun  a dict with key value 

# dict.clear()
print(dict.copy()) #! real copy not reference 
print(dict)





