print("Hello Community, This is the new beginning in my coding Journey")

# Python internally create an byte code and then it goes to VM.
# Python is interpreted language.
# Byte code is low level and machine independent.
# Byte code is not machine code.
# Here byte code is python specific interpretation.
# cpython is most used and standard implementation of python.
# Other variants of python are jython, IronPython, Stackless,PyPy.
# PVM (Python Virtual Machine) is a Python Interpreter which provides the runtime environment for the execution of python byte code into machine code.
# To access python shell --> $ python3.

import main
print(main.chai("Masala Tea"))
print(main.coffee("Lattee"))

# Here chai and coffe are methods defined in main files.
# IF you make any changes in main then to reload the import use command. 
# from importlib import reload
# reload(main) 