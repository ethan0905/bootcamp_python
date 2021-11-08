# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: esafar <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/08 14:42:19 by esafar            #+#    #+#              #
#    Updated: 2021/11/08 14:42:21 by esafar           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import string
import sys

def text_analyzer(sentence):
        print('Error.')
    a = int(0);
    b = int(0);
    c = int(0);
    d = int(0);
    e = int(0);

    for i in range (len(sentence)):
        if (sentence[i].isupper()):
            a = a + 1;
        elif (sentence[i].islower()):
            b = b + 1;
        elif (sentence[i] == '!' or sentence[i] == '?' or sentence[i] == '.' or sentence[i] == '#' or sentence[i] == '%' or sentence[i] == '$' or sentence[i] == '*' or sentence[i] == '^'):
            c = c + 1;
        elif (sentence[i].isdigit()):
            d = d + 1;
        elif (sentence[i] == ' '):
            e = e + 1;
    print('The text contains ', i,' characteres:')
    print('- ', a, 'upper letter')
    print('- ', b, 'min letter')
    print('- ', c, 'punctuation marks')
    print('- ', e, 'spaces')