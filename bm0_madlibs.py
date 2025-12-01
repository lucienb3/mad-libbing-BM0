from numpy import random

rndstory = random.randint(1,3)
print(rndstory)



if rndstory == 1:
	adjective1 = input("write a adjective: ")
	noun1 = input('write a noun: ')
	action1 = input('write a present tense action: ')
	action2 = input('write a past tense action: ')
	print(f"once opon a time there was a {adjective1} {noun1} who liked to {action1}. \n The {adjective1} {noun1} liked to {action1} so much that the {adjective1} {noun1} {action2}. ")




if rndstory == 2:
	adjective1 = input("write a adjective: ")
	noun1 = input("write a noun: ")
	adjective2 = input("write a adjective: ")
	animal1 = input("write an animal: ")
	verb1 = input("write a verb: ")
	emotion1 = input("write a emotion1: ")
	print(f"Today, I decided to visit the park to enjoy the beautiful {adjective1} weather. I packed my {noun1} and headed out. On the way, I saw a {adjective2} {animal1} {verb1} down the street. It looked very {emotion1}")