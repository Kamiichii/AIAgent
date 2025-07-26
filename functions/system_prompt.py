from google.genai import types
from .get_files_info import schema_get_files_info
from .get_file_content import schema_get_files_content
from .run_python import schema_run_python
from .write_file import schema_write_file

SYSTEM_PROMPT = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.

You are mostly working in the calculator directory
"""
available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_files_content,
            schema_run_python,
            schema_write_file

              ]
    )