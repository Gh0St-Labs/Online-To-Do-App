FILEPATH = 'todolist.txt'
def read_todos(filename_orpath=FILEPATH): # the syntax for creating a function is hence written. the name should be given with (). Next,
    """Read the Text File and builds a list inside the RAM and returns the items from Todolist."""
# write your code below with indentation.
    with open(filename_orpath, 'r') as file:
        todo_storage = file.readlines()
    return todo_storage

# so you replace something inside the code of a function, and the name of the replaced variable should be inside
# the () in the def line, then while declaring the function inside the main code, we have to give whatever input
# goes inside the replaced variable. refer if_you_dont_understand_funcs.py

def write_todos(filepath,mode,garage):
    """Writes the items inside the Todolist"""
    with open(filepath, mode) as file:
        file.writelines(garage)


# print("hello from function")

# now if you add this print function, and if you run todo_list.py, you will get "hello from function" in the top of
# of the "type add, show, edit or complete". So if you don't want it to print it out, add the print function under
# this code here

if __name__ == "__main__":
    print("Hello from function")
    print("For Dumb Nerds, this is what the if name main does. Of Course I learned it Dumbass! Hahahaha")

# this is an if Statement where the __name__ changes according to the string value. In this case, it is equal to
# a string called main, so this main acts like the int main() in C programming, but in python. So now, when this
# file is imported using import statement, or imported using the from statement, anything above the if statement
# will be imported and made to run, but everything under the if statement is basically just for
# todo_list_functions.py file. If you run this file, you'll get the string "hello from function" and all the items
# inside the file.readlines() function, but when imported, the contents under the if statement will remain as such
# and won't be executed, but everything above will be imported and made to run
# this can be used to test Different outputs.