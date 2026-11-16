#get_file_content
import os
from config import MAX_CHARS

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Reads the contents of a file in a specified directory relative to the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The name of the file to be read including relative directory"
                }
            },
        },
    },
}

def get_file_content(working_directory: str, file_path: str) -> str | None:

    try:
        bort = os.path.abspath(working_directory)
        #fort = os.path.abspath(file_path)
        borf = os.path.join(bort, file_path)
        frob = os.path.normpath(borf)
        dirok = os.path.commonpath([bort, frob]) == bort
        if dirok == False:
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory or file not found.'
        if os.path.isdir(frob) == True:
            return f'Error: Is not a regular file: "{file_path}"'
        else:
            print(f'Authorised READ access to "{file_path}"')
    except:
        return f'Error: Got lost looking for "{file_path}"'

    try:
        fileToRead = open(frob)
        content = fileToRead.read(10000)
        if fileToRead.read(1):
            content += f'[...File "{file_path}" truncated at {len(content)} characters]' 
            filTrunc = True
            print(f"{file_path} read length: {len(content)}")
            print(f"{file_path} truncated: {filTrunc}")
        fileToRead.close()
    except:
        return f'Error: Could not open "{file_path}"'

    return content
