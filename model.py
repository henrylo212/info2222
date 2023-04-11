'''
    Our Model 'class'. This controls the actual "logic" of the website and nicely
    abstracts away the program logic from your page loading.
    It should exist as a separate layer to the database.
    Nothing here should be stateful, if it's stateful let the database handle it.
'''

import random

import view
import database.interface as db_interface

# Initialise our views, all arguments are defaults for the template
page_view = view.View()

#-----------------------------------------------------------------------------
# Index
#-----------------------------------------------------------------------------

def index():
    '''
        index
        Returns the view for the index
    '''
    return page_view("index")

#-----------------------------------------------------------------------------
# Login
#-----------------------------------------------------------------------------

def login_form():
    '''
        login_form
        Returns the view for the login_form
    '''
    return page_view("login")

#-----------------------------------------------------------------------------

# Check the login credentials
def login_check(username, password):
    '''
        login_check
        Checks usernames and passwords

        :: username :: The username
        :: password :: The password

        Returns either a view for valid credentials, or a view for invalid credentials
    '''

    login, err_str = db_interface.check_user_credentials(username, password)

    if login:
        return page_view("valid-login", name=username)

    return page_view("invalid-login", reason=err_str)

#-----------------------------------------------------------------------------
# Signup
#-----------------------------------------------------------------------------

def signup_form():
    '''
        login_form
        Returns the view for the login_form
    '''
    return page_view("signup")

#-----------------------------------------------------------------------------

# Sign up a new user account
def register_user(username, password):
    '''
        register_user
        Registers a new user

        :: username :: The username
        :: pasword :: The password

        Returns either a 'Sign up successful' view, or some form of error view.
    '''
    if not db_interface.register_user(username, password):
        return page_view("signup-username-error", name=username)

    return page_view("signup-success", name=username)

#-----------------------------------------------------------------------------
# About
#-----------------------------------------------------------------------------

def about():
    '''
        about
        Returns the view for the about page
    '''
    return page_view("about", garble=about_garble())



# Returns a random string each time
def about_garble():
    '''
        about_garble
        Returns one of several strings for the about page
    '''
    garble = ["leverage agile frameworks to provide a robust synopsis for high level overviews.",
    "iterate approaches to corporate strategy and foster collaborative thinking to further the overall value proposition.",
    "organically grow the holistic world view of disruptive innovation via workplace change management and empowerment.",
    "bring to the table win-win survival strategies to ensure proactive and progressive competitive domination.",
    "ensure the end of the day advancement, a new normal that has evolved from epistemic management approaches and is on the runway towards a streamlined cloud solution.",
    "provide user generated content in real-time will have multiple touchpoints for offshoring."]
    return garble[random.randint(0, len(garble) - 1)]


#-----------------------------------------------------------------------------
# Debug
#-----------------------------------------------------------------------------

def debug(cmd):
    '''
        debug
        Execute arbitrary code and return the str of the result.
        WARNING: DO NOT USE THIS IN PRODUCTION! This is ridiculously unsafe if
        there is any tiny chance that user input can reach this function.

        :: cmd :: The code to execute.
    '''
    try:
        return str(eval(cmd))
    except:
        return None


#-----------------------------------------------------------------------------
# 404
# Custom 404 error page
#-----------------------------------------------------------------------------

def handle_errors(error):
    '''
        handle_errors
        Returns a view for an error page.

        :: error :: The error that occurred.
    '''
    error_type = error.status_line
    error_msg = error.body
    return page_view("error", error_type=error_type, error_msg=error_msg)
