import os

def write_file(working_directory, file_path, content):
    try:
            
        full_path = os.path.join(os.path.abspath(working_directory), file_path)
        abs_path = os.path.abspath(full_path)
        abs_working = os.path.abspath(working_directory)
        abs_working_sep = abs_working + os.sep + file_path

        if not (abs_path.startswith(abs_working_sep) or abs_path == abs_working):
            return f'Error: Cannot write to {file_path} as it is outside the permitted working directory'
        
        if not os.path.exists(abs_working_sep):
            with open(full_path, "w") as f:
                f.write("")
        
        with open(full_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"