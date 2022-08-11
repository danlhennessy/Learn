import pdb

# py -m pdb my_program.py  - Debug a program that you dont have write access to

print("Start..")

a = 23

breakpoint()  # Debugger stops here until next is input

a = 33
a = 45

print("Hello World")

breakpoint()

# Debug Commands: h: help, w: where, n: next line, s: step (Into function), c: continue (until next breakpoint), p: print, l: list, q: quit
# e.g. 'p a' in debugger will print current value of variable a