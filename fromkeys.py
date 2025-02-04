'''
Ths program starts by asking the user to enter the LENGTH of a number string. So, for instance... if the user enters 3 for numberLength (see below), the number generated (using randomInteger) may be 123, 344, 771, etc....

It's a string of digits that, in the example above, has a length of 3.

Of course, the user can enter whatever length he wants.

Then, using .fromkeys(), which is a dict method, it will generate a list of unique numbers.
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

      stringifiedDigits = "".join([str(randomInteger(0, 9)) for i in range(numberLength)]);

      uniqueNumberCount = lambda stringifiedDigits=stringifiedDigits: len(dict.fromkeys(",".join(stringifiedDigits).split(","), 0))

      print(uniqueNumberCount())

   except ValueError as ve:
      print(f"ValueError: {ve.args[0]} for {ve.args[1]}.");

   except SyntaxError as stx:
      print(f"SyntaxError: {stx.args[0]} for {stx.args[1]}.");

   except Exception as exc:
      print(f"Exception occurred: {exc.args[0]} for {exc.args[1]}.")

main()