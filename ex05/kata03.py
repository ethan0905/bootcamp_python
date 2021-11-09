# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata03.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: esafar <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/08 18:12:51 by esafar            #+#    #+#              #
#    Updated: 2021/11/08 18:12:52 by esafar           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

phrase = "The right format"

output = ''
size = len(phrase)
for i in range (42-size):
    output = output + '-'
print(output + phrase)
