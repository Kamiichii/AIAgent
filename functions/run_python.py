import os
import subprocess
from google.genai import types
def run_python_file(working_directory, file_path):
    desired_path = os.path.join(os.path.abspath(working_directory),file_path)
    is_in_workingpath = os.path.abspath(desired_path).startswith(os.path.abspath(working_directory))

    if not is_in_workingpath:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(desired_path):
        return f'Error: File "{file_path}" not found.'
    if not desired_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        output_parts = []
        result = subprocess.run(["python3",file_path],
                                timeout=30, 
                                cwd=working_directory,
                                capture_output=True,
                                text=True)
        if result.stdout:
            output_parts.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output_parts.append(f"STDERR:\n{result.stderr}")
        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")
        if output_parts:
            return "\n".join(output_parts)
        else:
            return "No output produced."
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python = types.FunctionDeclaration(
        name="run_python_file",
        description="It runs the python file it is provided and prints its stdout,stderr and return code, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The filepath to the python executeable, relative to the working directory.",
                ),
            },
        ),
    )