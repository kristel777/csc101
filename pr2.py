#CSC 101
#Kristel Saraci
#Version 3 of the project
#Guessing game simulation.
#Create the first function.
def get_words():
    #Create a list with the names of the four software companies.
    my_list = ["Tesla", "Nvidia", "Amazon", "Microsoft"]
    return my_list
#Create the second function.
def check_words(guess, my_list):
    #Check if the user's guess is in the list.
    if guess in my_list:
        #Return the value if true otherwise return false.
        return True
    else:
        return False
#Create the third function.
def check_total(correct_count, incorrect_count):
    #Return winner if the correct count is over 7.
    if correct_count > 7:
        return "Winner"
    #Return loser is the incorrect count is over 7
    elif incorrect_count > 7:
        return "Loser"
    #Return draw if otherwise.
    else:
        return "Draw"
#Create the fourth function.
def main():
    #Initiazile the variables.
   correct_count = 0
   incorrect_count = 0
  #Create the for loop.
   for i in range(15):
        my_list = get_words()
        #Ask the user for it's input.
        user_guess = input("Guess a name of a software company: ")
        #Check if user's guess is correct.
        #Call the check_words function.
        correct = check_words(user_guess,my_list)
        if correct :
            #Increment the count of correct counts if the user guessed correctly.
            correct_count = correct_count + 1
            print('Correct')
            #Increment the count of incorrect counts if otherwise.
        else:
            incorrect_count = incorrect_count + 1
            print('Incorrect')

#Display the output of each count after the loop.
   print("Correct Guesses:", correct_count)
   print("Incorrect Guesses:", incorrect_count)
   #Call the check_total function and display the output of it.
   total_result = check_total(correct_count , incorrect_count)
   print("Game Result:",total_result)


#Call the mai function.
main()
