# A simple python code for a simple calculator

def main():

    def menu():
        print("""
            What would you wish to do with your values: 
                1. Addition
                2. Subtraction
                3. Multiplication
                4. Division
                5. Find the remainder
                6. Comparison
        """)
    

#variables

    num1 = int(input("Enter the first value: "))
    num2 = int(input("Enter the second value: "))
    menu()
    oparand = int(input("What would you like to oparate with: "))
    status = True

    #functions
    def addition():
        result = num1 + num2

        print (f'The value of the oparation is {result}')

    def subtraction():
        result = num1 - num2

        print(f'The value of the oparation is {result}')

    def multiplication():
        result = num1 * num2

        print(f'The value of the oparation is {result}')

    def division():
        result = num1 / num2

        print(f'The value of the oparation is {result}')

    def modulance():
        result = num1 % num2

        print(f'The value of the oparation is {result}')

    def comparision():
        if num1 > num2:
            print(f'{num1} is greater than {num2}')

        else:
            print(f'{num2} is greater than {num1}')

    
        
    #statements

    if oparand == 1:
        addition()

    elif oparand == 2:
        subtraction()

    elif oparand == 3:
        multiplication()

    elif oparand == 4:
        division()

    elif oparand == 5:
        modulance()

    elif oparand == 6: 
        comparision()

    else:
        print(f'{num1} and {num2} cannot be oparated on mathematically')


    


main()   