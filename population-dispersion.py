import statistics
import math
print('\nThe population variance for dataset (1, 3, 4, 2, 6, 5, 3, 2, 5, 2) = ',statistics.pvariance([1,3,4,2,6,5,3,4,5,2]),'\n')
print('\nThe population standar deviation for the same dataset (using statistic.pstdev) = ',statistics.pstdev([1,3,4,2,6,5,3,4,5,2]),'\n')
print('\nThe population standar deviation for the same dataset (using math.sqrt & statistic.pvariance to confirm statistic.pstdev) = ',
      math.sqrt(statistics.pvariance([1,3,4,2,6,5,3,4,5,2])),'\n')     
if statistics.pstdev([1,3,4,2,6,5,3,4,5,2]) == math.sqrt(statistics.pvariance([1,3,4,2,6,5,3,4,5,2])):
  print('\nConfirmed math.sqrt & statistic.pvariance is = to statistic.pstdev.\n\n')
else:
  print('\nNot equal.\n\n')

