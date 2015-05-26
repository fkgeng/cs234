
#read from input, convert all characters into lower cases
my_input=input().lower()
#convert the board from string to list of charaters
my_input_list=list(my_input)

#remove_dash: list of list of character -> list of list of character
#purpose: define the function which will go through a list of characters and ignore any dashes
def remove_dash(alist):
	new_list=[]
	for character in alist:
		if character != "-":
			new_list.append(character)
	return new_list

#create a new list which exclude any dashes
modified_list=remove_dash(my_input_list)

#determine the size of the list
list_length=len(modified_list)

#compare left side with the right side. Compare each pair. 
counter=0
while counter<=list_length//2:
	if modified_list[counter]!=modified_list[list_length-counter-1]:
		#if it does not match for any given pair, return no and end the script
		print ("no")
		quit()
	counter+=1
#if all pairs match, then return yes
print("yes")

