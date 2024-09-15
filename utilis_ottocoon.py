''' ITERATION 5 add stats
Module: Coons Toons- Reusable Module for My Data Analytics Projects
This tool shows the key statistics for the client satisfaction and IMBD scores for a film by the company Coons Toons.

This module provides a simple, reusable foundation for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

Process:

We don't write code from top to bottom; instead, we often write it from the outside in.
Here's what a first draft of my utils_case.py might look like:

1. I start with this docstring at the very beginning.
   I use it to clarify the purpose of my Python file and organize my thoughts.
   
2. I'll declare a global variable for my byline string and just set it to some simple text.

3. I'll declare a main() function for my module. When I run this script, I can use main() to test my byline.

4. I'll add the boilerplate conditional execution code so I only run the main() function when 
   this script is executed directly (but not when I import it into another file).

I'll test it in an online interpreter to ensure this version runs correctly before continuing.
'''
import statistics as stat
#####################################
# Declare a global variable named byline.
#####################################

sequal_number: int=4
is_animated: bool=True
theaters: list=["AMC","Cinamark"]
imbd: list =[6.7,6,7,8.5]
client_sat: list= [4,7,10]


min_sat: float = min(client_sat)
max_sat: float = max(client_sat)
sat_stdev: float = stat.stdev(client_sat)
mean_sat: float = stat.mean(client_sat)

min_imbd: float = min(imbd)
max_imbd: float = max(imbd)
imbd_stdev: float = stat.stdev(imbd)
mean_imbd: float = stat.mean(imbd)

byline: str = f"""
The following are the key statistics for the client satisfaction: 
Min:{min_sat}, Max:{max_sat}, Standard Devation{sat_stdev}, Mean:{mean_sat}
The following are the key statistics for IMBD scores: 
Min:{min_imbd}, Max:{max_imbd}, Standard Devation{imbd_stdev}, Mean:{mean_imbd}
"""

#####################################
# Define a main() function for this module.
#####################################

# Create a function named main.
# A function is a block of code that performs a specific task.
# This function will simply print the byline to the console.
# Add a type hint to indicate that this function doesn't return anything when called 
# (that is, it has a Python type of None).
# It doesn't need any additional information passed in, 
# so there's nothing needed inside the parentheses.
# Everything afer the colon (:) must be indented (usually 4 spaces)
#return byline in function:
def get_byline()->str: 
   return byline
def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(get_byline())

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()
