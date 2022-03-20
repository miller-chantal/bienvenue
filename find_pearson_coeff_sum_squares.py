# a program to calculate coefficient r using sum cross products - (((sumX)(sumY))/N )
# divided by sqrt (SSx)(SSy) = ((sum(x2) - (sumX2))/N * ((sum(y2) - (sumy2)) / N

import math


number_of_scores = int(input('what is the number of scores? ' ))
sum_xy = float(input('what is the sum of the cross products? ' ))
sum_x = float(input('what is the sum of x?' ))
sum_x_squared = float(input('what is x squared then sum? ' ))
sum_squared_x = float(input('what is sum of x squared? ' ))
sum_y = float(input('what is the sum of y ' ) )
sum_y_squared = float(input('what is y squared then sum? ' ))
sum_squared_y = float(input('what is sum of y squared? ' ))

numerator_coeff = sum_xy - (((sum_x * sum_y) / number_of_scores))
print('the numerator is: ' + str(numerator_coeff))



ss_x_y = (sum_x_squared - (sum_squared_x / number_of_scores)) * (sum_y_squared - (sum_squared_y / number_of_scores))


denominator_coeff = math.sqrt(ss_x_y)


print('the denominator is:' + str(denominator_coeff))
pearson_r = numerator_coeff / denominator_coeff

print('the pearson r coefficient is: ' + str(pearson_r))

coeff_determination = pearson_r ** 2

print('the coefficient of determination is: ' + str(coeff_determination))
 
