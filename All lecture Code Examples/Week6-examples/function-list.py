def myFunction(fname, units):
  print(fname + ' needs to study the following units:')
  for x in units:
    print(x) 

unitList = ['COMP6010', 'COMP6200', 'COMP6210']
myFunction('Eric', unitList)
myFunction('Monica', ['COMP8200', 'COMP8210', 'COMP8851'])