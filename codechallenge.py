#Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

def string_bits(str):
  newstr = ""
  for i in range(0,len(str)):
    if i % 2 == 0:
      newstr = newstr + str[i]
  return newstr
