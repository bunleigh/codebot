from functions.get_files_info import *
from functions.get_file_content import *
from functions.write_file import *
from functions.run_python_file import *

print("Result for main.py:")
result = run_python_file("calculator", "main.py")
print(result, "\n")

print("Result for main.py, [3 + 5]:")
result = run_python_file("calculator", "main.py", ["3 + 5"])
print(result, "\n")

print("Result for tests.py")
result = run_python_file("calculator", "tests.py")
print(result, "\n")

print("Result for ../main.py")
result = run_python_file("calculator", "../main.py")
print(result, "\n")

print("Result for nonexistant.py")
result = run_python_file("calculator", "nonexistent.py")
print(result, "\n")

print("Result for lorem.txt")
result = run_python_file("calculator", "lorem.txt")
print(result)