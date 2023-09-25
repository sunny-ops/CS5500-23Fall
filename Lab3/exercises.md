# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!

## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
   - It is a concrete class. Because the MObject class does not have any abstract methods, and it also does not use the abstractmethod decorator from the abc module.
2. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
   - It is a destructor. Defining a `__del__` method can slow down the garbage collection process, especially in a cyclic reference situation.
3. What class does Texture inherit from?
   - I inherits from Image.
4. What methods and attributes does the Texture class inherit from 'Image'?
   - Attributes: m_width, m_height, m_colorChannels, m_Pixels
     - Methods: **init**, getWidth, getHeight, getPixelColorR, getPixels, set PixelsToRandomValue.
5. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
   - It has a "has-a" relationship. An image is a 2D array of pixels, while a texture often refers to an image that gets mapped onto a 3D model.
6. I did not declare a constructor for Texture. Does Python automatically create constructors for us?
   - Yes, Python provides default constructors and destructors for classes if they are not explicitly defined.

## Task 2 - Singleton

1. Refactor the singleton.py file such that:

- The first time the logger is constructed, it will print out:
  - `Logger created exactly once`
- If the logger is already initialized, it will print: - `logger already created`
  Note: You do not 'have' a constructor, but you construct the object in the _instance_ member function where you will create an object.  
  Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singleton's in Python thread safe? Why or why not?


   Singleton is not safe in Python thread.
   The typical Singleton pattern in Python checks if an instance already exists, and if not, creating one. When you have multiple threads, threads could simultaneously determine that an instance doesn't exist and then proceed to create an instance, leading to multiple instances, thereby violating the Singleton principle.

_edit the code directly_
