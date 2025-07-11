import os
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
