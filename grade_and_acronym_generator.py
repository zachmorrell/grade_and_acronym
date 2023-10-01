# Function used to display the options of the program and navigate those options.
def instructions():
    menu_instructions = [
    "\n*       This program is used to solve specific geometry problems       *",
    "*   Option -   Description                                             *",
    "*     0        Display this message again.                             *",
    "*     1        Calculate a letter grade based on a 5 question test.    *",
    "*     2        Use any combination of words to create an acronym       *",
    "*     3        To exit the program entirely.                           *"]
    print(("*"*(len(menu_instructions[0])-1)), "\n".join(menu_instructions),"\n" + ("*"*(len(menu_instructions[0])-1)))

    while(True):
        option = int(input("Which numeric option do you wish to choose: "))
        match(option):
            case 0:
                print(("*"*(len(menu_instructions[0])-1)), "\n".join(menu_instructions),"\n" + ("*"*(len(menu_instructions[0])-1)))
            case 1:
                grade()
            case 2:
                acronym()
            case 3:
                exit()
            case _:
                print(f"selected {option}")

# Function that takes the number of correct answers out of 5 questions and returns a grade.
def grade():
    print("This program will return the grade on a 5 points quiz based on the points earned.")
    print("Enter a whole number ranging from 0 to 5. Avoid decimals as they will be rounded.\n")
    grade_index = ["F", "F", "D", "C", "B", "A"]
    score_given = False
    student_score = 0
    
    while score_given == False:
        try:
            student_score = int(input("Input your quiz point score: "))
            if 0 <= student_score <= 5:
                score_given = True
            else:
                print("The only acceptable inputs are preferrably whole numbers 0 to 5. Please try again.")
        except ValueError:
            print("Please enter a whole number 0 to 5")
    print("Your grade for this quiz is: ", grade_index[student_score])
    continue_calc(1)

# Function that creates an acronym for a group of words using the upper case.
def acronym():
    print("This program will print a resulting acroynm for a word or words.\n")
    user_input = input("Enter any text to generate an acroynm for it: ").split()
    print(''.join(word[0].upper() for word in user_input))
    continue_calc(2)
    
# Function displayed after each calculation to request if a user would like to perform more calculations, return to the instructions method, or exit the program.
def continue_calc(current_program):
    programs = [instructions, grade, acronym]

    # Displays the name of the function, without __name__ it would also supply the memory address.
    option = input(f"\nWould you like to continue with the {programs[current_program].__name__} program? (y/n/exit): ").lower()
    if(option == "y" or option == "yes"):
        programs[current_program]()
    elif(option == "exit" or option == "e"):
        exit()
    else:
        programs[0]()

# Starts the program, could be considered the main()
instructions()
