# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
  and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
  Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.
Answer: Functions for [lists](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) and [dictionaries](https://docs.python.org/3/library/stdtypes.html#typesmapping) are generally intuitively named, reflecting their core actions. For example, `list.append(x)` clearly signifies adding an item to the end of the list. However, some method names, like `list.pop()`, which both removes and returns an element, might seem ambiguous to those unfamiliar with traditional computer science terminologies. While 'popAndReturn' would be more descriptive, established naming conventions often prioritize historical context and widespread familiarity.

2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

  Answer: dictionary stores key-value pairs, while list stores individual elements

​                 Dictionary access elements via keys, while list access elements via indices

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

 Answer: Yes, a list allows for random access. You can access any element using its index in constant time.

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?

Answer:

Pros: flexibility in development, resuability, and generality

Cons: Complexity in Code, some operations might be less efficient due to handle multiple data types

## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

Answer:  The `requests` module provides functions named after the HTTP methods they represent: `get()`, `post()`, `put()`, `patch()`, `delete()`, etc. These are aptly named as they directly correspond to the HTTP methods they execute.

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

   Answer: Yes, the primary method in the `requests` library that's known to have multiple parameters is `request()`. It's the underlying method that is used for all the HTTP methods (`get()`, `post()`, `put()`, etc.), e.g. requests.request(method, url, **kwargs). 

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  

Answer: (1) good: Flexibitly, Extensibility, Intergration with other functions

​               (2) bad: hard to read, difficult to debug, lack of clarity

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?


Answer: 

1. These are default values for arguments. If the caller doesn't provide a value for that argument, `None` will be the default. This makes certain arguments optional, providing flexibility in how the method can be called. It's a way of saying, "If you don't give me a specific value, I'll assume it's `None` (or whatever the default is)."

2. Yes. Arguments can have any type of default value: numbers, strings, lists, dictionaries, instances of custom classes.

3. By providing default values, you make it easier for users of your API. They might only need to supply a few arguments and rely on defaults for the others. This can simplify common use cases.

   
