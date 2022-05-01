def myFunction(fname, *units):
  print(fname + ' needs to study the following units:')
  for x in units:
    print(x) 
  print(units[0] + ' is the first unit')


myFunction('Mike', 'COMP6010', 'COMP6200', 'COMP6210')