'''
Ths program starts by asking the user to enter the LENGTH of a number string. So, for instance... if the user enters 3 for numberLength (see below), the number generated (using randomInteger) may be 123, 344, 771, etc....

It's a string of digits that, in the example above, has a length of 3.

Of course, the user can enter whatever length he wants.

Then, using the "power" of RECURSION and DICTIONARIES, it spits out a list of unique numbers.

PARAMETERS and FUNCTION(S):
uniqueNumbers: The function that uses dictionaries and recursion to return a unique count.
setrecursionlimit: Imported from sys, this function sets the recursion limit. If you do NOT import this and set the recursion limit, Python uses the default recursion limit of 1,000 (though, when I did it w/o setrecursionlimit, it was around 993 or something like that).
stringifiedDigits: This is the value that is generated based on the numberLength inputted by the user and entered as the first value of uniqueNumbers function.
For each iteration (recursion), that stringified digit is spliced: stringifiedDigits[1::]
dictionary: The dictionary that will be used to get the unique value count. How will we do that? In the end, the count will be generated as len(dictionary.keys()).
'''

def main():
   from random import randint as randomInteger;
   from sys import setrecursionlimit;
   from colorama import init;
   from termcolor import colored;

   setrecursionlimit(93579179); #sets the recursion limit.
   init();

   try:
      numberLength = eval(input("Enter the length of the number string you want to find unique Numbers for: ")); #THIS is what is taking so long. The greater the length of the number string, the longer it takes Python to create those numbers.

      dictTemplate:dict = {};
      stringifiedDigits = "";

      def AddKeysToTemplate(integer):
         dictTemplate[str(integer)] = integer;
         return str(integer);

      '''
      "For Loop" middleware/middle step:
      The bottom for loop "cuts" the randomInteger generating process if the user enters a super large number.

      The bottom for loop will STOP if all 10 unique numbers are found, regardless if the length of strigifiedDigits == numberLength, which was the length the user inputted!!!

      So, for example, if the user enters 93919953 but Python 10 unique numbers (0-9) are generated at, say, the 37th number (len(stringifiedDigits) == 37), then what is the point of going past the 37th number? 

      That will take up space, time and other stuff.
      '''
      for i in range(numberLength): #time saving step. 
         stringifiedDigits+=AddKeysToTemplate(randomInteger(0,9));
         if len(dictTemplate.keys()) > 9:
            print(f"Even though the user entered {numberLength} as the desired length, we were able to fill all 10 unique numbers using {len(stringifiedDigits)} numbers for efficiency and speed.")
            break; #THIS!!! This for loop with the break literally speeds up the process if the user enters like a GAZILLION for numberLength.
      
      def uniqueNumbers(stringifiedDigits=stringifiedDigits, dictionary:dict={}):
         dictionary[stringifiedDigits[0]] = stringifiedDigits[0];

         if len(stringifiedDigits) == 1:
            dictionary[stringifiedDigits] = stringifiedDigits;
            print(f"Final Dictionary Result: {dictionary}.")
            return f"There are {len(dictionary.keys())} unique numbers.";

         elif len(dictionary.keys()) == 10:
            print(f"The stringifiedDigits has ")
            print(f"Final Dictionary Result: {dictionary}.");
            return f"Although there was originally {colored(str(numberLength), 'light_green', attrs=['bold'])} digits inside stringifiedDigits, I did not have to go through all of them.\nInstead, I only spliced out {colored(str((numberLength - len(stringifiedDigits))+1), 'red', attrs=['bold'])} digits b/c the maximum number of unique digits has been reached which is 10."; #This elif condition will prematurely TERMINATE the recursion if all 10 unique numbers are found. I put this condition in to (hopefully) save some time.
      
         elif ("" in dictionary) and (len(dictionary.keys()) == 0):
            return "There are 0 unique numbers.";
      
         return uniqueNumbers(stringifiedDigits[1::]);

      print(uniqueNumbers())

   except ValueError as ve:
      print(f"ValueError: {ve.args[0]} for {ve.args[1]}.");

   except SyntaxError as stx:
      print(f"SyntaxError: {stx.args[0]} for {stx.args[1]}.");
   
   except IndexError as idx:
      print(f"Index out of range error!!! {idx.args[0]} for {idx.args[1]}!!!")

   except Exception as exc:
      print(f"Exception occurred: {exc.args[0]} for {exc.args[1]}.")

main()