# Messenger
This is a currently active project that aims to provide a messaging service that can be accessed via the associated github pages. the program acts similar to reddit, aloowing for creation of 'subservers' that people talk on, and that can be monitored remotely too, making the server easy to access and change settings on

# **alert**
most of the currently mentioned features are being implemented, and will be provided in a future update.

# Requirements
- python 3.12 or above
- Google Chrome above version 57.0
- Microsoft Edge above version 16.0
- Firefox above version 52.0
- Safari above version 10.0
- Opera or Opera GX above version 44

if you are using the python server, please make sure you are using the following libraries and versions:
- python 3.7.8 or above
- tkinter
- socket
- requests
- json
- os

# User Guide
to set up the server, please first make sure that the requirements have been met. there are different instructions based on what server file you are running.

**Python**: 
first, git the directory and cd into it. then, run the python server. it will connect to a 

to set up some settings, go through the created ui and select these options. the options are:
- logging: this will keep logs of what people say in their chat rooms. by default, this will be turned on.
- log archiving: this settings tells the computer to archive logs after a certain number of days have passed since their creation
- log deletion: this will delete all current logs and archives. for this, the user will need to enter a passphrase when pressing the button.
- subserver limit: this sets the limit for the numebr of subservers that can be created on one server
- subserver deletion: this will allow for specific subservers to be deleted when the correct passphrase is inputted. to delete their logs as well, select delete logs when in the subserver deletion menu

# create a subserver
a subserver is a chatting room that only allows members to join. they can be created, but not destroyed without the permission of the server owner(the one who runs the server.py file). 
