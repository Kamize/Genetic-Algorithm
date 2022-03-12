import math
from tkinter import Y

# heuristic equation
def h(x,y) :
    hasil = pow((math.cos(x) + math.sin(y)),2) / pow(x,2)+pow(y,2)
    return hasil

def main():
    x = 10
    y = 5
    print(h(x,y))

main()