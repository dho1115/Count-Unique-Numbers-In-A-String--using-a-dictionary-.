Using a dictionary and the "power" of recursion, this app counts the number of unique numbers in a string.

NOTE that "power" is in quotes. Sometimes, I wonder if it's any faster than a for loop or with just using set( ) or even list comprehension.

But, that's just me. Oh, well.

UPDATE!!!

See the new comments inside ''' [comment] '''!!!

UPDATE!!!
Renamed file to recursion.py.

UPDATE!!!
I can do this using fromkeys as well.

UPDATE!!!
Inside recursion.py, I added this:

for i in range(numberLength): #time saving step. 
         stringifiedDigits+=AddKeysToTemplate(randomInteger(0,9));
         if len(dictTemplate.keys()) > 9:
            print(f"Even though the user entered {numberLength} as the desired length, we were able to fill all 10 unique numbers using {len(stringifiedDigits)} numbers for efficiency and speed.")
            break;

The above for-loop "short circuits" the random number generating process if 10 unique digits (the max) has been reached. I tried a dictionary comprehension, but it does not work as well.

UPDATE:
The YouTube link: https://youtu.be/R2WnT2rVhqM

