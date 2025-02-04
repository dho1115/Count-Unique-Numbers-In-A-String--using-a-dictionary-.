from random import randint as randomInteger;
from sys import setrecursionlimit;

setrecursionlimit(979531); #sets the recursion limit.

try:
   numberLength = eval(input("Enter the length of the number string you want to find unique Numbers for: "));
   stringifiedDigits = "".join([str(randomInteger(0, 9)) for i in range(numberLength)]);

   def uniqueNumbers(stringifiedDigits=stringifiedDigits, dictionary:dict={}):
      dictionary[stringifiedDigits[0]] = stringifiedDigits[0];
      if len(stringifiedDigits) == 1:
         dictionary[stringifiedDigits] = stringifiedDigits;
         print(f"Final Dictionary Result: {dictionary}")
         return len(dictionary.keys());
   
      if ("" in dictionary) and (len(dictionary.keys()) == 0):
         return 0;
   
      return uniqueNumbers(stringifiedDigits[1::]);

   print(uniqueNumbers())

except ValueError as ve:
   print(f"ValueError: {ve.args[0]} for {ve.args[1]}.");

except SyntaxError as stx:
   print(f"SyntaxError: {stx.args[0]} for {stx.args[1]}.");

except Exception as exc:
   print(f"Exception occurred: {exc.args[0]} for {exc.args[1]}.")