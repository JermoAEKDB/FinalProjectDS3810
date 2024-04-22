import random

#Variables for random number generation between 1-69 and 1-26
var1 = random.randint(1,69)
var2 = random.randint(1,69)
var3 = random.randint(1,69)
var4 = random.randint(1,69)
var5 = random.randint(1,69)
var6 = random.randint(1,26)

#print greeting and selection Y/N
print("Welcome to the Powerball Number Generator!")
user_input = input("Would you like some Powerball Numbers? (Yes or No):")

# if-else functions for selection
if user_input == 'Yes' :
    print(str("Here are your selected numbers!:"),str(var1),"",str(var2),"",str(var3),"",str(var4),"",str(var5)," ",str(var6))
elif user_input == 'No' :
    print("Seems like you don't wan't to test your luck, Goodbye!")
else:
    print("Perhaps there has been an error,reset the generator and try again with (Yes/No).")

