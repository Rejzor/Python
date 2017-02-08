'''Exercise: user provide a odd number of last floor of tree. Program should draw tree by using characters like "#" '''

last_floor = int(input("Please provide lenght of last floor of tree: "))
how_spaces = int(last_floor/2) # It's a idea to get number of spaces. For example last floor looks like ####### -> 7/2 = 3.5 we need only first part of that number mean 3. So first floor # gets 3 spaces second floor ### gets 2 spaces ###### gets 1 spaces and last one ####### gets 0 spaces.
for i in range(1,last_floor+1,2): # We just start from 1 and in next interation we jumpt to 3, then to 5. We need that +1 because without it we miss one interation.
	print(how_spaces * " " + i * "#" + how_spaces * " ")
	how_spaces = how_spaces -1

     #
    ###
   #####
  #######
 #########
###########