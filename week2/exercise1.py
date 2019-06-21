"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
# I think this says that "some_words" is the list provided.
some_words = ['what', 'does', 'this', 'line', 'do', '?'] # lists out the stuff within the square brackets
# I think it prints the words in the list "some_words"
for word in some_words:
    print(word) # prints a singular word from the list
# I think it does the same thing?
for x in some_words:
    print(x) # it did the same thing?
# I think it prints the "some_words" list
print(some_words) # it printed the "some_words" list
# I think if the list "some_words" is greater than 3, it'll print that 'some_words contains more than 3 words'
if len(some_words) > 3:
    print('some_words contains more than 3 words') # It printed "some_words contains more than 3 words"
# I think it defines a useful function and prints the list?
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname()) # Ohhh it described my laptop's uhhh 'stuff', cool
# I think.. a??? Useful function?????? what
usefulFunction() #it gave me my code line thing
