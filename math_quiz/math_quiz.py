import random

def generate_random_integer(min_value, max_value):
    """
    Generate a random integer between the specified minimum and maximum values.

    Parameters:
    min_value (int): The minimum value for the random integer.
    max_value (int): The maximum value for the random integer.

    Returns:
    int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)

def get_random_operator():
    """
    Select a random mathematical operator from '+', '-', or '*'.

    Returns:
    str: A randomly selected operator.
    """
    return random.choice(['+', '-', '*'])

def create_math_problem(num1, num2, operator):
    """
    Create a math problem and calculate the correct answer based on the provided operator.

    Parameters:
    num1 (int): The first number in the math problem.
    num2 (int): The second number in the math problem.
    operator (str): The operator for the math problem ('+', '-', '*').

    Returns:
    tuple: A tuple containing the math problem as a string and the correct answer.
    """
    problem_statement = f"{num1} {operator} {num2}"
    
    # Correct answer calculations
    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2
    
    return problem_statement, correct_answer

def math_quiz():
    """
    Run the Math Quiz Game. Users are presented with a series of math problems, and they must provide answers.

    The game ends after the specified number of questions, and the user's score is displayed.
    """
    score = 0  # Initialize score counter
    total_questions = 3  # Set the number of quiz questions

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate two random integers and a random operator
        num1 = generate_random_integer(1, 10)
        
        # Adding error handling to ensure num2 is an integer
        try:
            num2 = generate_random_integer(1, 5)
        except ValueError:
            print("An error occurred while generating the second number. Please try again.")
            continue  # Skip this iteration if there's an error

        operator = get_random_operator()

        # Create a math problem and get the incorrect answer
        problem, answer = create_math_problem(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        # Get and validate user input
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        # Check if the user's answer matches the incorrect answer
        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1  # Increment score
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
