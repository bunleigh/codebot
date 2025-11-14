from functions.get_files_info import *
from functions.get_file_content import *
#print("Result for current directory:")
#result = get_files_info("calculator", ".")
#print(result, "\n")

print("Result for main.py:")
result = get_file_content("calculator", "main.py")
print(result, "\n")

print("Result for pkg/calculator.py:")
result = get_file_content("calculator", "pkg/calculator.py")
print(result, "\n")

print("Result for /bin/cat:")
result = get_file_content("calculator", "/bin/cat")
print(result, "\n")

print("Result for pkg/does_not_exist.py:")
result = get_file_content("calculator", "pkg/does_not_exist.py")
print(result, "\n")