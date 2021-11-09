# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: esafar <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/09 14:51:41 by esafar            #+#    #+#              #
#    Updated: 2021/11/09 14:51:43 by esafar           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---',
		    'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---',
		    'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--',
		    'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....',
		    '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----',
		    ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def encrypt(message):
	crypted_str = ''
	for letter in message:
		if letter != ' ':
			crypted_str += MORSE_CODE_DICT[letter]
		else:
			crypted_str += ' / '
	return crypted_str
 
if len(sys.argv) > 1:
	output = ""
	i = 1
	check = 0
	for i in range (len(sys.argv)-1):
		for letter in sys.argv[i+1]:
			if letter == '/':
				check = 1
				break
		if check == 1:
			break
		elif check != 1:
			if i == 0:
				output += encrypt(str(sys.argv[i+1]).upper())
			else:
				output += ' / ' + encrypt(str(sys.argv[i+1]).upper())
	if check == 1:
		output = 'Error.'
	print(output)