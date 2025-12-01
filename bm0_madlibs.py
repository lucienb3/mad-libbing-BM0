from numpy import random

rndstory = random.randint(1,3)
print(rndstory)



if rndstory == 1:
	adjective1 = input("write a adjective: ")
	noun1 = input('write a noun: ')
	action1 = input('write a present tense action: ')
	action2 = input('write a past tense action: ')
	print(f"once opon a time there was a {adjective1} {noun1} who liked to {action1}. \n The {adjective1} {noun1} liked to {action1} so much that the {adjective1} {noun1} {action2}. ")


print(f"")
