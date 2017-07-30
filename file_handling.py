file_name = "my_tasks.txt"

with open(file_name, 'w') as f:
    f.write("1. Attend the meetup")
    f.write("2. Go home and get sleep")
    f.write("3. Make sure you had lunch before going to bed.")

print("File written successfully")
