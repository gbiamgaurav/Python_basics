

import os
import sys
import pandas as pd
import numpy as np

class Greeter:
    def greet(self):
        print("Hi there!")

def hello_world():
    var = 123
    var2 = 123+36
    var3 = var2+var
    message = "Hello World!"
    greeter = Greeter()
    greet_func = getattr(greeter, "greet")
    greet_func()

if __name__ == "__main__":
    hello_world()            