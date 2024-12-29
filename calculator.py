print("1 - add")
print("2 - subtract")
print("3 - multiply")
print("4 - divide")
option = int(input("chose an operator : "))

if(option in [1,2,3,4]):
    num1=int(input("enter 1 num : "))
    num2=int(input("enter 2 num : "))

    if(option == 1):
        result=num1+num2
    elif(option == 2):
        result=num1-num2
    elif(option == 3):
        result=num1*num2
    elif(option == 4):
        result=num1//num2

else:
    print("syntax error")
print("result of the operation is : ")
print(result)