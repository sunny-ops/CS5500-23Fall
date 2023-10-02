**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 2

<hr>
**Use Case**: Change Drawing Color

**Primary Actor**: User

**Goal in Context**: change the color of the drawing tool in the mini-paint application by pressing number keys 1 through 8.

**Preconditions**: The mini-paint application is open and functional.

**Trigger**: User presses one of the number keys from 1 to 8.

**Scenario**:

1. User decides to change color of their drawing tool
2. User presses the appropriate number key corresponding to their desired color.
3. The system recognizes the keypress event.
4. The system updates the current drawing color based on the key pressed.

**Exceptions**: If the user presses a number key outside of the range 1-8, the color does not change and a soft alert might notify the user of the valid range.

**Priority**: Medium

**When available**: First release of the mini-paint application*

**Channel to actor**: Direct input through the keyboard

**Secondary Actor**: N/A

**Channels to Secondary Actors**: N/A

**Open Issues**: *How the system handle keypress events outside the valid range

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
