# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: esafar <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/08 17:23:20 by esafar            #+#    #+#              #
#    Updated: 2021/11/08 17:23:22 by esafar           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

langage = {'Python': 'Guido van Rossum', 'Ruby': 'Yukihiro Matsumoto', 'PHP': 'Rasmus Lerdorf', '~/Source code': 'Ethan Safar'}

for c, founder in langage.items():
    print(c, 'was created by', founder)