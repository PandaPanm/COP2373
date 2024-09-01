#Wes Williams
#9/1/24



# Create and write to 8ball_responses.txt
responses = [
    "Yes, of course!\n",
    "Without a doubt, yes.\n",
    "You can count on it.\n",
    "For sure!\n",
    "Ask me later!\n",
    "I'm not sure.\n",
    "I can't tell you right now.\n",
    "I'll tell you after my nap.\n",
    "No way!\n",
    "I don't think so.\n",
    "Without a doubt, no.\n",
    "The answer is clearly NO!\n"
]

with open('8ball_responses.txt', 'w') as file:
    file.writelines(responses)

print("File '8ball_responses.txt' created successfully with the responses.")

###############################################################################################################

import random


# Read responses from the 8ball_responses.txt that was made
def load_responses(filename):
    with open(filename, 'r') as file:
        responses = file.readlines()
    return responses


# Main function to interact with the user
def magic_8_ball():
    responses = load_responses('8ball_responses.txt')

    print("Welcome to the Magic 8 Ball!")

    while True:
        question = input("Ask a yes/no question (or type 'quit' to exit): ")

        if question.lower() == 'quit':
            print("Goodbye!")
            break

        if question.strip() == '':
            print("Please ask a question.")
            continue

        # Display a random response
        print(random.choice(responses))


# Run the Magic 8 Ball program
if __name__ == "__main__":
    magic_8_ball()


