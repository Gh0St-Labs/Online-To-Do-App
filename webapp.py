import streamlit as st
import todo_list_functions as func
# the requirements.txt file is the file which is needed by the server to know what are the files to download
# to deploy our website.
# we use pip freeze > requirements.txt to load all the extension files, but in reality, the freeze contains
# all the extension files and we add and store them to a file called requirements.txt. This is a more safer
# way.

def just_add_todo():
    entered_todo = st.session_state['users_todo']
    # so as you can tell, the st.session_state is like recieving the input or text from the key 'users_todo' which is an text input type.
    # once it receives it, it stores it in the entered_todo variable. Session state creates an program in respect of the key given to it in the square
    # brackets. The Syntax is the same as above. First the program will be empty with the variable assigned. Once the user enters the input in the
    # input box, such as our case, the program stores the user's todo to the variable assigned.
    # even if you give a key of an title function, or an write function, the program takes in the value given to the title or write function and stores it
    # in the assigned variable.
    todo_garage.append(entered_todo + '\n')
    func.write_todos('todolist.txt', 'w', todo_garage)
    # if you are wondering, why am I giving in writetodos before readtodos? that's because IT DOSEN'T MATTER. I've given writetodos in a function which
    # does not do anything until the function is called. The function will be called AFTER the readtodos function which is right below.


todo_garage = func.read_todos('todolist.txt')

st.title("📜 Store all your To-Dos in one place with TO-DO HUT!")
st.write("Add To-Dos and complete them by checking the box. Time to increase your Productivity! ")
# st.subheader() ->> this creates a subheading with the text you give inside the brackets
# st.write() ->> this creates a simple line of text that you give in.
# st.checkbox ->> creates a check box next to the text that you give in.
# label creates a small text above the input box just for a silly reference.
# the order of adding the element matters here. Such as in HTML.

for the_index, todo in enumerate(todo_garage):
    checkbox = st.checkbox(todo.capitalize(), key=todo)
    # the reason for the key to be todo itself is because each and every key should be different
    # in order to remove. So each key is the Todo itself.
    # now the values in each of todos are false. If you now check the box, it becomes true. THAT'S HOW THIS WORKS.
    if checkbox: # you can just give in check box, because it is defaultly true
        todo_garage.pop(the_index) # this removes the index of the checked checkbox
        func.write_todos('todolist.txt', 'w', todo_garage)
        del st.session_state[todo] # this is to delete the todo from session state.
        st.experimental_rerun() # this is always mandatory while using checkboxes. This maintains the code and runs it with no error

todo_input = st.text_input(placeholder='Add To-Do here...', label='', on_change=just_add_todo, key='users_todo')
