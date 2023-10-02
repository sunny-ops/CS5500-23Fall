**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 4

<hr>
**Use Case**: Draw on Canvas with Mouse Drag

**Primary Actor**: User

**Goal in Context**: To simulate the action of drawing with a pencil, enabling the user to freely draw on the canvas by pressing and dragging the mouse.

**Preconditions**: The mini-paint application is open and a color is selected for drawing

**Trigger**: User presses the left mouse button over the canvas area and starts dragging

**Scenario**: 

1. User positions the mouse pointer over the desired starting point on the canvas.
2. User presses the left mouse button without releasing it.
3. As the mouse is dragged, the system continually changes the pixel color under the mouse pointer to the currently selected color.
4. The user draws desired patterns, shapes, or lines by moving the mouse while keeping the left button pressed.
5. The user releases the mouse button to stop drawing.

**Exceptions**: If no color has been selected for drawing, the system might either not draw or could prompt the user to select a drawing color first.

**Priority**: Medium

**When available**: First release

**Channel to actor**: Mouse and GUI

**Secondary Actor**: N/A

**Channels to Secondary Actors**: N/A

**Open Issues**: How should the application handle rapid mouse movements?

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
