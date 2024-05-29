# textpic
A program to turn a picture into text symbols. 
TECHSTACK: Python, Tkinter, numpy, pillow

The method "shades" renders the picture in several shades. Each symbol represents a certain area of the picture. The symbol is assigned acording to RGB values of the coresponding area. One of five symbols is chosen acording to the average RGB value of pixels in the coresponding area of the picture. The method is better for rendering large pictures (large in text symbols). The method "blocks" has only two shades: black and white, but has a higher resolution because one symbol represents 4 areas of the picture instead of one. One of sixteen symbols is chosen using a binary tree implemented via index of a string. It is better for high contrast pictures and for rendering smaller amount of symbols and has a tendency to make a picture incomprehensible. The method is best reserved for rendering pictures with clear symbols in it, for example text.

The program runs in a Tkinter window and has an interface with multiple settings.
