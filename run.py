'''
    This is a file that configures how your server runs
    You may eventually wish to have your own explicit config file
    that this reads from.

    For now this should be sufficient.
'''

#-----------------------------------------------------------------------------

import sys
from bottle import run

from config import CONFIG
from database.database import load_database, save_database
from server_adapter import SSLCherootAdapter

import controller
import model
import view

#-----------------------------------------------------------------------------

def run_server():    
    '''
        run_server
        Runs a bottle server
    '''
    load_database()
    run(host=CONFIG["HOST"], port=CONFIG["PORT"], server=SSLCherootAdapter, debug=CONFIG["DEBUG"])
    save_database()

#-----------------------------------------------------------------------------

# What commands can be run with this python file

command_list = {
    'server'       : run_server
}

def run_commands(args):
    '''
        run_commands
        Parses arguments as commands and runs them if they match the command list

        :: args :: Command line arguments passed to this function
    '''
    commands = args[1:]

    # Default command
    if len(commands) == 0:
        commands = CONFIG["DEFAULT_COMMANDS"]

    for command in commands:
        if command in command_list:
            command_list[command]()
        else:
            print(f"Command '{command}' not found")

#-----------------------------------------------------------------------------

run_commands(sys.argv)
