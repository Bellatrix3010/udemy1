# # This is a sample Python script.
#
# # Press Umschalt+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if _me__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
###
#d3-->27
# user_prompt="enter a task: "
#
# tasks = []
#
# while True:
#     task=input(user_prompt)
#     print(task.capitalize())
#     tasks.append(task)
#     print(tasks)
#
# ###########

from unittest import case
#
# tasks = []
#
# while True:
#
#     user_prompt_action = input("write add, show, or exit: ")
#
#     match user_prompt_action:
#         case 'add':
#             task=input("enter a task: ")
#             tasks.append(task)
#         case 'show':
#             print(tasks)
#         case 'exit':
#             break
#
# print('bye!!!')
#############

# tasks = []
#
# while True:
#     user_prompt_action = input("write add, show, or exit: ")
#     user_prompt_action = user_prompt_action.strip()
#
#     match user_prompt_action:
#         case 'add':
#             task = input("enter a task: ")
#             tasks.append(task)
#         case 'show':
#             for item in tasks:
#                 print(item)
#         case 'exit':
#             break
#         case _:
#             print("hey! you entered an unknown command ;), please wriete onlyadd, show or exit!!! ")
#
# print('byyyyyyyyyye')

#### meine rahe halll
# #greetings[]
# while True:
#     user_country = input('country? ')
#     user_country = user_country.strip()
#     match user_country:
#         case 'USA':
#             print('Hello')
#         case 'India':
#             print('Namaste')
#         case 'Germany':
#             print('Hallo')
# ########### rahe halle website

# user_country = input('country? ')
# user_country = user_country.strip()
# match user_country:
#     case 'USA':
#         print('Hello')
#     case 'India':
#         print('Namaste')
#     case 'Germany':
#         print('Hallo')
#     case _:
#         print('Whaaatttt? ;)')

######
#
# ingredients = ["john smith", "sen plakay", "dora ngacely"]
# for name in ingredients:
#     print(name.title())

####
# buttons = ["cancel", "reply", "submit"]
#
# for i in buttons:
#     print(i.capitalize())
#####
# buttons = ["cancel", "reply", "submit"]
#
# for i in buttons:
#     print(i.capitalize())
###
# for item in ["sandals", "glasses", "trousers"]:
#     print(item.capitalize())

##rooze4

# tasks = []
#
# while True:
#
#     user_prompt_action = input("write add, show, edit or exit: ")
#
#     match user_prompt_action:
#         case 'add':
#             task=input("enter a task: ")
#             tasks.append(task)
#         case 'show':
#             print(tasks)
#         case 'edit':
#             number=int(input('enter the number of the task to change: '))
#             number: int=number-1 #in python a list starts with 0, but the user do not know it!!!
#             new_task=input('your new task: ')
#             tasks[number]=new_task
#         case 'exit':
#             break
#
# print('bye!!!')
#############
# numbers = ["10", "20"]
# result = int(numbers[0]) * int(numbers[1])
# print(result)
####
# rate=0.95
# dollar_by_user=float(input("how much dollar? "))
# calc_euro = dollar_by_user * rate
# print("The amount of Euro is: ")
# print(calc_euro)
########
ranking = ['John', 'Sen', 'Lisa']

# rank_prompt=int(input("Please inter the rank of a spotler: "))
# print(ranking[rank_prompt - 1])

#######
# rank_prompt=int(input("enter the name of the sportler: "))
# person_prompt=person_prompt-1
# print(ranking[person_prompt])

######
# sportlerme_prompt=input("enter the name of the sportler: ")
# index=ranking.index(sportlerme_prompt)+1
# print(index)
##########
# elements = ['a', 'b', 'c']
# new = 'x'
# elements[1]=new
# print(elements)
###
# waiting_list=["sen","ben","john"]
# waiting_list.sort()
# for index, item in enumerate(waiting_list):
#     sortlist=f"{index+1}.{item.capitalize()}"  #f string method
#     print(sortlist)

###########

# for i, j in enumerate("abcd"):
#     print(i + 1)

