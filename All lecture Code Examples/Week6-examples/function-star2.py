def myFunction(*units):
  for x in units:
    print(x) 

print("6000-level Essential Units in M of DS:")
myFunction('STAT6110', 'STAT6175', 'COMP6200', 'COMP6210') # 4 elements
print("8000-level Essential Units in M of DS:")
myFunction('COMP8210', 'COMP8220', 'STAT8111', 'STAT8121', 'COMP8851') # 5 elements