import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    try:
            
        full_path = os.path.join(os.path.abspath(working_directory), file_path)
        abs_path = os.path.abspath(full_path)
        abs_working = os.path.abspath(working_directory)
        abs_working_sep = abs_working + os.sep + file_path
        print(abs_working_sep)

        if not (abs_path.startswith(abs_working_sep) or abs_path == abs_working):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.exists(abs_working_sep):
            return f'Error: File "{file_path}" not found.'
        
        if not abs_working_sep.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'
        
        completed_process = subprocess.run(
            ["python", abs_working_sep, *args],
            capture_output=True,
            text=True,
            timeout=30,
            check=True
        )
        print(f'STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}')

        output = []
        if completed_process.stdout:
            output.append(f"STDOUT:\n{completed_process.stdout}")
        if completed_process.stderr:
            output.append(f"STDERR:\n{completed_process.stderr}")
        if completed_process.returncode != 0:
            output.append(f"Process exited with code {completed_process.returncode}")

        if output:
            return "\n".join(output)
        else:
            return "No output produced."

    
    except Exception as e:
        return f"Error: executing Python file: {e}"
    