#Matthew Golab
#V2.0 This program had two major changes during its lifespan
#This program is written to solve programming excercise 4-15, in which the author of the book asks us to print out a rough triangle of "#"s.
#The goal is to use two four loops to accomplish this task
#
#
#
#first off, we will collect an interger from the user to determine how many times to run the program to get the desired output
userInput = int(input("Please enter a number for the size of the pattern "))

#this first loop overall will run the number of times specified by the user. it also adds each "#" at the end of the spaces generated by the second loop
for i in range(userInput):
    print('#', end='')
#this loop generates spaces after the first # and adds one per line to achieve the desired effect.
    for x in range(i):
        print(' ', end='')
        
        
    print('#')
        
        
        
    



    
