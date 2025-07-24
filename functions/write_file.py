import os
from google.genai import types
def write_file(working_directory, file_path, content):
    desired_path = os.path.join(os.path.abspath(working_directory),file_path)
    is_in_workingpath = os.path.abspath(desired_path).startswith(os.path.abspath(working_directory))

    if not is_in_workingpath:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(os.path.dirname(desired_path)):
        try:
            os.makedirs(os.path.dirname(desired_path))
        except Exception as e:
            return f"Error: {e}"
    try:
        with open(desired_path, "w") as f:
            f.write(content)
    except Exception as e:
        return f"Error: {e}"
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

schema_write_file = types.FunctionDeclaration(
        name="write_file",
        description="Writes the provided contents to the desired file, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "content":types.Schema(
                    type=types.Type.STRING,
                    description="Contents to write to the file"
                ),
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="Filepath to the file to write the provided contents at, relative to the working directory. If it does not exists create it",
                ),
                
            },
        ),
    )