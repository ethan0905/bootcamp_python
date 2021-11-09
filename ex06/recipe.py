# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: esafar <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/08 18:55:33 by esafar            #+#    #+#              #
#    Updated: 2021/11/08 18:55:34 by esafar           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

cookbook = {
	'sandwich': {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'], 'meal' : 'lunch', 'prep_time' : 10},
	'cake': {'ingredients': ['flour', 'sugar', 'eggs'], 'meal' : 'dessert', 'prep_time' : 60},
	'salad': {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'], 'meal' : 'lunch', 'prep_time' : 15}
}

print('Please select an option by typing the corresponding number:')
print(' ')
print('2: Delete a recipe')
print('3: Print a recipe')
print('4: Print the cookbook')
print('5: Quit')
			
# def board():
# 	print('Please select an option by typing the corresponding number:')
# 	print(' ')
# 	print('2: Delete a recipe')
# 	print('3: Print a recipe')
# 	print('4: Print the cookbook')
# 	print('5: Quit')

def print_recipe(name):
	s = str(name)
	i = str(cookbook[s]['ingredients'])
	d = str(cookbook[s]['meal'])
	m = str(cookbook[s]['prep_time'])
	print "Recipe for " + s + ":"
	print "Ingredients list: " + i
	print "To be eaten for " + d + "."
	print "Takes " + m + " minutes of cooking."
	print "..."

def print_cookbook():
	print "All recipe from cookbook:"
	for key in cookbook.keys():
		print "- " + key

def remove_recipe(name):
	s = str(name)
	cookbook.pop(s)

# def add_recipe(name):
# 	s = str(name)
# 	i = str(ingredients)
# 	m = str(meal)
# 	p = str(prep_time)
# 	cookbook[s] = "ethan"

# number = 0
# while number != -1:
# 	board();
# 	number = int(input(">> "))
# 	if number == 5:
# 		print(' ')
# 		print('Cookbook closed.')
# 		number == -1;
# 	elif number == 4:
# 		print ("All recipe from cookbook:")
# 		for key in cookbook.keys():
#  			print ("- " + key)
# 	print(' ')