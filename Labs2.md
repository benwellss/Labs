## Chapter 2 Labs
#### Part 1

        age = int(input("Enter age: "))
        
        if age >= 18:
            print("You are in category A")
        elif age >= 16:
            print("You are in category B")
        elif age < 16:
            print("You are in category C")
        else:
            print("Enter valid age")

#### Task 1

        print("Select operation: ")
        print("1. Add")
        print("2. Subtract")
        print("3. Divide")
        print("4. Multiply")
        
        
        choice = input("Enter choice from above (1/2/3/4): ")
        
        if choice in ("1", "2", "3", "4"):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        
            if choice == "1":
                    print("Result", num1 + num2)
            if choice == "2":
                    print("Result", num1 - num2)
            if choice == "3":
                if num2 == 0:
                    print("Error. Cannot divide by zero")
                else:
                    print("Result", num1 / num2)
            if choice == "4":
                    print("Result", num1 * num2)
        else:
            print("Invalid Input")

#### Task 3 (Task 2 skipped)

            level = int(input("Enter your level: "))
            grade = int(input("Enter your grade: "))
            
            if level == 1:
                if 71 < grade <= 100:
                    print("Distinction")
                elif 61 < grade <= 70:
                    print("Merit")
                elif 50 < grade <= 60:
                    print("Pass")
                elif grade <= 50:
                    print("Fail")
            if level == 2:
                if 66 < grade <= 100:
                    print("Distinction")
                elif 51 < grade <= 65:
                    print("Merit")
                elif 40 < grade <= 50:
                    print("Pass")
                elif grade <= 40:
                    print("Fail")
            else:
                print("Please enter valid value")

#### Task 4

            print("Pythagoras' Calculator: ")
            print("1. Find length of A given B and C")
            print("2. Find length of B given A and C")
            print("3. Find length of C given A and B")
            
            choice = input("Enter choice from above (1/2/3): ")
            
            if choice == "1":
                num1 = float(input("Enter B: "))
                num2 = float(input("Enter C: "))
                if choice == "1":
                    print("Result", num1**2 + num2**2)
            
            if choice == "1":
                num1 = float(input("Enter A: "))
                num2 = float(input("Enter C: "))
                if choice == "2":
                    print("Result", num1**2 + num2**2)
            
            if choice == "1":
                num1 = float(input("Enter A: "))
                num2 = float(input("Enter B: "))
                if choice == "3":
                    print("Result", num1**2 + num2**2)
            
            else:
                print("Invalid Input")
