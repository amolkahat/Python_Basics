
def print_msg(msg, error="No Error", *kwargs):
    print("Log : "+error+":" + msg)
    print(kwargs)


print_msg("This will be logged","File not found", "1", "12", "213", "32113")
