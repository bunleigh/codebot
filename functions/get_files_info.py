import os

def get_files_info(working_directory, directory="."):
    try:
            
        full_path = os.path.join(os.path.abspath(working_directory), directory)
        abs_path = os.path.abspath(full_path)
        abs_working = os.path.abspath(working_directory)
        abs_working_sep = abs_working + os.sep + directory

        if not (abs_path.startswith(abs_working_sep) or abs_path == abs_working):
            return f'Error: Cannot list {directory} as it is outside the permitted working directory'
        
        if not os.path.isdir(abs_path):
            return f'Error: "{directory}" is not a directory'
        
        listing = []

        for file in os.listdir(abs_path):

            abs_file = os.path.abspath(abs_path + os.sep + file)
            is_dir = os.path.isdir(abs_file)
            size = os.path.getsize(abs_file)
            listing.append(f"{file}: file_size={size} bytes, is_dir={is_dir}")
        return "\n".join(listing)
    
    except Exception as e:
        return f"Error: {e}"


def main():
    print("Getting files info...")


main()