import random

frequency1 = 0
frequency2 = 0
frequency3 = 0
frequency4 = 0
frequency5 = 0
frequency6 = 0
frequency7 = 0
frequency8 = 0
frequency9 = 0
frequency10 = 0
frequency11 = 0
frequency12 = 0

trials = 6_000

for roll in range(trails):
  face = random.randrange(1,7) + randomg.randrange(1,7)
  if face == 1:
    frequency1 += 1
  elif face == 2:
    frequency2 += 1
  elif face == 3:
    frequency3 += 1
  elif face == 4:
    frequency4 += 1
  elif face == 5:
    frequency5 += 1
  elif face == 6:
    frequency6 += 1
  elif face == 7:
    frequency7 += 1
  elif face == 8:
    frequency8 += 1
  elif face == 9:
    frequency9 += 1
  elif face == 10:
    frequency10 += 1
  elif face == 11:
    frequency11 += 1
  elif face == 12:
    frequency12 += 1
    
print(f'Face{"Frequency":>13}')
print(f'{1:4}{Frequency1:>13}')
print(f'{2:4}{Frequency2:>13}')
print(f'{3:4}{Frequency3:>13}')
print(f'{4:4}{Frequency4:>13}')
print(f'{5:4}{Frequency5:>13}')
print(f'{6:4}{Frequency6:>13}')  
print(f'{7:4}{Frequency7:>13}')
print(f'{8:4}{Frequency8:>13}')
print(f'{9:4}{Frequency9:>13}')  
print(f'{10:4}{Frequency10:>13}')
print(f'{11:4}{Frequency11:>13}')
print(f'{12:4}{Frequency12:>13}')
      
craps = frequency2 + frequency3 + frequency12
wins = frequency7 + frequency11
print('\nFraction of the time rolling craps = ', craps/trails)
print('Fraction of time rolling wins =', wins/trails)
  
  
