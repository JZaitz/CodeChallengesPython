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

#Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.
  def array_front9(nums):
  end = len(nums)
  if end > 4:
    end = 4

  for i in range(end):
    if nums[i] == 9:
      return True
  return False

#Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
  def array123(nums):
  for i in range(len(nums)-2):
   if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
     return True
  return False
