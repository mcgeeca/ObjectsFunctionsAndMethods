"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Craig McGee Jr..
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()

def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # TODO: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------
    window = rg.RoseWindow()
    Point1 = rg.Point(100,100)
    Point2 = rg.Point(200,200)
    Circle1 = rg.Circle(Point1, 20)
    Circle2 = rg.Circle(Point2, 10)
    Circle2.fill_color = "green"
    Circle1.attach_to(window)
    Circle2.attach_to(window)
    window.render()
    window.close_on_mouse_click()

def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------
    window = rg.RoseWindow()
    center_of_circle = rg.Point(100,150)
    rectangle = rg.Rectangle(corner_1 = rg.Point(200, 120), corner_2 =
    rg.Point(120, 200))
    center_of_rectangle = rectangle.get_center()
    circle = rg.Circle(center_of_circle, 5)
    circle.fill_color = "blue"
    circle.attach_to(window)
    rectangle.attach_to(window)
    window.render()
    print(circle.outline_thickness)
    print(circle.fill_color)
    print(circle.center)
    print(center_of_circle.x)
    print(center_of_circle.y)
    print(rectangle.outline_thickness)
    print(rectangle.fill_color)
    print(center_of_rectangle)
    print(center_of_rectangle.x)
    print(center_of_rectangle.y)
    window.close_on_mouse_click()

def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    # ------------------------------------------------------------------
    window = rg.RoseWindow()
    line_1 =rg.Line(rg.Point(100, 300), rg.Point(200, 400))
    line_2 = rg.Line(rg.Point(100, 200), rg.Point(300, 400))
    line_2.thickness = 5
    line_2.attach_to(window)
    line_1.attach_to(window)
    window.render()
    center_of_line = line_2.get_midpoint()
    print(center_of_line)
    print(center_of_line.x)
    print(center_of_line.y)
    window.close_on_mouse_click()

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
