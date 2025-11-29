




def calculator_Salman():

    print("\t\tWelcome to Smart Calculator") # Welcome

    while True:   #loops till user wants to wxit
      
      try:     #to make sure input is only digits.
       a=float(input("Please Enter the Number 1 : "))
       b=float(input("Please Enter the Number 2 : "))

      except ValueError:      #The continue ensures to take values till right value is entered
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


import random

def number_guessing_game():
    """
    A simple number guessing game where the computer selects a random number
    between 1 and 50 and the user tries to guess it.
    
    """
    while True:
        num = random.randint(1, 50)
        count = 0

        while True:
            guess = int(input("Guess a number between 1 and 50: "))
            count += 1

            if guess > num:
                print("Your guess is Too High\n")
            elif guess < num:
                print("Too Low! Try again.\n")
            else:
                print("\nCorrect! You guessed the number!")
                print("The number was:", num)
                print("Total guesses:", count)
                break

        play = input("\nDo you want to play again? (yes/no): ").lower()

        if play != "yes":
            print("Thanks for playing! Goodbye!")
            break
            print()

def main(): 
    while True:   # loops to ensure correct input
       print("\tWELCOME TO CALCULATOR AND GUESSING GAME BY GROUP Xam")
       print("Press 1 to enter Calculator")
       print("Press 2 to play Guess the Number")
       print("Press 3 to exit")
       choice = input("Enter your choice (1/2/3): ")
       if choice == "1":
            calculator_Salman()
            print()
       elif choice == "2":
            number_guessing_game()
            print()
       elif choice == "3":
            print("Goodbye!")
            break
       else:
            print("Invalid choice! Please enter 1, 2, or 3.")

main()  # calling main function that holds both functions