  
import statistics
import math
import random

for roll in range(100):
  print(random.randrange(1,101), end=' ')
  print('\nThe population variance for a random dataset of 100 numbers = ',statistics.pvariance(random.randrange(1,101),'\n')
#print('\nThe population standard deviation for the same dataset (using statistic.pstdev) = ',statistics.pstdev([1,3,4,2,6,5,3,4,5,2]),'\n')
#print('\nThe population standard deviation for the same dataset (using math.sqrt & statistic.pvariance to confirm statistic.pstdev) = ',
#      math.sqrt(statistics.pvariance([1,3,4,2,6,5,3,4,5,2])),'\n')     
#if statistics.pstdev([1,3,4,2,6,5,3,4,5,2]) == math.sqrt(statistics.pvariance([1,3,4,2,6,5,3,4,5,2])):
#  print('\nConfirmed math.sqrt & statistic.pvariance is = to statistic.pstdev.\n\n')
#else:
#  print('\nNot equal.\n\n')
