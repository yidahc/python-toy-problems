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

print ('\n'+favoriteColor, petsName, num)

pswd1 = favoriteColor+'_'+petsName
print ('\nFirst password: ' + pswd1)

pswd2 = num+favoriteColor+num
print ('Second password: ' + pswd2)

print('\nNumber of characters in',pswd1+':',len(pswd1))
print('Number of characters in',pswd2+':',len(pswd2))



# Redoing toy problem with string formatting

favoriteColor = input('Enter favorite color: \n')
petsName = input('Enter pet\'s name: \n')
num = int(input('Enter a number: \n'))
# converting to int, since that is the data type we want to work with

print ('\n%s %s %d' % (favoriteColor, petsName, num))

pswd1 = favoriteColor+'_'+petsName
print ('\nFirst password: %s_%s' % (favoriteColor, petsName))

# %s and %d serve as placeholders for a string and digit respectively, so we can write the whole sentece without concatinating
# variables to replace placeholders are all writen afterwards, after the %, for easier legibility

pswd2 = str(num)+favoriteColor+str(num)
#converting to string, as python does not automatically typecast
print ('Second password: %d%s%d' % (num, favoriteColor, num))

print('\nNumber of characters in %s: %d' % (pswd1,len(pswd1)))
print('Number of characters in %s: %d' % (pswd2,len(pswd2)))