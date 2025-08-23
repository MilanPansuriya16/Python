
'''
I.   What is functional programming?
     - Functional programming is a programming paradigm where programs are constructed by applying and composing functions. It emphasizes the use of pure functions, immutability, and avoids changing-state and mutable data.

II.  What is modular programming?
     - Modular programming is a software design technique that emphasizes separating the functionality of a program into independent, interchangeable modules. Each module contains everything necessary to execute only one aspect of the desired functionality.

III. Why do we need functions?
     - Functions help in breaking down complex problems into smaller, manageable pieces. They promote code reuse, improve readability, and make debugging and testing easier.

IV.  How function works?
     - A function is defined once and can be called multiple times. When called, it executes the code inside its block and can return a value. Functions can accept parameters and return results.

V.   1 Programming question?
     - Example: Write a function to calculate the factorial of a number.
       ```python
       def factorial(n):
           if n == 0 or n == 1:
               return 1
           else:
               return n * factorial(n - 1) 
       print(factorial(5))  # Output: 120
       ```

'''