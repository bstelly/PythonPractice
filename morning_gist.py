'''Write a program to ask the user to enter a string of characters and find its length.
Then provide the following information about this string:
a.
Print the uppercase letters (if any) in the string
b.
Print every 2nd character in the string
c.
Print the string with all vowels replaced by an underscore
and count/print the number of vowels'''

MY_STRING = raw_input("Please input a string \n")
print "\n"
LENGTH = len(MY_STRING)
print "The string contains",
print LENGTH,
print "characters\n"
print "Uppercase letters in string: ",
COUNTER = 0
for i in range(0, LENGTH):
    for j in range(65, 91):
        if MY_STRING[i] is chr(j):
            print chr(j),
            COUNTER += 1
if COUNTER is 0:
    print "None"
print "\n"
print "Every second character in string: ",
SECOND_CHR = 1
while SECOND_CHR < LENGTH:
    print MY_STRING[SECOND_CHR],
    SECOND_CHR += 2
print "\n"
print "All vowels replaced by underscore: ",
VOWELS = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
SECOND_COUNTER = 0
for i in range(0, LENGTH):
    if VOWELS.__contains__(MY_STRING[i]):
        SECOND_COUNTER += 1
for i in range(0, LENGTH):
    if VOWELS.__contains__(MY_STRING[i]):
        MY_STRING = MY_STRING.replace(MY_STRING[i], chr(95))
print MY_STRING
print "Number of vowels: ",
print SECOND_COUNTER
print "\n"
