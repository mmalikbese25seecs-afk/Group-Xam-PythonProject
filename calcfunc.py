# The function that calculates two inputs

def calculator_Salman():

    print("\t\tWelcome to Smart Calculator")

    while True:   #loops till user wants to wxit
      
      try:     #to make sure input is only digits.
       a=float(input("Please Enter the Number 1 : "))
       b=float(input("Please Enter the Number 2 : "))

      except ValueError:      #The continue ensures to take values tillright value is entered
        print("Please enter Digits Only")
        continue
      
      #Giving user the choice what operation he wants to perform
      print()
      print("Select Which Operation You Want To Perform:")
      print("\t1= Addition(+)")
      print("\t2= Subtraction(-)")
      print("\t3= Multiplication(*)")
      print("\t4= Division(/)")
      print("\t5= All")
      print("\t6= EXIT")  #It breaks the loop
      print()

      choice= input("Enter your choice: \n\t")
      print()

      if choice=="1":    #Addition 
       print("Adiitiontion of ",a," + " ,b ," = ",a+b)
       print()
      #subtraction
      elif choice=="2" : 
        print("Subtraction of ",a," - " ,b ," = ",a-b)
        print()
      
      elif choice=="3" : #Multiplication
        print("Multiplycation of ",a," * " ,b ," = ",a*b)
        print()
  
      elif choice=="4" : #Division
      #The try/except make sure number is not being divided by zero

        try:
           print("Division of ",a," / " ,b ," = ",a/b)    
           print()
        except ZeroDivisionError : #error when divisor is zero
            print("A Number cannot Be Divided By Zero")

   #Choice 5 performs all operations on the numbers

      elif choice =="5":  
        print("Adiitiontion of ",a," + " ,b ," = ",a+b)           
        print( "Subtraction of ",a," - " ,b ," = ",a-b)
        print("Multiplication of ",a," * " ,b ," = ",a*b)

        try:   # try/except donot allow division by 0
           print("Division of ",a," / " ,b ," = ",a/b)    
           print()

        except ZeroDivisionError :     #Error when divisor is zero
            print("A Number cannot Be Divided By Zero")
            print()

      elif choice == "6":
            print("Exiting Calculator")
            break           #This breaks the loop
      
      else :      #if input is otherthan 1-6,its not valid
        print("Wrong Input ")



calculator_Salman()