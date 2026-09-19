#run_python_file

import os
#import time
import subprocess

from config import RUN_CMD

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str | None:
    try:
        bort = os.path.abspath(working_directory)
        #fort = os.path.abspath(file_path)
        borf = os.path.join(bort, file_path)
        frob = os.path.normpath(borf)
        dirok = os.path.commonpath([bort, frob]) == bort
        if dirok == False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory.'
        if os.path.isfile(frob) == False:
            return f'Error: Cannot execute "{file_path}" does not exist or is not a regular file.'
        if file_path[-3:] != ".py":
            return f'Error: "{file_path}" is not a Python file'
        else:
            print(f'Success: "{file_path}" is within the working directory.')
    except:
        return f'Error: Got lost looking for "{file_path}"'
    
    try:
        command: list[str] = [RUN_CMD, frob]  
        if args:
            command.extend(args)
        #subprocess.run(*command)
        #go = time.time()
        result = subprocess.run([*command], capture_output=True, text=True, timeout=30)
        #halt = time.time()
        #elapsed = halt - go
        #print(elapsed)
    except:
        return f'Error: something wen wrong with {command}'
    retStr = ""
    if result.returncode != 0:
        retStr += f'"Process exited with code {result.returncode}"\n'
    if not result.stderr and not result.stdout:
        retStr += f'"No output produced."\n'
    else:
        retStr += f'STDOUT: {result.stdout}\nSTDERR: {result.stderr}\n'
    return retStr


    #time.sleep(30)