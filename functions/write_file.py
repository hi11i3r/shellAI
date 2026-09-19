#write_file.py

import os

def write_file(working_directory: str, file_path: str, content: str) -> str | None:
    try:
        bort = os.path.abspath(working_directory)
        #fort = os.path.abspath(file_path)
        borf = os.path.join(bort, file_path)
        frob = os.path.normpath(borf)
        dirok = os.path.commonpath([bort, frob]) == bort
        if dirok == False:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory.'
        if os.path.isdir(frob) == True:
            return f'Error: Cannot write to "{file_path}" as it is a directory.'
        else:
            print(f'Success: "{file_path}" is within the working directory.')
    except:
        return f'Error: Got lost looking for "{file_path}"'

    try:
        fileToWrite = open(frob, "w")
        fileToWrite.write(content)
        fileToWrite.close()
    except:
        return f'Error: Could not open or write to "{file_path}"'

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
       