The Tower of Hanoi is a classic problem in computer science and mathematics. The objective is to move a set of disks from one pole to another, subject to the following constraints:

Only one disk can be moved at a time.

A disk can only be placed on top of a larger disk or an empty pole.

The disks are initially stacked on one of the poles in decreasing size, with the largest disk at the bottom.

You have three poles to use for the transfer.

The goal is to move all the disks from the starting pole (let's say Pole A) to the destination pole (Pole C), using the third pole (Pole B) as an auxiliary. The challenge is to perform the task using the minimum number of moves and adhering to the constraints.

Application Overview:
Create an interactive application using Tkinter that visually demonstrates the solution to the Tower of Hanoi problem. The application should:

Allow users to choose the number of disks (1 to 10).

Visualize the initial state of the Tower of Hanoi puzzle, with the disks stacked on the first pole.

Provide step-by-step movement of the disks, with each move following the classic Tower of Hanoi algorithm.

Enable users to navigate through the sequence of moves using Next and Previous buttons to see how the puzzle is solved.

Display the list of moves in a scrollable text box, showing the move sequence (e.g., "Move disk from pole 1 to pole 3").

Use colors to differentiate between disks for better visualization.

Optionally, animate the movement of the disks to provide a more engaging user experience.

Functional Requirements:
Canvas: A graphical representation of three poles and a set of disks that can be moved.

Step-by-Step Navigation: The ability to move through the steps of the solution using Previous and Next buttons.

Move List Display: A text box that shows each move as the disks are transferred between poles.

Recursive Solution: Implement the recursive algorithm for solving the Tower of Hanoi problem, storing the moves in a list and updating the visual state accordingly.

Disk Visualization: The disks should be represented with varying sizes and colors for easy distinction.

User Interface: A user-friendly interface with buttons and a scrollable text box to control the solution and view the move sequence.

Constraints:
The user can choose the number of disks between 1 and 10.

The solution must display the step-by-step moves in an easily readable format.

The program should handle the graphical rendering efficiently for real-time visualization.

