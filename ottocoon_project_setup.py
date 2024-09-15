''' This module provides functions for creating a series of project folders. '''
### Otto Coon
#####################################
# Import Modules at the Top
#####################################

# Import moduldes from standand library
# TODO: Import additional modules as needed
import pathlib
### I chose to do this with os as I am more familar with it than pathlib
import os
import time
# Import local modules
# TODO: Change this to import your module and uncomment
import utils_ottocoon as otto
#####################################
# Declare global variables
#####################################

# Create a project path object
project_path = pathlib.Path.cwd()

# Create a project data path object
data_path = project_path.joinpath('data')

# Create the data path if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

#####################################
# Define Function 1. For item in Range: Create a function to generate folders for a given range (e.g., years).
# Pass in an int for the first year
# Pass in an int for the last year
#####################################

def create_folders_for_range(start_year: int, end_year: int) -> None:
    '''
    Create folders for a given range of years.
    
    Arguments:
    start_year -- The starting year of the range (inclusive).
    end_year -- The ending year of the range (inclusive).
    '''
    year=start_year
    shifted_end_year=end_year+1
    while year in range (start_year,shifted_end_year):
        ### Try except to not break if folders already exist
        try:
            os.mkdir(f"Documents\data_fund_02_projects\datafun-02-project-setup\{year}_Coon_Toons_Annual_Report")
        except OSError:
            print(f"{year} file already exists")
        year=year+1
    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}")

    # TODO: Implement the actual folder creation logic

  
#####################################
# Define Function Function 2. For Item in List: Develop a function to create folders from a list of names.
# Pass in a list of folder names 
#####################################

def create_folders_from_list(folder_list: list, to_lowercase: bool=False, remove_spaces: bool =False) -> None:
    ### Create folders for given list
    ### Went back and added remvoe spaces option and lowercase, giving them default values of false.
    # TODO: Add docstring
    if to_lowercase == True:
        folder_list=list(map(lambda x: x.lower(), folder_list))
    if remove_spaces==True:
        folder_list=list(map(lambda x: x.replace(" ",""), folder_list))
    for folder in folder_list:
        ### Try except to not break if folders already exist
        try:
            os.mkdir(f"Documents\data_fund_02_projects\datafun-02-project-setup\{folder}")
        except OSError:
            print(f"{folder} file already exists")


    
    # TODO: Log the function call and its arguments
    print(f"FUNCTION CALLED: create_folders_from_list with folder_list={folder_list}")
    # TODO: Implement this function and remove the temporary pass


  
#####################################
# Define Function 3. List Comprehension: Create a function to create prefixed folders by transforming a list of names and combining each with a prefix (e.g., "data-").
# Pass in a list of folder names
# Pass in a prefix (e.g. 'data-') to add to each
#####################################

def create_prefixed_folders(folder_list: list, prefix: str) -> None:
    # TODO: Implement this function professionally and remove the temporary pass
    ### Create folders for given list and prefix

    for folder in folder_list:
        ### Try except to not break if folders already exist
        try:
            os.mkdir(f"Documents\data_fund_02_projects\datafun-02-project-setup\{prefix}{folder}")
        except OSError:
            print(f"{prefix}{folder} file already exists")


    
    # TODO: Log the function call and its arguments
    print(f"FUNCTION CALLED: create_prefixed_folders with folder_list={folder_list} and prefix={prefix}")

  

#####################################
# Define Function 4. While Loop: Write a function to create folders periodically (e.g., one folder every 5 seconds).
# Pass in the wait time in seconds
#####################################

def create_folders_periodically(Timer_Duration: int, Timer_interval: int) -> None:
### Use a while loop with an if statement to check to see if the timer has been passed to code this section
    timer: bool=True
    end_time=time.time()+Timer_Duration
    while timer:
        if time.time()>end_time:
            timer=False
        else:
            try:
                os.mkdir(f"Documents\data_fund_02_projects\datafun-02-project-setup\{time.strftime("%Y%m%d-%H%M%S")}")
            except OSError:
                print("Current time file file already exists")
            time.sleep(Timer_interval)
    print(f"FUNCTION CALLED:  create_folders_periodically with Timer_Duration of {Timer_Duration} and Timer_interval of {Timer_interval}")      


  
#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    # Print get_byline() from imported module
    # TODO: Change this to use your module function and uncomment
    print(f"Byline: {otto.get_byline()}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs:int = 5  # duration in seconds
    Time_to_create_files_sec=10
    create_folders_periodically(Time_to_create_files_sec,duration_secs)

    # TODO: Add options e.g., to force lowercase and remove spaces 
    # to one or more of your functions (e.g. function 2) 
    # Call your function and test these options
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    # Uncomment this line after you've added your custom logic
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")


#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()

#TODO: Run this as a script to test that all functions work as intended.
