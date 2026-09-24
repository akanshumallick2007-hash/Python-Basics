import random #use to select random items.
import string #use to provide collection of characters.
length=int(input("Enter your Length:")) #take length from user.
char= (string.ascii_letters + #combines all lower_case and upper_case.
       string.digits + #combines all numbers from 0 to 9.        #and the (+) between these are help to connected with each other.
       string.punctuation) #combines all types of punctuation.
password=''.join(  #join all the items or elements with each other.
    random.choice(char)  #picks one random character.
    for i in range(length)  #repeat the action.
)
print("\nGenerate Password:",password) #print the line to clear understand.
print(password) #display password which is created.