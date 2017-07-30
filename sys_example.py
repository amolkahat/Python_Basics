import sys
import os

if len(sys.argv) == 1:
    print("Error. Not sufficient arguments")
    sys.exit(1)

if len(sys.argv) >= 1:
    file_name = sys.argv[1]
    if not os.path.isfile(file_name):
        with open(file_name, 'w') as f:
            f.write("Written file")


# Create TODO App.
# options will be 
# -a for add
# -d delete the option.
# -l for display
# -u update a task
# -t Time track
# -h Help page
# -v version
# -tag Tag to the taks like [Office, Home, Sport]
# IMPROVEMENT: Need to replace sys module with argparse.

# https://etherpad.openstack.org/p/python_todo
# https://github.com/amolkahat/Python_Basics
# https://pymbook.readthedocs.io












