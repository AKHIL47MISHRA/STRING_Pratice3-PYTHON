# 2. Write a program to fill in a letter template given below with name and date.
# letter = ''' 
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

name=input("name of person: ")  #it will take str as input 
date=(input("date of selection: "))  #if you put int in front of inputt it will print only dat ea input not the month 
print(f"Dear {name},You are selected on {date}")

