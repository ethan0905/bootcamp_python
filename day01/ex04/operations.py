# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: esafar <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/08 16:50:59 by esafar            #+#    #+#              #
#    Updated: 2021/11/08 16:51:01 by esafar           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) == 3:
    if sys.argv[1].isdigit() and sys.argv[2].isdigit():
        n1 = int(sys.argv[1]);
        n2 = int(sys.argv[2]);

        print('Sum:        ', n1 + n2)
        print('Difference: ', n1 - n2)
        print('Product:    ', n1 * n2)
        if n2 == 0:
            print('Quotient:    ERROR (div by zero)')
            print('Remainder:   ERROR (modulo by zero)')
        else:
            print('Quotient:   ', n1 / n2)
            print('Remainder   ', n1 % n2)
    else:
        print('InputError: numbers only')
        print('Usage: python3 operations.py <number1> <number2>')
        print('Example:')
        print('    python3 operations.py 10 3')
elif len(sys.argv) > 3:
    print('InputError: too many arguments')
    print('Usage: python3 operations.py <number1> <number2>')
    print('Example:')
    print('    python3 operations.py 10 3')
else:
    print('Usage: python3 operations.py <number1> <number2>')
    print('Example:')
    print('    python3 operations.py 10 3')

