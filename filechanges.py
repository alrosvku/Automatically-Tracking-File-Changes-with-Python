### Deliverable ###
# The deliverable is a Python file (preferably called filechanges.py) 
# that must:
# - contain the source code of all the functions that will 
# connect to the SQLite instance and database, which will be used 
# to track file changes.

# Upload a link to your deliverable in the Submit Your Work section 
# and click submit. After submitting, the Author’s solution and peer 
# solutions will appear on the page for you to examine.


import sqlite3

# Function that creates the SQLite instance
def create_instance():
    conn = sqlite3.connect("datafile.db")
    cursor = conn.cursor()

