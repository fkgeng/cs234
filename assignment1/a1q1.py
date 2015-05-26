
#empty list to store all valid input values
my_input_list=[]

#keep reading from input() until "END" is met
while True:            
    my_input=input() 
    if my_input!= "END":       
        my_input_list=my_input_list+my_input.split() 
    else:
    	break

#match vechcle type to its rate
price_list={"VEHICLE":0.25,"TRUCK":1.333,"MOTORCYCLE":0.17}

#empty dictionary to store plate numbers vs. their cost
#this dictionary will be used as final ouput
my_dic={}

counter=0
while (counter <=len(my_input_list)-2):
	#if the plate number has never seen before
	if not my_input_list[counter] in my_dic.keys():
		my_dic[my_input_list[counter]]=eval(my_input_list[counter+2])*price_list[my_input_list[counter+1]]
	#if the plate number has seen
	else:
		my_dic[my_input_list[counter]]=my_dic[my_input_list[counter]]+eval(my_input_list[counter+2])*price_list[my_input_list[counter+1]]
	counter+=3

#sort dictionary keys in descending order by values
for plate_number in sorted(my_dic,key=my_dic.get,reverse=True):
	#print output in required format
	print ("%s: %s" % (plate_number, my_dic[plate_number]))
