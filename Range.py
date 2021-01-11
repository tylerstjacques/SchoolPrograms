def func(lst):
  """ lst contains a list of numbers"""
  if len(lst) == 1:
    return lst[0]
  ret = func(lst[1:])
  if lst[0] < ret:
    return lst[0]
  else:
    return ret


lst=[1,2,3,4,5,-10]
print(func(lst))
