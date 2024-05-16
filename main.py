# welcome the user
print('⚠️⚠️⚠️welcome to⚠️⚠️⚠️')
print('🌚freaky maths games🌚')

def yes_no(question):
    while True:
        response = input (question).lower()


        if response == 'yes' or response == "y":
            return "yes"
        elif response == 'no' or response == "n":
            return "no"
        else:
            print('please enter yes / no')

# instructions for game
def instructions():
    print('''in this 𝓕𝓻𝓮𝓪𝓴𝔂 math game you will be forced!
to answer the given questions or else you will be punished by 𝓕𝓻𝓮𝓪𝓴𝔂 𝓑𝓸𝓫 👅''')

# Asks the user if they would like to see the instructions
want_instruction = yes_no('do you need instructions(I would recomend) ')

# checks for yes or no
if want_instruction == 'yes':
    instructions()