from functions.get_files_info import *

print("Result for current directory:")
result = get_files_info("calculator", ".")
print(result, "\n")

print("Result for 'pkg' directory:")
result = get_files_info("calculator", "pkg")
print(result, "\n")

print("Result for '/bin' directory:")
result = get_files_info("calculator", "/bin")
print(result, "\n")

print("Result for '../' directory:")
result = get_files_info("calculator", "../")
print(result)