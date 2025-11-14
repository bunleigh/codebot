import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:

        full_path = os.path.join(os.path.abspath(working_directory), file_path)
        abs_path = os.path.abspath(full_path)
        abs_working = os.path.abspath(working_directory)
        abs_working_sep = abs_working + os.sep + file_path
        print(full_path)

        if not (abs_path.startswith(abs_working_sep) or abs_path == abs_working):
            return f'Error: Cannot read {file_path} as it is outside the permitted working directory'
        
        if not os.path.isfile(abs_working_sep):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(full_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            return file_content_string

    except Exception as e:
        return f"Error: {e}"