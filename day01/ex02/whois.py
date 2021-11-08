# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: esafar <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/08 12:11:45 by esafar            #+#    #+#              #
#    Updated: 2021/11/08 14:21:07 by esafar           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if (sys.argv[1].isdigit()):
	num = int(sys.argv[1]);
	if len(sys.argv) == 2:
		if (num == 0):
			print('Im zero.');
		elif (num % 2) == 0:
			print('Im even.');
		elif (num % 2) == 1:
			print('Im odd.');
		else:
			print('Error.');
else:
	print('Error....');