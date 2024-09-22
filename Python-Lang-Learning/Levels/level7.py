
#   ! Tuple is immutable , that is we cannot remove or append  elements inside the tuple 

# tpl =  (1,2,3,4)
# # print(tpl.index(3)) , get the idex of the argument that we apssed in 

# ls =    list(tpl)
# ls[2] = "hello"
# tpl = tuple(ls)

# print(tpl)

# ? Dictornaries 

dict = {
    "name":"nitesh",
    "age":18,
    "age":21,
    21:"yak ",
    "nested":{
        "first":"Kushwaha"
    }
}

# print(dict[21])  
# # print(dict['21'])  # error 
# print(dict['name'])
# # print(dict[name]) # error
# # ? nested accessing
# print(dict['nested']['first'])

# ? sets -- do not cantain any duplicate , and it is just like real  maths sets , you can perfom all the operation called intersection , union , difference  ... 

# s1 = { 1,2,3}

# s1.difference_update({1,2,3,4})
# print(s1)

