while True:
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("︱                       WELCOME TO ACT                             ︱")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("─────────────────────────────────────────────────────────────────────")
    print("  1.ACT 102                                                          ")
    print("                                                                     ")
    print("  2.ACT 103                                                          ")
    print("─────────────────────────────────────────────────────────────────────")
    shit = int(input("\n PLEASE CHOOSE THE TYPE OF ACT YOU WANT TO OPEN: "))

    if shit == 1:
        #while True:
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("︱                  FUNMENTALS OF PROGRAMMING                       ︱")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

            print("─────────────────────────────────────────────────────────────────────")
            print("  1.PRELIM LESSON                                                    ")
            print("                                                                     ")
            print("  2.MIDTERM LESSON                                                   ")
            print("                                                                     ")
            print("  3.FINAL LESSON                                                     ")
            print("─────────────────────────────────────────────────────────────────────")

            print("─────────────────────────────────────────────────────────────────────")
            we = int(input("\n CHOOSE TERM(1-3) : "))

            if we == 1:
                print("──────────────────────────────────────────────────────────────────")
                print("                      PRELIM LESSON                               ")
                print(" 1. LESSON 1 : INTRODUCTION TO PROGRAMMING                        ")
                print(" 2. PYTHON PRINT SYNTAX                                           ")
                print(" 3. PYTHON COMMENTS                                               ")
                print(" 4. VARIABLES,CONTANTS AND DATA TYPES IN PYTHON                   ")
                print(" 5. BASIC DATA TYPES IN PYTHON                                                  ")
                print(" 6. ARITHMETIC OPERATORS                                          ")
                print("──────────────────────────────────────────────────────────────────")
                choice = int(input("PLEASE SELECT THE LESSON YOU WANT TO OPEN : "))
                print("──────────────────────────────────────────────────────────────────")
                if choice == 1:
                    print("INTRODUCTION TO PROGRAMMING          \n")
                    print("WHAT IS PROGRAMMING LANGUAGE?"
                          "\n-A programming language is a special language that computers understand and use to perform tasks\n")
                    print("    Common Languages:")
                    print("   > Python → Easy to learn, great for beginners")
                    print("   > C / C++ → Fast and powerful")
                    print("   > Java → Platform independent")
                    print("   > JavaScript → For websites")
                    print("   > PHP → For web backends")
                    print()
                    print("WHAT IS PROGRAMMING?\n")
                    print(
                        "-Python is a high-level, interpreted, and general-purpose programming "
                        "\nlanguage designed to be simple, readable, and easy to learn.")
                    print("PYTHON was created by Guido van Rossum in 1991.")
                if choice == 2:
                    print("PYTHON PRINT SYNTAX\n")
                    print("Python Print Syntax                                             ")
                    print("\nis a Python insturctions that will output values and results to the computer screen.")
                    print("\nExample:\n")
                    print("           INPUT                        OUTPUT                    ")
                    print("┃       print(Hello, World) ┃      Hello World           ┃        ")
                    print("PYTHON SYNTAX")
                    print("1. Python is Case-Sensitive")
                    print("Python treats uppercase and lowercase letters differently.\n")
                    print("2. Indentation")
                    print(
                        "Unlike other programming languages, Python uses indentation (spaces) to define blocks of code.\n")
                    print("PRINTING OUTPUT")
                    print("Print Statement: ")
                    print("- The print() function displays information on the screen.")
                    print("Syntax: print(value)")
                    print("print - the function that displays output.")
                    print("() - parentheses that contain the information to be displayed.")
                    print("value - the text, number, variable, or expression you want to show.\n")
                    print("PRINT TEXT")
                    print("Text (also called a string) must be enclosed in quotation marks.\n")
                    print("PRINTING NUMBERS")
                    print("You can print numbers directly without quotation marks.")
                if choice == 3:
                    print("          PYHTON COMMENTS          \n")
                    print("-Comments are ignored by Python.")
                    print("-They are used to explain the code.\n")
                    print("Exercise 1: Getting to Know You with print()")
                    print(
                        "Objectives\n""By the end of this activity, you should be able to:"
                        "\nPractice using the print() function."
                        "\nDisplay text, numbers, and formatted output."
                        "\nUnderstand the difference between single quotes (' ') and double quotes (" ")")
                    print(
                        "Instruction\nCreate a Python program that uses only the print() function."
                        "\n  Do not use variables, input(), or any other Python statements.\n")
                    print("Your program should display the following information:\n")
                    print("1.Your Full Name")
                    print("2.Your Age")
                    print("3.Your Favorite Subject")
                    print("4.Your Dream Job")
                    print("5.A short quote or motto that inspires you")
                    print(
                        "6.A creative ASCII Art made using the print()"
                        "\n function (e.g., a smiley face, house, heart, flower, cat, or any simple design).")
                    print("Full Name       : Juan Dela Cruz")
                    print("Age             : 18")
                    print("Favorite Subject: Programming")
                    print("Dream Job       : Software Develope")
                    print("Quote:\nSuccess is the sum of small efforts repeated day in and day out.\n")
                if choice == 4:
                    print("          VARIABLES AND DATA TYPES          \n")
                    print("1. What is a Variable?")
                    print(
                        "-A variable is a named storage location used to keep data in a program."
                        "\nThe value of a variable can change while the program is running."
                        "\nExample: a, b, c, age, name")
                    print("Variable Naming Rules:")
                    print(
                        "•A variable can have a short name (like x and y)or a more descriptivename (age, carname,total_volume).")
                    print("•A variable name muststart with a letter or theunderscore character.")
                    print("•A variable name cannotstart with a number.")
                    print("Variable names are case-sensitive \n(age and AGE are two different variables)")
                    print("Assigned value to variable")
                    print(
                        "-In programming, we store data in variables."
                        "We assign a value to a variable using the = (assignment operator).")
                    print("Output Variables")
                    print("-The Python print() function is often used to output variables.")
                    print("-In the print() function, you output multiple variables, separated by a comma:")
                    print("-In the print() function, you output multiple variables, separated by a +:\n")
                if choice == 5:
                    print("         BASIC DATA TYPES IN PYTHON           \n")
                    print(
                        "Data types are categories that tell Python what kind of data a variable stores."
                        "They determine the type of value a variable can hold and what operations can be performed on that value.\n")
                    print("      |123|                 INT-Interger Numbers  ")
                    print("      |3.14|                FLOAT-Decimal Numbers ")
                    print("      |“|                   STR-String or Text    ")
                    print("      |T/F|                 BOOL-Boolean values   ")
                    print("DECLARATION OF VARIABLES")
                    print("VARIABLE".ljust(15) + "VALUE".ljust(12) + "DATA TYPE".ljust(15) + "DESCRIPTION")
                    print("name".ljust(15) + '"Maria"'.ljust(12) + "str".ljust(15) + "Stores text inside quotes.")
                    print("age".ljust(15) + "20".ljust(12) + "int".ljust(15) + "Stores whole numbers.")
                    print("grade".ljust(15) + "89.5".ljust(12) + "float".ljust(
                        15) + "Stores numbers with decimal points.")
                    print("is_enrolled".ljust(15) + "True".ljust(12) + "bool".ljust(
                        15) + "Stores True or False values.\n")
                    print("ASSIGNED VALUE AND OUTPUT THE VALUE")
                    print(100 * "_")
                    print('1  name = "Maria"'.ljust(32) + "# string")
                    print('2  age = 20'.ljust(32) + "# integer")
                    print('3  grade = 89.5'.ljust(32) + "# float")
                    print('4  is_enrolled = True'.ljust(32) + "# boolean")
                    print('5  print(name)'.ljust(32) + "---------> # prints name")
                    print('6  print(age)'.ljust(32) + "---------> # prints age")
                    print('7  print(grade)'.ljust(32) + "---------> # prints grade")
                    print('8  print(is_enrolled)'.ljust(32) + "---> # prints status")

                if choice == 6:
                    print("What are Arithmetic Operators?")
                    print("- Arithmetic operators are symbols used to perform mathematical calculations on numbers.")
                    print("They work the same way as the operators used in everyday mathematics.")
                    print("────────────────────────────────────────────────────────────────────")
                    print("                 PYTHON  ARITHMETIC OPERATORS          \n")
                    print("────────────────────────────────────────────────────────────────────")
                    print("Operator        Description        Example           Result")
                    print("   +              Addition:         5 + 3               8  ")
                    print("   -             Subtraction:       10 - 4              6  ")
                    print("   *             Multiplication:    7 * 2               14 ")
                    print("   /           Division (float):    15 / 3              5.0")
                    print("  //         Floor Division:       17 // 3              5  ")
                    print("  %              Modulus:           10 % 3              1  ")
                    print("  *          Exponentiation:       2 * 3                8  ")
                    print("────────────────────────────────────────────────────────────────────")
                    print(
                        "  An expression is a combination of values, variables, and operators that evaluates to result. ")
                    print("a = 10\nb = 5\nresult = a + b\nprint(the result is:, result ")
                    print("────────────────────────────────────────────────────────────────────")
                    print("1.Additon\n Add two numbers.")
                    print("2.Subtraction\n Subtract the second number from the first number.")
                    print("3.Multiplication\n Multiplies two numbers.")
                    print("4.Division\nDivide the first number from the second number(float result).")
                    print("5.Floor Division\n Divides and returns the whole number part.")
                    print("6.Modulus\n Returns the remainder of the division.")
                    print("7.Exponentiation\nRaises the first number to the power of second.")
                    print("────────────────────────────────────────────────────────────────────\n")
                    print("────────────────────────────────────────────────────────────────────")
                    print("Python follows the order of operations PEMDAS):                     ")
                    print("Parentheses, Exponents, Multiplication, Division, Addition, Subtraction")
                    print("────────────────────────────────────────────────────────────────────\n")
                    print("────────────────────────────────────────────────────────────────────")
                    print("                            PEMDAS Example                          ")
                    print("                print(2 + 3 * 4)      # Output: 14                  ")
                    print("                print((2 + 3) * 4)    # Output: 20                  ")
                    print("────────────────────────────────────────────────────────────────────\n")
                    print("BASIC INPUT AND OUTPUT IN PYTHON")
                    print("- Accepting User Input Purpose of input in programming")
                    print("- Real-life analogies (e.g., asking for a user's name and responding)")

            elif we == 2:
                print("──────────────────────────────────────────────────────────────────")
                print("                       MIDTERM LESSON                             ")
                print(" 1. CONDITIONAL STATEMENTS in PYTHON                                                ")
                print(" 2. LOGICAL OPERATOR                                                      ")
                print("──────────────────────────────────────────────────────────────────")
                choice2 = int(input("\n PLEASE SELECT THE LESSON YOU WANT TO OPEN : "))
                if choice2 == 1:
                    print("          CONDITIONAL STATEMENTS in PYTHON         \n")
                    print("Introduction to conditional statements")
                    print(
                        "-A conditional statement allows program to make decision based on wheater a condition is True or False.\n")
                    print("Relational Operators")
                    print(
                        "-Relational operators, also called comparison operators, are used to comapre two values"
                        "\nThe result is always either True or False.\n")
                    print("───────────────────────────────────────────────────────────────────────────────────────")
                    print("Operator            Meaning                         Example                      Result")
                    print("   ==               Equal to                        10 == 10                     True  ")
                    print("   !=               Not equal to                    10 != 5                      True  ")
                    print("   >                Greater than                    10 >  5                      True  ")
                    print("   <                Less than                       5  <  10                     True  ")
                    print("   >=               Greater than or equal to        10 >= 10                     True  ")
                    print("   <=               Less than or equal to           5  <= 10                     True  ")
                    print("───────────────────────────────────────────────────────────────────────────────────────")
                    print("\n-THE IF STATEMENT ")
                    print("-The if statement executes a block of code only when the condition is True.")
                    print("\n-THE IF-ELSE STATEMENT ")
                    print("-The else statement provides an alernative when if condition is True.")
                    print("\n-THE IF-ELIF-ELIF STATEMENT ")
                    print("The elif statement is used when there are multiple conditions to evaluate."
                        "\nPython checks each condition from top to bottom and executes the first condition that is True.\n")
                if choice2 == 2:
                    print("          LOGICAL OPERATOR         \n")
                    print("PYTHON LESSON: LOGICAL OPERATORS\n")
                    print("Learning Objectives")
                    print("-At the end of the lesson, students should be able to:\n")
                    print("1. Define logical operators in Python.")
                    print("2. Identify the three logical operators: and or, and not")
                    print("3. Use logical operators with conditional statements.")
                    print("4. Combine multiple conditions in a Python program.")
                    print("5. Create simple real-life programs using logical operators.\n")
                    print("What Are Logical Operators?")
                    print("Logical operators are used to combine or reverse conditions in a Python program."
                        "\nThey are commonly used with if, elif, and else.")
                    print("Python has three logical operators:")
                    print("────────────────────────────────────────────────────────────────────────────────────────")
                    print("          Operator                                             Meaning                  ")
                    print("            and                                      Both conditions must be True       ")
                    print("            or                                       At least one condition must be True")
                    print("            not                                      Reverses the result                ")
                    print("────────────────────────────────────────────────────────────────────────────────────────")
                    print("\nThe and Operator")
                    print("The and operator returns True only when ALL conditions are True.")
                    print("                 Truth Table -and                ")
                    print("─────────────────────────────────────────────────")
                    print("Condition A          Condition B          A and B")
                    print("  TRUE                  TRUE               TRUE  ")
                    print("  TRUE                  FALSE              FALSE ")
                    print("  FALSE                 TRUE               FALSE ")
                    print("  FALSE                 FALSE              FALSE ")
                    print("─────────────────────────────────────────────────")
                    print("\nThe or Operator")
                    print("The or operator returns True when at least ONE condition is True.")
                    print("                 Truth Table -or                 ")
                    print("─────────────────────────────────────────────────")
                    print("Condition A          Condition B          A and B")
                    print("  TRUE                  TRUE               TRUE  ")
                    print("  TRUE                  FALSE              TRUE  ")
                    print("  FALSE                 TRUE               TRUE  ")
                    print("  FALSE                 FALSE              FALSE ")
                    print("─────────────────────────────────────────────────")
                    print("\nThe not Operator")
                    print("The not operator reverses the result of a condition.")
                    print("        Truth Table -not        ")
                    print("────────────────────────────────")
                    print("Condition          Not Condition")
                    print("  TRUE                  FALSE   ")
                    print("  FALSE                 TRUE    ")
                    print("────────────────────────────────")
            elif we == 3:
                print("──────────────────────────────────────────────────────────────────")
                print("                       FINAL LESSON                               ")
                print(" 1. INTRODUCTION TO ITERATION AND LOOPS                           ")
                print("──────────────────────────────────────────────────────────────────")
                choice3 = int(input("\n PLEASE SELECT THE LESSON YOU WANT TO OPEN : "))
                if choice3 == 1:
                    print("          INTRODUCTION TO ITERATION          \n")
                    print("Iteration means repeating a process.")
                    print("In programming, it means repeatedly executing a set of instructions. "
                          "Each repetition is called an iteration.")
                    print("Iteration allows a program to perform the same task multiple times.")
                    print("Both programs produce the same output, but the loop makes the program shorter and easier to modify.")
                    print("To repeat the message 100 times, change 4 to 100.\n")
                    print("PYTHON WHILE LOOP")
                    print("──────────────────────────────────────────────────────────────────")
                    print("        Syntax                                   Example Code     ")
                    print("  while condition:                             count = 1          ")
                    print("      statement(s)                             while count <= 5:  ")
                    print("                                                    print(count)  ")
                    print("                                                    count += 1    ")
                    print("──────────────────────────────────────────────────────────────────")

            else:
                print("invalid")
                #break

            print(" QUIZ: FUNDAMENTALS OF PROGRAMMING ")
            print("------------------------------------------\n")
            score = 0
            # Question 1
            print("Q1: print(Hello, World), What is the correct output?")
            print("A) Hello World")
            print("B) HELLOM,WORLD")
            print("C) worldhello")
            ans1 = input("Your answer (A/B/C): ").upper().strip()
            if ans1 == "A":
                print("Correct!\n")
                score += 1
            else:
                print("ENGKKKK MALEEEEEEEE\n")
            # Question 2
            print("Q2: Which of these is NOT a programming language?")
            print("A) Python")
            print("B) HTML")
            print("C) KEYBOARD")
            ans2 = input("Your answer (A/B/C): ").upper().strip()
            if ans2 == "C":
                print("Correct!\n")
                score += 1
            else:
                print("TULOG KA SIGURO NUNG DINICUSS YAN\n")
            # Question 3
            print("Q3: What symbol do we use to make a decision in code?")
            print("A) if-else")
            print("B) input")
            print("C) + - * /")
            ans3 = input("Your answer (A/B/C): ").upper().strip()
            if ans3 == "A":
                print("Correct!\n")
                score += 1
            else:
                print("HAYNAKO\n")
            # Question 4
            print("Q4: What year was the python created?")
            print("A) 1998")
            print("B) 1991")
            print("C) 2026")
            ans4 = input("Your answer (A/B/C): ").upper().strip()
            if ans4 == "B":
                print("Correct!\n")
                score += 1
            else:
                print("PURO MALI ERP AH\n")
            # Question 5
            print("Q5: SINONG POGI SA TATLO?:")
            print("A) SIR MARK")
            print("B) PRINCE")
            print("C) SIR JOMAR")
            ans5 = input("Your answer (A/B/C): ").upper().strip()
            if ans5 == "B":
                print("Correct!\n")
                score += 1
            else:
                print("SI PRIMCE BERNARDO NG PINAKA MASANTING SA CCST\n")
            # Final Result
            print(" ==========================")
            print(f" YOUR TOTAL SCORE: {score}/5")
            percent = (score / 5) * 100
            print(f" That's {percent:.0f}%")
            print("===========================")
            if score == 5:
                print("PERPUK SOLID KANAMAN TOL")
            elif score >= 4:
                print("ONTI PA ERP!!!!")
            elif score >= 3:
                print("SIGE PWEDE NA")
            else:
                print("MAG PANGGAP KANG BUGA NE")
            print("\nSALAMAT SA PAGLALARO KAIBIGAN KONG TUNAY")

    elif shit == 2:
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("︱                  FUNMENTALS OF PROBLEM SOLVING                    ")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

        print("─────────────────────────────────────────────────────────────────────")
        print("  1.INTRODUCTION                                                     ")
        print("                                                                     ")
        print("  2.WHAT IS AN ALGORITHM?                                            ")
        print("                                                                     ")
        print("  3.WHAT IS AN PSEUDOCODE?                                           ")
        print("                                                                     ")
        print("  4.WHAT IS FLOWCHART?                                               ")
        print("                                                                     ")
        print("  5.PROGRAM LOGIC                                                    ")
        print("                                                                     ")
        print("  6.WHAT IS CONDITION?                                               ")
        print("                                                                     ")
        print("  7.IF ELSE STATEMENT                                                ")
        print("                                                                     ")
        print("  8.IF ELSE IF ELSE STATEMENT                                        ")
        print("─────────────────────────────────────────────────────────────────────")
        pili = int(input("\n CHOOSE LESSON:"))

        if pili == 1:
            print("                          INTRODUCTION                          \n")
            print("One of the biggest mistakes beginners make is immediately writing code without planning.")
            print("Professional programmers do not start coding first. Instead, they:")
            print("1.Understand the problem.")
            print("2.Plan the solution.")
            print("3.Design the logic.")
            print("4.Write the code.")
            print("5.Test and improve the program.\n")
            print("                     WHAT IS PROBLEM SOLVING?                     ")
            print("-Problem solving is the process of analyzing a problem")
            print("and finding the best solution before writing a")
            print("computer program.\n")
            print("The Programming Problem Solving Process")
            print("1.PROBLEM")
            print("2.ANALYZE")
            print("3.CREATE ALGORITHM")
            print("4.WRITE PSUEDOCODE")
            print("5.DRAW FLOWCHART")
            print("6.WRITE PROGRAM")
            print("7.TEST PROGRAM")

        if pili == 2:
            print("                      WHAT IS AN ALGORITHM?                     \n")
            print("•An algorithm is a step-by-step procedure used to")
            print("solve a problem or accomplish a task.")
            print("•Algorithms can be simple (e.g., a recipe for cooking a")
            print("rice) or complex (e.g., sorting a list of numbers).\n")
            print("Example of ALGORITHM:")
            print("Let us look at a recipe for cooking rice. It")
            print("consists of the following simple activities:\n")
            print("1.Put 1 cup of rice in the vessel of an electric rice-cooker.")
            print("2.Put 2 cups of water in the cooker vessel.")
            print("3.Close the lid of the cooker and switch it on.")
            print("4.Wait until the indicator light of the rice- cooker turns off.")

        if pili == 3:
            print("                     WHAT IS AN PSEUDOCODE?                    \n")
            print("•Pseudocode is an informal way of writing program")
            print("logic using simple English statements.")
            print("•It is not a programming language.")
            print("•It is simply a plan before coding.")
            print("────────────────────────────────────────────────────────────────────")
            print("Operator        Description        Example           Result")
            print("   +              Addition:         5 + 3               8  ")
            print("   -             Subtraction:       10 - 4              6  ")
            print("   *             Multiplication:    7 * 2               14 ")
            print("   /           Division (float):    15 / 3              5.0")
            print("  //         Floor Division:       17 // 3              5  ")
            print("  %              Modulus:           10 % 3              1  ")
            print("  *          Exponentiation:       2 * 3                8  ")
            print("────────────────────────────────────────────────────────────────────")

        if pili == 4:
            print("                     WHAT IS AN FLOWCHART?                    \n")
            print("A flowchart is a diagram representing the logical")
            print("sequence in which a combination of steps or")
            print("operations is to be performed.\n")
            print("────────────────────────────────────────────────────────────────────────────")
            print("             PSEUDOCODE                                FLOWCHART            ")
            print("START                                                   START               ")
            print("DECLARE number1, number2, sum:INREGER                     ↓                 ")
            print("OUTPUT Enter the first number                 number1, number2, sum:integers")
            print("INPUT number 1                                            ↓                 ")
            print("OUTPUT Enter the second number               OUTPUT Enter the first number  ")
            print("INPUT number 2                               INPUT number 1                 ")
            print("sum←number1+number2                                       ↓                 ")
            print("OUTPUT The sum is,sum                       OUTPUT Enter the second number  ")
            print("END                                         INPUT number 2                  ")
            print("                                                          ↓                 ")
            print("                                            sum = number1 + number2         ")
            print("                                                          ↓                 ")
            print("                                            OUTPUT The sum is,sum           ")
            print("                                                          ↓                 ")
            print("                                                         END                ")
            print("────────────────────────────────────────────────────────────────────────────")
        if pili == 5:
            print("                     PROGRAM LOGIC                    \n")
            print("•Program logic is the sequence of instructions that")
            print("tells a computer how to solve problem.")
            print("it follow a logical order to produce the correct output.\n")
            print("INPUT     ➔     PROGRESS     ➔     OUTPUT")

        if pili == 6:
            print("                     WHAT IS CONDITION?                    \n")
            print("•A condition is an expression that evaluates to either:")
            print("COMPARISON OPERATORS")
            print("─────────────────────────────────────────────────────────────────────────────────────────────")
            print("OPERATOR        MEANING         EXAMPLE                      EXPLANATION                     ")
            print("==             Equal to        score == 75      True if score is equal to 75.                ")
            print("!=           Not equal to      score != 75      True if score is not equal to 75.            ")
            print(">            Greater than      score >75        True if score is greater than 75.            ")
            print("<              Less than       score < 75       True if score is less than 75.               ")
            print(">=      Greater than or equal  score >=75       True if score is greater than or equal to 75.")
            print("<=        Less than or equal   score<=75        True if score is less than or equal to 75.   ")
            print("─────────────────────────────────────────────────────────────────────────────────────────────")

        if pili == 7:
            print("                   IF ELSE STATEMENT                   \n")
            print("- The if statement executes a block of code only when a condition is true.")
            print("- The else statement provides an alternative when the if condition is false.")
            print("SYNTAX")
            print("if condition : ")
            print("         statement")
            print("else :")
            print("         statement")
            print("Keypoints: ")
            print("Use else when you want an alternative action if the if condition is False.")
            print("Only one of the if or else block will be executed.\n")
            print("EXAMPLE:")
            print("score = 65")
            print("if score >= 18:")
            print('    print("PASSED")')
            print("else: ")
            print('    print("FAILED")\n')
            print("OUTPUT:")
            print("FAILED")
            print("EXPLANATION:")
            print("In this example, score is 65, which is less than 75,")
            print("so the else block runs and the program prints Failed.")
            print("Examples of if-else with All Comparison Operators")
            print("Examples of if-else with All Comparison Operators (score = 10)")

        if pili == 8:
            print("                   IF ELSE IF ELSE STATEMENT                   \n")
            print("•Use this structure when there are three or more possible outcomes.\n")
            print("IF condition THEN")
            print("   statement")
            print("ELSE IF condition THEN")
            print("   statement")
            print("ELSE")
            print("     statement")
            print("END IF")
            print("\nKEYPOINTS")
            print("Conditions are checked from top to bottom.")
            print("The first TRUE condition runs, and the rest are skipped")
            print("           START")
            print("             |")
            print("             ⬇  ")
            print("        CONDITION 1 ________➔yes (STATEMEN 1)-----→│")
            print("           TRUE?                                   │")
            print("             |                                     │")
            print("             |  NO                                 │")
            print("             ⬇                                     │")
            print("        CONDITION 2 ________➔yes (STATEMENT 2)-----│")
            print("           TRUE?                                   │")
            print("             |                                     │")
            print("             |  NO                                 │")
            print("        CONDITION N ________➔yes (STATEMENT N)-----│")
            print("           TRUE?                                   │")
            print("             |                                     │")
            print("             |  NO                                 │")
            print("             ⬇                                     │")
            print("            ELSE                                   │")
            print("         STATEMENT                                 │")
            print("             |                                     │")
            print("             |                                     │")
            print("             ⬇                                     │")
            print("            END ←----------------------------------↓")

    else:
        print("─────────────────────────────────────────────────────────────────────")
        print("PUMILI KALANG SA DALAWA HOYYYYYYYY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("─────────────────────────────────────────────────────────────────────")


    print(" QUIZ: FUNDAMENTALS OF PROBLEM SOLVING \n")
    score = 0
    # Question 1
    print("Q1: What is algorithm")
    print("A) a solution")
    print("B) a step-by-step procedure used to")
    print("C) this is a game")
    ans1 = input("Your answer (A/B/C): ").upper()
    if ans1 == "B":
        print("Correct!\n")
        score += 1
    else:
        print("AYOS TOLLLLLL\n")
    # Question 2
    print("Q2: Pseudocode is?")
    print("A) color")
    print("B) simple english-like plan before coding")
    print("C) place to take a rest")
    ans2 = input("Your answer (A/B/C): ").upper()
    if ans2 == "B":
        print("Correct!\n")
        score += 1
    else:
        print("LALAAAAA\n")
    # Question 3
    print("Q3: What does an if-else statement do?:")
    print("A) Makes a decision - do one thing OR another")
    print("B) SHET SHET NAKITA AKO")
    print("C) CUTTING")
    ans3 = input("Your answer (A/B/C): ").upper()
    if ans3 == "A":
        print("Correct!\n")
        score += 1
    else:
        print("PUYAT KA SIGURO\n")
    # Final Result
    print(" ---------------------------")
    print(f" Your total score: {score}/3")
    percentage = (score / 3) * 100
    print(f" That's {percentage:.0f}%")
    if score == 3:
        print("Excellent! You really know your stuff!")
    elif score == 2:
        print(" Good job! Keep it up!")
    else:
        print("Don't worry! Keep practicing, you'll get better!")

    break