######
# for i, j in enumerate("abcd"):
#     print(i)
#
# for i, j in enumerate("abcd"):
#     phrase = f"Printing {i * 5}"
#     print(phrase)
#
# for i, j in enumerate("abcd"):
#     print(f"Printing {j * 5}")

# filenames = ['document', 'report', 'presentation']
# for index, item in enumerate(filenames):
#     listfilenames=f"{index}-{item.capitalize()}.txt"
#     print(listfilenames)

####
# ips = ['100.122.133.105', '100.122.133.111']
# pin_prompt=int(input("enter an of ip that you want: "))
# message=f"You chose {ips[pin_prompt]}"
# print(message)
####
# menu = ["pasta", "pizza", "salad"]
#
# user_choice = int(input("Enter the index of the item: "))
#
# message = f"You chose {menu[user_choice]} :) "
# print(message)

# menu = ["pasta", "pizza", "salad"]
#
# for i, j in enumerate(menu):
#     print(f"{i}.{j}")
########
# buttons = [('John', 'Sen', 'Morro'), ('Lin', 'Ajay', 'Filip')]
# for first, second, third in buttons:
#     print(second)
###
# name = input("Enter your name: ")
# print(f"Your name is {name} <ß")

#####rooze6 -60 120221216


# while True:
#
#     user_prompt_action = input("write add, show, edit or exit: ")
#
#     match user_prompt_action:
#         case 'add':
#             task=input("enter a task: ") + "\n"
#
#             file=open('tasks.txt', 'r')
#             tasks=file.readlines()                         #primary list ra bekhooneh, ta badan betoneh item jadid behesh ezafeh koneh!!!!
#             file.close()
#
#             tasks.append(task)
#
#             file=open('tasks.txt', 'w')                    #new tasks with old ones
#             file.writelines(tasks)
#             file.close()
#
#         case 'show':
#             file=open('tasks.txt','r')
#             tasks=file.readlines()
#             file.close()
#
#             for index, item in enumerate(tasks):
#                 row=f"{index+1}-{item}"
#                 print(row)
#
#         case 'edit':
#             number=int(input('enter the number of the task to change: '))
#             number: int=number-1 #in python a list starts with 0, but the user do not know it!!!
#             new_task=input('your new task: ')
#             tasks[number]=new_task
#         case 'exit':
#             break
#
# print('bye!!!')

####################64 mohraviate content ra mirizeh tooye har directory!!!
# contents=["AAA","BBB","CCC"]
# filenames=["a.txt","b.txt", "c.txt"]
#
# for content, filename in zip(contents, filenames):
#     file=open(f"46files/{filename}", 'w')
#     file.write(content)
###########
# file = open('logs.txt', 'w')
# file.write('101.102.103.222 GET 01.988')
# file.write('171.131.104.108 POST 2.143') #list e dovvom ezafeh misheh beh liste 1
# file.close()
# #####
# file = open('logs.txt', 'w')
# file.write('101.102.103.222 GET 01.988')
# file.close()
#
# file = open('logs.txt', 'w')
# file.write('171.131.104.108 POST 2.143')   #faghat liste dovvom mimooneh, avvali overwrite misheh!!
# file.close()
##### 46 codings
# file=open('46files/coding/essay.txt', 'r')
# sentence=file.read()
# print(sentence.title())
####
# file=open('46files/coding/essay.txt', 'r')
# sentence=file.read()
# print(len(sentence))
##########
# member=input("Please enter a new member name: ") + "\n"
#
# file=open('46files/coding/members.txt', 'r')
# existing_members=file.readlines()
# file.close()
#
# existing_members.append(member)
#
# file=open('46files/coding/members.txt', 'w')
# existing_members=file.writelines(existing_members)
# file.close()
#
# # f=open('46files/coding/members.txt', 'r')
# # content=f.read()
# # print(content)
# # f.close()
########## or so: from internet!!!
# member = input("Add a new member: ")
#
# file = open("members.txt", 'r')
# existing_members = file.readlines()
# file.close()
#
# existing_members.append(member + "\n")
#
# file = open("members.txt", 'w')
# existing_members = file.writelines(existing_members)
# file.close()
####
# contents=["hello", "Hello","hello"]
# filenames=["aa.txt", "aaa.txt", "aaaa.txt"]
#
# for content, filename in zip(contents,filenames):
#     file=open(f"46files/coding/{filename}", 'w')
#     file.write(content)
#     file.close()
####or from website

# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
#
# for filename in filenames:
#     file = open(filename, 'w')
#     file.write("Hello")
#     file.close()

####
# F=["a.txt","b.txt","c.txt"]
#
# for f in F:
#     file=open(f"46files/coding/{f}", 'r')
#     content=file.read()
#     print(content)
###
# ####day7  L71    --> see line 370 with strip
# while True:
#
#     user_prompt_action = input("write add, show, edit or exit: ")
#
#     match user_prompt_action:
#         case 'add':
#             task=input("enter a task: ") + "\n"
#
#             file=open('tasks.txt', 'r')
#             tasks=file.readlines()                         #primary list ra bekhooneh, ta badan betoneh item jadid behesh ezafeh koneh!!!!
#             file.close()
#
#             tasks.append(task)
#
#             file=open('tasks.txt', 'w')                    #new tasks with old ones
#             file.writelines(tasks)
#             file.close()
#
#         case 'show':
#             file=open('tasks.txt','r')
#             tasks=file.readlines()
#             file.close()
#
#             for index, item in enumerate(tasks):
#                 item=item.strip('\n')             #lesson 71: strip: to remove breklines when we print the txt contents!!!
#                 row=f"{index+1}-{item}"
#                 print(row)
#
#         case 'edit':
#             number=int(input('enter the number of the task to change: '))
#             number: int=number-1 #in python a list starts with 0, but the user do not know it!!!
#             new_task=input('your new task: ')
#             tasks[number]=new_task
#         case 'exit':
#             break
#
# print('bye!!!')

# ####
# filenames=["1.doc","1.report", "1.presentation"]
# # to rename all the list members
# filenames=[filename.replace ('.', '-') + ('.txt') for filename in filenames]
# print(filenames)
####
# new = []
#
# for i in [1, 2, 3]:
#     new.append(i + 10)
#
# print(new)

###
# new = [i for i in ['a', 'b', 'c']]
# print(new)

