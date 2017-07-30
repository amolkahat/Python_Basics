file_name = "my_tasks.txt"

f = open(file_name, 'w')
f.write("1. Attend the meetup")
f.write("2. Go home and get sleep")
f.write("3. Make sure you had lunch before going to bed.")
f.close()

print("File written successfully")
