""" 
(1) Prompt the user to enter two words and a number, storing each into separate variables. Then, output those three values on a single line separated by a space.
Enter favorite color:
yellow                                                                                                                                                         
Enter pet's name:
Daisy                                                                                                                                                
Enter a number:
6

yellow Daisy 6

(2) Output two passwords using a combination of the user input. Format the passwords as shown below.
Enter favorite color:
yellow                                                                                                                                                         
Enter pet's name:
Daisy                                                                                                                                                
Enter a number:
6

yellow Daisy 6

First password: yellow_Daisy
Second password: 6yellow6

(3) Output the length of each password (the number of characters in the strings).
Enter favorite color:
yellow                                                                                                                                                         
Enter pet's name:
Daisy                                                                                                                                                
Enter a number:
6

yellow Daisy 6

First password: yellow_Daisy
Second password: 6yellow6

Number of characters in yellow_Daisy: 12
Number of characters in 6yellow6: 8 
"""

favoriteColor = input('Enter favorite color: \n')
petsName = input('Enter pet\'s name: \n')
num = input('Enter a number: \n')

print (favoriteColor, petsName, num)