"""
language: python3
description: To draw uniform stairway
"""
import turtle
#import sys

#length is the length of the single side of the stair
length=1

#It prompts the user to enter the total number of steps which should be even
total_steps=int(input("Enter total number of steps(even)"))

# total_steps_div saves the half of total_steps
total_steps_div=total_steps//2

def init_uniform(total_steps):
    """Initialize the world coordinates and draw labels.
       The lower left is (-1,-1) and the upper right is computed based on the total number of steps.
       Preconditions:
                       turtle position x,y: (0,0)
                       turtle is facing east
                       turtle pen is up
       Postcondition:
                       Writes Iterative and Recursive on the screen for the line segments to be drawn
                       with those methods
                       turtle is facing east
                       turtle pen is up
       :param total_steps: a non-negative, even value for the total number of steps
       :return: None
    """
    turtle.title("Uniform Stairs")
    turtle.setworldcoordinates(-1,-1, total_steps*2+2, total_steps*2+2)
    turtle.pensize(3)
    turtle.up()
    turtle.setpos(0,(total_steps//2)+1)
    turtle.down()
    turtle.write("Iterative",font=("Arial",20,"bold"))
    turtle.up()
    turtle.setpos(total_steps+1, (total_steps//2)+1)
    turtle.down()
    turtle.write("Recursive",font=("Arial",20,"bold"))
    turtle.up()
    turtle.home()


def drawStairsIter(total_steps):
    """
        Takes in total_steps and draws the uniform stairs iteratively.
        :param total_steps: represents number of stair segments
        Preconditions:
                        turtle is facing east
                        turtle pen is up
        Postcondition:
                        According to the for loops, it draws the stairs
                        turtle is facing east
                        turtle pen is up
        :return: None
    """

    #It checks whether the user has given even number of steps and determines the action accordingly
    if total_steps%2==0 and total_steps>0:
        turtle.down()

        #This for loop will draw the stairs of left side i.e the uphill stairs
        for i in range(total_steps//2):
            turtle.left(90)
            turtle.forward(length)
            turtle.right(90)
            turtle.forward(length)

        # This for loop will draw the stairs of right side i.e the downhill stairs
        for i in range(total_steps//2):
            turtle.forward(length)
            turtle.right(90)
            turtle.forward(length)
            turtle.left(90)
        turtle.up()
        turtle.forward(length)
        #turtle.exitOnClick()

    #Incase the user has not given even number of stair segments, then
    #It will tell the user about the kind of input expected.
    else:
        print("Invalid input. Total steps should be a non-negative, even integer")


def drawStairsRec(total_steps):
    """
            Takes in total_steps and draws the uniform stairs recursively.
            :param total_steps: represents number of stair segments
            Preconditions:
                            turtle is facing east
                            turtle pen is up
            Postcondition:
                            According to the recursive conditions, it draws the stairs
                            turtle is facing east
                            turtle pen is down
            :return: None
    """
    turtle.down()

    #Base Case: It checks whether the total_steps is less than or equal to its half
    if total_steps<=total_steps_div:
        return None

    # If the total_steps is not less than or equal to its half, Then it performs the following commands
    else:
        turtle.left(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        drawStairsRec(total_steps-1)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.left(90)


def computeLength(segments,length):
    """
               Computes the total length of all the stair segments
               :param segments(int): The number of stair segments
               :param length(int): The length of a single side of the stair
               Preconditions:
                               segments>=0
                               length>0
               Postcondition:
                               segments>=0
                               length>0
               :return: Total Length
    """

    #Base Case: It checks whether the segments is equal to 0.
    #If, it is, it returns 0
    if segments==0:
        return 0

    #If the segments is not 0, Then it performs the following recursive function
    else:
        return (length*2)+ computeLength(segments-1,length)

def main():
    """
           Preconditions: None
           Postcondition: calls init_uniform() and passes the required parameters along with it
                       calls drawStairsIter() and passes the required parameters along with it
                       calls drawStairsRec() and passes the required parameters along with it
                       calls computeLength() and passes the required parameters along with it and prints the answer accordingly.
           :return: None
    """

    init_uniform(total_steps)
    drawStairsIter(total_steps)
    drawStairsRec(total_steps)
    print("Total uniform stair length(iterative):",computeLength(total_steps,length))
    print("Total uniform stair length(recursive):", computeLength(total_steps, length))
    #It pauses for the user to hit enter to close
    turtle.mainloop()
    input("Hint enter to close....")

if __name__=='__main__':
    #main() is called
    main()