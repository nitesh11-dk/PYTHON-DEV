import platform
print(platform.python_version())

# name = input("What is your name? \n")

# toPrint = input("Do you want to print? Type Yes\n")

# if toPrint.lower == 'yes':
#     print(f"Your name is {name}")
#     if name.startswith("N") or name.startswith("n"):
#         print("Ohh, you are lucky! Your name starts with N.")
#     else:
#         print("Ohh, you are not lucky!")
# else:
#     print("Oh, it seems you don't want to print your name!")


# team1 = ['Yoda' ]
# team2 = ['Jack' , 'Rose']
# team3 = [ 'Darth' ,'Vader' , 'Leah']

# print(f""" team 1 is {team1} \n
#  team 2 is {team2} \n
#  team 3 is {team3} \n
# """)

# selTeam =  int(input("enter the team number you want to chose "))


# if selTeam == 1:
#     print(f"you pick team 1 , and it has only {len(team1)} character , they are  {team1}")
# elif selTeam == 2:
#     print(f"you pick team 2 , and it has only {len(team2)} character  , they are{team2}")
# elif selTeam == 3:
#     print(f"you pick team 3 , and it has only {len(team3)} character  ,they are{team3}")
# else:
#     print(" please enter the daafult team number ")

# if selTeam %2 ==0 :
#     print("The number of people in your team are even")
# else:
#     print("The number of people in your team are odd")



# # ! match , case  , swtich case
# good_or_not   = int(input("enter the number form 1  tp 3"))
# match good_or_not:
#     case 1:
#         print("you are good one ")
#     case 2 :
#         print("you are good 2 ")
#     case 3 :
#         print("you are good 3 ")

#  here by deafult break is automatically added ;


#  ! 14  formatting
name = 'nitesh' 
age =18

# print(f"your name is {name} and age is {age}")
# print(f"your name is {name} and age is {age:.2f}")
# here :.2f ise used for 2 decimal points more 



# print("your name is  and age is" + {age}) # ! will get an error
# File "D:\USER\NITESH\Desktop\PY-US\level6.py", line 65, in <module>
#     print("your name is  and age is" + {age})
#           ~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~
# TypeError: can only concatenate str (not "set") to str


# ! 17 Slicing 

# full_name = "james bond"

# print(full_name[0:5])
# print(full_name[6:10])

name = 'Titanic'

# print(name[-1])
# print(name[6])
# print(name[len(name) -1])

# ! 20 Loops 

ls = ['Leia'  , 'Look' ]


# for i in ls:
#     print(f"{i}  ,i am your father")
# # for i in range(1,9): # 9 is excluded here 
# #     print(f"{i} is your name ")

# baby_yoda_age = 1912 
# while baby_yoda_age <= 1984:
#     print(f"no one found in titanic  {baby_yoda_age}")
#     baby_yoda_age += 1


