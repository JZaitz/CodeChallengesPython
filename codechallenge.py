#Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

def string_bits(str):
  newstr = ""
  for i in range(0,len(str)):
    if i % 2 == 0:
      newstr = newstr + str[i]
  return newstr

#Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
  newstr = ""
  numtimes = len(str) + 1
  for i in range (1, numtimes):
    newstr = newstr + str[0:i]
  return newstr

#Given an array of ints, return the number of 9's in the array.

def array_count9(nums):
  counter = 0
  for i in range(0,len(nums)):
    if nums[i] == 9:
      counter = counter + 1
  return counter
