#------------------------------------------------------------------------------
#  Copyright (c) 2012, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
""" Driver for the spiral plot example.

The window will show an Enable Component on the left with a spiral. The right 
side of the window will show several sliders that control the parameters
of the spiral drawing. The drawing will update whenever the slider values
change.

This demo requires numpy and Enable.

"""
import enaml

def main():
    from spiral_canvas import SpiralCanvas
    SpiralCanvas.activate()

    with enaml.imports():
        from spiral_plot import SpiralWindow

    window = SpiralWindow()
    window.show()


if __name__ == '__main__':
    main()

