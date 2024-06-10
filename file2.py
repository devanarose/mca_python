# listt = ['Devana','adithya','aswin','sivanand','dhaivath']
# if 'adithya' in listt : print("present in the list") 
# else : print("not present")

# listt.sort()
# i=0
# #for i in listt : print(listt)
# while i<len(listt) :
#     print(listt[i])
#     i=i+1

#arithmetic operations
val1 = int(input('enter first number '))
val2 = int(input('enter second number '))
inp = int(input('1. Addition\n2.Subtraction\n3.Multiplication\n4.Division\nENTER CHOICE : '))
match inp:
    case 1: print(val1 + val2)    
    case 2: print(val1 - val2)
    case 3: print(val1 * val2)
    case 4: print(val1 / val2) 
    case _ : print("invalid choice") 