###
# names = ["john smith", "jay santi", "eva kuki"]
# names=[name.title() for name in names]
# print(names)
###
# names = ["john 1990", "alberta1970", "magnola2000"]
# names=[len(name) for name in names]
# print(names)
####
# user_entries = ['10', '19.1', '20']
# floatUE=[float(i) for i in user_entries ]
# print(floatUE)
####
# user_entries = ['10', '19.1', '20']
# user_entries_int=[float(i) for i in user_entries]
# #XXXXX eshtebehhhhh --> nicht so komlex !!!! ;)) summ=[sum(i) for i in user_entries_int]
# print(sum(user_entries_int))
# # print(user_entries_int)
# # print(user_entries)
####
# temperatures = [10, 12, 14]
# temp_str=[str(i) + '\n' for i in temperatures]  #in khat ezafeh shod beh kod avvalieh!!!!
# file = open("file.txt", 'w')
#
# file.writelines(temp_str)
####
# numbers = [10.1, 12.3, 14.7]
# numbers = [int(number) for number in numbers]
# print(numbers)
#### day8, lesson 80 --> "with ... as file" is beter than "file=open()..."
# while True:
#
#     user_prompt_action = input("write add, show, edit or exit: ")
#
#     match user_prompt_action:
#         case 'add':
#             task=input("enter a task: ") + "\n"
#
#             # file=open('tasks.txt', 'r')
#             # tasks=file.readlines()                         #primary list ra bekhooneh, ta badan betoneh item jadid behesh ezafeh koneh!!!!
#             # file.close()
#             with open('tasks.txt', 'r') as file:
#                 todos=file.readlines()  #in 2 khat kare 3 khte bala ra mikoneh! va behtareh!!!!
#
#
#             tasks.append(task)
#
#             # file=open('tasks.txt', 'w')                    #new tasks with old ones
#             # file.writelines(tasks)
#             # file.close()
#             with open('tasks.txt', 'w') as file:   #with is better than open...
#                 file.writelines(tasks)
#
#         case 'show':
#             # file=open('tasks.txt','r')
#             # tasks=file.readlines()
#             # file.close()
#             with open('tasks.txt','r') as file:
#                 tasks = file.readlines()
#
#             for index, item in enumerate(tasks):
#                 item=item.strip('\n')             #lesson 71: strip: to remove breklines when we print the txt contents!!!
#                 row=f"{index+1}-{item}"
#                 print(row)
#
#         case 'edit':
#             number=int(input('enter the number of the task to change: '))
#             number: int=number-1 #in python a list starts with 0, but the user do not know it!!!
#             new_task=input('your new task: ')
#             tasks[number]=new_task
#         case 'exit':
#             break
#
# print('bye!!!')
# ####################################################################################################
# #### day8 --> "with ... as file" is beter than "file=open()..."
# while True:
#
#     user_prompt_action = input("write add, show, edit or exit: ")
#
#     match user_prompt_action:
#         case 'add':
#             task=input("enter a task: ") + "\n"
#
#             with open('tasks.txt', 'r') as file:
#                 todos=file.readlines()  #in 2 khat kare 3 khte bala ra mikoneh! va behtareh!!!!
#
#             tasks.append(task)
#
#             with open('tasks.txt', 'w') as file:   #with is better than open...
#                 file.writelines(tasks)
#
#         case 'show':
#             with open('tasks.txt','r') as file:
#                 tasks = file.readlines()
#
#             for index, item in enumerate(tasks):
#                 item=item.strip('\n')             #lesson 71: strip: to remove breklines when we print the txt contents!!!
#                 row=f"{index+1}-{item}"
#                 print(row)
#
#         case 'edit':
#             number=int(input('enter the number of the task to change: '))
#             number: int=number-1 #in python a list starts with 0, but the user do not know it!!!
#
#             with open('tasks.txt','r') as file:
#                 tasks = file.readlines()
#
#             new_task=input('your new task: ')
#             tasks[number]=new_task + '\n'
#
#             with open('tasks.txt', 'w') as file:   #with is better than open...
#                 file.writelines(tasks)
#
#         case 'exit':
#             break
#
# print('bye!!!')

# with open("file.txt", 'r') as file:
#     file.read()

####83: daily journal app

# date=input("Please enter today's date (yyyy.mm.dd): ")
# mood=input("How do you rate your mood today from  1 :|  to  10 :))  : ")
# thoughts=input("Let your toughts flow... \n ")
#
# with open(f"bonus/83_daily_journal/{date}.txt", 'w') as file:
#     file.write(mood + 2*'\n')
#     file.write(thoughts)
############
# with open("file.txt", 'w') as file:
#     file.write("Hello")
#
# with open("file.txt", 'w') as file:
#     file.write("Hi")

###
# with open("file.txt", 'w') as file:
#     file.write("Hello")
#     file.write("Hi")

###
# while True:
#     with open("coin_play/sides_na.txt", 'r') as file:  #txt must be create before running the code!!!
#         sides=file.readlines()
#
#     side=input("Throw the coin and enter head or tail here:  ?") + '\n'
#
#     sides.append(side)
#
#     with open("coin_play/sides_na.txt", 'w') as file:
#         file.writelines(sides)
#
#     nr_head=sides.count("head\n")
#     percentage=nr_head / len(sides) * 100
#     print(len(sides))
#     print(nr_head)
#     print(f"Heads: {percentage}%")


