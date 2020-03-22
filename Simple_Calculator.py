# It is a simple prototype of an calculator!!
# It accepts only two numeric values and an operator between them!!

print("""   
  This is a Two Number Calculator!
    Type the two numbers below!
    
  In this code you can use five types of operators:
         '+' , '-' , '*' , '/' , '%'
        
  Don't type an letter in the numeric value field!!!    
     """)


First_Number = int(input("What is the First Number in your Equation: "))
Second_Number = int(input("What is the Second Number in your Equation: "))
Operation = input("What is the Operator between the Two Numbers: ")

if Operation == '+':
    print(f"The Result is: {First_Number + Second_Number}")

elif Operation == '-':
    print(f"The Result is: {First_Number - Second_Number}")

elif Operation == '*':
    print(f"The Result is: {First_Number * Second_Number}")

elif Operation == '/':
    print(f"The Result is: {Second_Number / First_Number}")

elif Operation == '%':
    print(f"The Result is: {Second_Number / First_Number}")

else:
    print("This is an Invaild Operator!!!")