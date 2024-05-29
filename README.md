# textpic
A program to turn a picture into text symbols. 
TECHSTACK: Python, Tkinter, numpy

The method "shades" renders the picture in several shades. Each symbol represents a certain area of the picture. The symbol is assigned acording to RGB values of the coresponding area. The method is better for rendering large pictures. The function "blocks" has only two shades: black and white, but has a higher resolution because one symbol represents 4 areas of the picture instead of one. It is better for high contrast pictures and for rendering smaller amount of symbols and has a tendency to make a picture incomprehensible. The method is best reserved for rendering pictures with clear symbols in it, for example text.
The program runs in a Tkinter window and has an interface with multiple settings.
