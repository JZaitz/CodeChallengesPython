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

#Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
def hello_name(name):
  return "Hello %s!" % name

#Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".
def make_abba(a, b):
  return a + b + b + a


#The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".
def make_tags(tag, word):
  return "<" + tag + ">" + word + "</" + tag + ">"


#Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".


def make_out_word(out, word):
  outb = out[:2]
  oute = out[2:]
  return outb + word + oute


#Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.
def extra_end(str):
  end = str[-2:]
  return end * 3


#Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".
def first_two(str):
  end = str[:2]
  if len(str) >= 2:
    return end
  else:
    return str[:1]

#Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
def first_half(str):
  midpoint = len(str)/2
  return str[:midpoint]

#Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.
def without_end(str):
  return str[1:-1]

#Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).
def combo_string(a, b):
  alen = len(a)
  blen = len(b)
  if alen > blen:
    return b + a + b
  elif blen > alen:
    return a + b + a

#Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.
def non_start(a, b):
  return a[1:] + b[1:]

#Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.
def left2(str):
  beg = str[:2]
  end = str[2:]
  return end + beg

#Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.
def non_start(a, b):
  newa = a[1:]
  newb = b[1:]
  return newa + newb

#Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.
def extra_end(str):
  end = str[-2:]
  return end * 3

#Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".
def first_two(str):
  if len(str) >= 2:
    newstr = str[:2]
    return newstr
  elif len(str) == 1:
    return str
  else:
    return str

#Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
def first_half(str):
  fhalf = len(str)/2
  return str[:fhalf]

#Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.
def without_end(str):
  return str[1:-1]