# #############
# while True:
#     with open("coin_play/sides.txt", 'r') as file:
#         sides = file.readlines()
#
#     side = input("Throw the coin and enter head or tail here: ?") + "\n"
#
#     sides.append(side)
#
#     with open("coin_play/sides.txt", 'w') as file:
#         file.writelines(sides)
#
#     nr_heads = sides.count("head\n")
#     percentage = nr_heads / len(sides) * 100
#
#     print(f"Heads: {percentage}%")
#############
# x = 0
#
# if len("Hello") == 5:
#     x = x + 1
# elif len("Hello") > 5:
#     x = x + 2
# else:
#     x = x + 3
#
# print(x)
#
# ids = ["XF345_89", "XER76849", "XA454_55"]
#
# x = 0
#
# for id in ids:
#     if '_' in id:
#         x = x + 1
# print(x)

####
# ids = ["XF345_89", "XER76849", "XA454_55"]
#
# x = 0
#
# for id in ids:
#     if '_' in id:
#
#         x = x + 1
# print(x)
#
# ####
# ids = ["XF345_89", "XER76849", "XA454_55"]
#
# x = 0
#
# for id in ids:
#     if '_' in id:
#         x = x + 1
# print(x)
# ids = ["XF345_89", "XER76849", "XA454_55"]
#
# x = 0
#
# for id in ids:
#     if '_' in id:
#         x = x + 1
# print(x)

####
# length = float(input("Enter length: "))
# width = float(input("Enter width: "))
#
# perimeter = (length + width) * 2
# area = length * width
#
# print("Perimeter is", perimeter)
# print("Area is", area)
#
# if perimeter < 14 and area < 8:
#     print("OK")
# else:
#     print("NOT OK")
###94
# password=input("enter a new password: ")
#
# if len(password) > 7:
#     print("greate password there!!")
# else:
#     print("Your password is weak!")

####

# password=input("enter a new password: ")
#
# if len(password) > 7:
#     print("greate password there!!")
# elif len(password) == 7:
#     print("Your password is OK, but not too strong!")
# else:
#     print("Your password is weak!")
# ####
# try:
#     "a" + 2
# except TypeError:
#     print("Cannot add number to string.")
# # ###
# try:
#     "a" + 2
# except IndexError:
#     print("Cannot add number to string.")

# waiting_list = ["john", "marry"]
# name = input("Enter name: ")
#
# if name not in waiting_list:
#     exit(f"{name} is not in the list.")
#
# number = waiting_list.index(name)
# print(f"{name}'s turn is {number}")


###


# waiting_list = ["john", "marry"]
# name = input("Enter name: ")
#
# try:
#
#     number = waiting_list.index(name)
#     print(f"{name}'s turn is {number}")
#
# except ValueError:
#     print(f"{name} is not in the list.")

######
# try:
#     total_value=input("renter total value: ")
#     enter_value=input("enter value: ")
#     percentage= (float(enter_value)/float(total_value))*100  #20/50*100
#     print(f"That is {percentage}%")
# except ValueError:
#     exit("you need enter a number. Run the program again!")
############
#day10
# try:
#     total_value=input("enter total value: ")
#
#     enter_value=input("enter value: ")
#     percentage= (float(enter_value)/float(total_value))*100  #20/50*100
#     print(f"That is {percentage}%")
#
# except ZeroDivisionError:
#     exit("Your total value can not be zero!")
#
# except ValueError:
#     exit("you need enter a number. Run the program again!")

# ####     day 10: to svoid repeat a code: custom-function  --> to call it above program , starts with def....                                                                                       day8 --> "with ... as file" is beter than "file=open()..."

