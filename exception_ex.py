i = 10
try:
    j = i / 0
    print(j)
except Exception as e:
    print(e)
    print("Error.")
finally:
    print("Finally executed")
