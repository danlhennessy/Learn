import pdb

# py -m pdb my_program.py  - Debug a program that you dont have write access to

print("Start..")

a = 23

breakpoint()

a = 45

print("Hello World")

# Debug Commands: h: help, w: where, n: next, s: step, c: continue, p: print, l: list, q: quit
# e.g. 'p a' in debugger will print current value of variable a