# ###################################################################
# def get_tasks():  #function without argument
#
#     with open('tasks.txt', 'r') as file_local:
#         tasks_local = file_local.readlines()  # in 2 khat kare 3 khte bala ra mikoneh! va behtareh!!!!
#     return tasks_local
#
#     # with open('tasks.txt', 'w') as file:  # with is better than open...
#     #     file.writelines(tasks)
#
#
# while True:
#
#     user_prompt_action = input("write add, show, edit or exit: ")
#
#     match user_prompt_action:
#         case 'add':
#             task=input("enter a task: ") + "\n"
#
#             tasks = get_tasks()  #call our function!!! shabihe other functions mesle open, print, input ...and other
#
#             tasks.append(task)
#
#             with open('tasks.txt', 'w') as file:   #with is better than open...
#                 file.writelines(tasks)
#
#         case 'show':
#             tasks=get_tasks()
#
#             for index, item in enumerate(tasks):
#                 item=item.strip('\n')             #lesson 71: strip: to remove breklines when we print the txt contents!!!
#                 row=f"{index+1}-{item}"
#                 print(row)
#
#         case 'edit':
#             number=int(input('enter the number of the task to change: '))
#             number: int=number-1 #in python a list starts with 0, but the user do not know it!!!
#
#             tasks=get_tasks()
#
#             new_task=input('your new task: ')
#             tasks[number]=new_task + '\n'
#
#             with open('tasks.txt', 'w') as file:   #with is better than open...
#                 file.writelines(tasks)
#
#         case 'exit':
#             break
#
# print('bye!!!')

####day10, 111 difference between "function definition" and "function calls"
# def greet():
#     message = "hello"
#     new_message = message.capitalize()
#     return new_message


# greetings = greet()
# print(greetings)

#######day 11 / Lesson 112 bonus
# def get_average():
#     with open("bonus/files/data.txt", 'r') as file:
#         data=file.readlines()   #file.redlines() yek list ast!! pas migim kojash ra bekhooneh!!! ;)
#     values=data[1:]
#     values=[float(i) for i in values]
#
#     average_local=sum(values)/len(values)
#     return average_local
#
#
#
#
# average=get_average()
# print(average)
#
# ######

# def get_average():
#     x = "hello"
#     return x.capitalize()
#
# print(get_average())

####
##rooze 11 -coding exe.
# def get_max():
#     grades=[9.6, 9.2, 9.7]
#     max_local=max(grades)
#     min_local=min(grades)
#     message=f"Max: {max_local}, Min: {min_local}"
#     return message
#
#
# print(get_max())
##########################################114
# def get_maximum():
#     celsius = [14, 15.1, 12.3]
#     maximum = max(celsius)
#     return(maximum)
#
#
# celsius = get_maximum()
# fahrenheit = celsius *1.8 +32
# print(fahrenheit)

# ##############################################################119
# def get_tasks():  #function without argument  --> today with argument/parameters :)) --> code ra update nakardammm :|
#
#     with open('tasks.txt', 'r') as file_local:
#         tasks_local = file_local.readlines()  # in 2 khat kare 3 khte bala ra mikoneh! va behtareh!!!!
#     return tasks_local
#
#     # with open('tasks.txt', 'w') as file:  # with is better than open...
#     #     file.writelines(tasks)exit
#
#
# while True:
#
#     user_prompt_action = input("write add, show, edit or exit: ")
#
#     match user_prompt_action:
#         case 'add':
#             task=input("enter a task: ") + "\n"
#
#             tasks = get_tasks()  #call our function!!! shabihe other functions mesle open, print, input ...and other
#
#             tasks.append(task)
#
#             with open('tasks.txt', 'w') as file:   #with is better than open...
#                 file.writelines(tasks)
#
#         case 'show':
#             tasks=get_tasks()
#
#             for index, item in enumerate(tasks):
#                 item=item.strip('\n')             #lesson 71: strip: to remove breklines when we print the txt contents!!!
#                 row=f"{index+1}-{item}"
#                 print(row)
#
#         case 'edit':
#             number=int(input('enter the number of the task to change: '))
#             number: int=number-1 #in python a list starts with 0, but the user do not know it!!!
#
#             tasks=get_tasks()
#
#             new_task=input('your new task: ')
#             tasks[number]=new_task + '\n'
#
#             with open('tasks.txt', 'w') as file:   #with is better than open...
#                 file.writelines(tasks)
#
#         case 'exit':
#             break
#
# print('bye!!!')
#######################121


#####################122
# def prepare(text):
#     text = text.title()
#     text = text.strip()
#     return text
#
#
# print(prepare("hello    "))

