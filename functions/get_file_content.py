import os
from .config import CHARACTER_LIMIT
def get_file_content(working_directory, file_path):
    desired_path = os.path.join(os.path.abspath(working_directory),file_path)
    is_in_workingpath = os.path.abspath(desired_path).startswith(os.path.abspath(working_directory))


    if not is_in_workingpath:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(desired_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(desired_path, "r") as f:
             
            file_content_string = f.read(CHARACTER_LIMIT + 1)  # Read one extra
            if len(file_content_string) > CHARACTER_LIMIT:           
                file_content_string = file_content_string[:CHARACTER_LIMIT]
                return f'{file_content_string}[...File "{file_path}" truncated at {CHARACTER_LIMIT} characters]'
            return file_content_string
    except Exception as e:
        return f"Error: {e}"
            
           
             
        

