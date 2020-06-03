> # README

---
![readme](https://img.shields.io/badge/readme-OK-green.svg?colorB=00C106)
---
> ### Python Scripts

Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file at the root of the holbertonschool-higher_level_programming repo, containing a description of the repository
A README.md file, at the root of the folder of this project, is mandatory
Your code should use the PEP 8 style (version 1.7.*)
All your files must be executable
The length of your files will be tested using wc
---


> ### Shell Scripts
Allowed editors: vi, vim, emacs
All your scripts will be tested on Ubuntu 14.04 LTS
All your scripts should be exactly two lines long (wc -l file should print 2)
All your files should end with a new line
The first line of all your files should be exactly #!/bin/bash
All your files must be executable
---

> ### C Scripts

Allowed editors: vi, vim, emacs
All your files will be compiled on Ubuntu 14.04 LTS
Your programs and functions will be compiled with gcc 4.8.4 using the flags -Wall -Werror -Wextra and -pedantic
All your files should end with a new line
Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
You are not allowed to use global variables
No more than 5 functions per file
In the following examples, the main.c files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own main.c files at compilation. Our main.c files might be different from the one shown in the examples
The prototypes of all your functions should be included in your header file called lists.h
Don’t forget to push your header file
All your header files should be include guarded

---

> ### 0. Lookup mandatory
Write a function that returns the list of available attributes and methods of an object:

Prototype: def lookup(obj):
Returns a list object
You are not allowed to import any module
---


> ### 1. My list mandatory
Write a class MyList that inherits from list:

Public instance method: def print_sorted(self): that prints the list, but sorted (ascending sort)
You can assume that all the elements of the list will be of type int
You are not allowed to import any module
---

> ### 2. Exact same object mandatory
Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.

Prototype: def is_same_class(obj, a_class):
You are not allowed to import any module
---

> ### 3. Same class or inherit from mandatory
Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.

Prototype: def is_kind_of_class(obj, a_class):
You are not allowed to import any module
---

> ### 4.  Only sub class of mandatory
Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.

Prototype: def inherits_from(obj, a_class):
You are not allowed to import any module
---

> ### 5. Geometry module mandatory
Write an empty class BaseGeometry.

You are not allowed to import any module
---


> ### 6.  Improve Geometry mandatory
Write a class BaseGeometry (based on 5-base_geometry.py).

Public instance method: def area(self): that raises an Exception with the message area() is not implemented
You are not allowed to import any module
---

> ### 7.Write a class BaseGeometry (based on 6-base_geometry.py).

Public instance method: def area(self): that raises an Exception with the message area() is not implemented
Public instance method: def integer_validator(self, name, value): that validates value:
you can assume name is always a string
if value is not an integer: raise a TypeError exception, with the message <name> must be an integer
if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0
You are not allowed to import any module

> ### 8. Rectangle mandatory
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).

Instantiation with width and height: def __init__(self, width, height):
width and height must be private. No getter or setter
width and height must be positive integers, validated by integer_validator
---

> ### 9. Full rectangle mandatory
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)

Instantiation with width and height: def __init__(self, width, height)::
width and height must be private. No getter or setter
width and height must be positive integers validated by integer_validator
the area() method must be implemented
print() should print, and str() should return, the following rectangle description: [Rectangle] <width>/<height>
---

> ### 10.Square #1 mandatory
Write a class Square that inherits from Rectangle (9-rectangle.py):

Instantiation with size: def __init__(self, size)::
size must be private. No getter or setter
size must be a positive integer, validated by integer_validator
the area() method must be implemented
---

> ### 11. Square #2 mandatory
Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).

Instantiation with size: def __init__(self, size)::
size must be private. No getter or setter
size must be a positive integer, validated by integer_validator
the area() method must be implemented
print() should print, and str() should return, the square description: [Square] <width>/<height>
---



> ### ______


> Christian Nazareno
### | [twitter](https://twitter.com/Camilo06134257) | [linkedin](https://www.linkedin.com/in/christian-nazareno-8441b81a1/) | [mail](1464@holbertonschool.com) | [github](https://github.com/ch-canaza)  |