####
# def speed(distance, time):
#
#     return distance / time
#
#
# print(speed(200, 4))
##########123
# user_liter_prompt=input("input a number as liter to change it to liter: ")
# def conver_liter_to_cubicmeter():
#     return(int(user_liter_prompt)/1000)
#
# print(conver_liter_to_cubicmeter())

####rahe dovvom:
# def liters_to_m3(liters):
#     m3=liters/1000
#     return m3
######bonus from day 9
# password=input("enter a new password: ")
#
# if len(password) > 7:
#     print("greate password there!!")
# elif len(password) == 7:
#     print("Your password is OK, but not too strong!")
# else:
#     print("Your password is weak!")

#####################day 12
# ############# day 12 exe2
#
# user_password=input("enter new password:")
#
# def strenght(password):
#     '''doc-string
#     a strenght password:
#     lenght>=8
#     at least one digit
#     at least one tppercase letter
#     '''
#     result={}
#     if len(password) >= 8:
#         result["lenght"]=True
#     else:
#         result["lenght"]=False
#
#     digit=False
#     for i in password:
#         if i.isdigit():
#             digit=True
#
#     result["digits"]=digit
#
#     uppercase=False
#     for i in password:
#         if i.isupper():
#             uppercase=True
#
#     result["upper_case"]=uppercase
#
#     if all(result.values()):
#          return "Strong Password"
#     else:
#          return "Weak Password"
#
#
# print(help(strenght))
# print(strenght(user_password))

###132 example ---> dictionary

###frage 2 _lesson 12
# def get_area(x=10):
#     return x * 2
#
#
# area = get_area(x=1)
# print(area)
####
# def calculate_time(h, g=9.80665):
#     t = (2 * h / g) ** 0.5
#     print(h)
#     print(g)
#     print(t)
#     return t
#
#
# time = calculate_time(100)
# print(time)
###############################
# year_of_birth=input("enter your birth year (yyyy): ")
#
#
# def age_get(year_of_birth , current_year=2022):
#     age_local= (current_year - int(year_of_birth))
#     return age_local
#
#
# age=age_get(year_of_birth)
# print(age)

######################
# def age_get(year_of_birth , current_year=2022):
#     age_local= (current_year - int(year_of_birth))
#     return age_local
#
# year_of_birth=int(input("enter your birth year (yyyy): "))
# age=age_get(year_of_birth)
# if age > 120:
#     print("Are you sure about your age? ;)")
# else:
#     print(age)

####

# def get_names(user_input):
#     items=user_input.split(',')
#     return len(items)
#
#
# user_input=input("enter names, separated ba commas (no spaces):")
# lenghtname=get_names(user_input)
# print(lenghtname)

######
# contents=["AAA","BBB","CCC"]
# filenames=["a.txt","b.txt", "c.txt"]
#
# for content, filename in zip(contents, filenames):
#     file=open(f"46files/{filename}", 'w')
#     file.write(content)

# ################
# ############Dominik Stegmann13:27
# from pathlib import Path
# test_path = Path('//gid-archiv1/2019--GeoBasisdaten//Bayer/Deutschland/Ausgangsdaten/Klima/GFA/GFA_grids_utm32_250m')
#
# a_paths = [a for a in test_path.glob('ArRed*.sgrd')]
# b_paths = [b for b in test_path.glob('BrRed*.sgrd')]
# m_paths = [m for m in test_path.glob('MaxRed*.sgrd')]
#
# for a, b, m in zip(a_paths, b_paths, m_paths):
# print(f'a={a}')
# print(f'b={b}')
# print(f'm={m}')
#
# #################Dominik Stegmann11:24
# for a, b, m, nd in zip(A, B, M, ND):
####### day 13/day14
feet_inches = input("Enter feet and inches: ")


def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")

####
#######                            day 13/day14 --> in code inja run nmisheh!!!! tooye bounus run misheh:)


#from bonus.bonus14.parser14 import parse   -->automatik az refactor--> move e ghesmate def miad in khat!!! :)
from parser14 import parse
#from bonus.bonus14.converters14 import convert
from converters14 import convert
feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")

############################