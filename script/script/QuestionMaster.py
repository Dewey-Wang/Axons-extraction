class Questions:
    def __init__(self, question):
        self.question = question
        self.user_input = None

    def ask_question(self, input_type='string'):
        while True:
            try:
                if self.user_input is not None:
                    print(f"The input you entered was {self.user_input}. Please try again.")
                
                if input_type == 'yes_no':
                    self.user_input = input(f"{self.question} (y/n): ").lower()
                    if self.user_input in ['y', 'n']:
                        break
                    else:
                        print("Invalid input! Please enter 'y' or 'n'.")

                elif input_type == 'num':
                    self.user_input = float(input(f"{self.question}: "))
                    if self.user_input.is_integer():
                        self.user_input = int(self.user_input)
                    break
                    
                elif input_type == 'int':
                    self.user_input = int(input(f"{self.question}: "))
                    break
                    
                else:
                    # Default to string input
                    self.user_input = input(f"{self.question}: ")
                    break

            except ValueError:
                print(f"Invalid input! Please enter a valid {input_type}.")

        if input_type == 'yes_no':
            return self.user_input.lower() == 'y'
        else:
            return self.user_input

# Example usage:
if __name__ == "__main__":
    # Instantiate the Questions class with your question
    example_question = Questions("Do you want to continue?")

    # Ask the question and get the user's response
    user_response = example_question.ask_question(input_type='yes_no')

    # Process the user's response
    if user_response:
        print("User wants to continue.")
    else:
        print("User does not want to continue.")

    # Numeric question
    numeric_question = Questions("Enter a number")
    user_numeric = numeric_question.ask_question(input_type='num')
    print(f"User's response: {user_numeric}")
