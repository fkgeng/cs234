

#specify the board size here
fixed_size=13

#read the board
my_input=input()
#convert the board from string to list of charaters
my_input_list=list(my_input)
#modified the original list to list of list. Each inner list represents a row on the board
horizontal=[my_input_list[i:i+fixed_size] for i in range(0, len(my_input_list), fixed_size)]
#list of list, containing information for left side, right side, left diagonal and right diagonal characters.
vertical_and_diagonal=[[],[],[],[]]

#if_win: list of list of character -> none
#define the function to check if a player wins the game
def if_win(lol):
	for alist in lol:
		if all(item=="x" for item in alist):
			print("Player x won.")
		if all(item=="o" for item in alist):
			print("Player o won.")

#populate: none -> none
#purpose: populate the vertical_and_diagonal list based on the characters on the board. 
def populate():
	counter=0
	for item in horizontal:
		#left side
		vertical_and_diagonal[0]=vertical_and_diagonal[0]+list(item[0])
		#right side
		vertical_and_diagonal[1]=vertical_and_diagonal[1]+list(item[fixed_size-1])
		#right diagonal
		vertical_and_diagonal[2]=vertical_and_diagonal[2]+list(item[counter])
		#left diagonal
		vertical_and_diagonal[3]=vertical_and_diagonal[3]+list(item[fixed_size-counter-1])
		counter+=1

#run the process
populate()
if_win(horizontal)
if_win(vertical_and_diagonal)
