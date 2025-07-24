import os 
from google.genai import types

def get_files_info(working_directory, directory=None):
    abs_working_path = os.path.abspath(working_directory)
    desired_path = abs_working_path
    if directory is not None:
        desired_path = os.path.join(desired_path,directory)
    is_in_workingpath = os.path.abspath(desired_path).startswith(os.path.abspath(working_directory))

    if not is_in_workingpath:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(desired_path):
        return f'Error: "{directory}" is not a directory'   
    
    def get_contents():
        contents =[]
        for item in os.listdir(desired_path):
            current_file = os.path.join(desired_path,item)
            contents.append(f"- {item}: file_size={os.path.getsize(current_file)} bytes, is_dir={os.path.isdir(current_file)}")
        return "\n".join(contents)
    
    try:
        return get_contents()
    except Exception as e:
        return f"Error: {e}"

schema_get_files_info = types.FunctionDeclaration(
        name="get_files_info",
        description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "directory": types.Schema(
                    type=types.Type.STRING,
                    description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
                ),
            },
        ),
    )