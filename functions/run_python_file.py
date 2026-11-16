#run_python_file

import os
#import time
import subprocess

from config import RUN_CMD

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a python file in a specified directory relative to the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "python_file": {
                    "type": "string",
                    "description": "Python file name too execute, including relative path"
                },
                "arguments": {
                    "type": "string",
                    "description": "All arguments, if any, to pass to the python executable"
                }
                
            },
        },
    },
}

def run_python_file(
    working_directory: str, python_file: str, arguments: list[str] | None = None
) -> str | None:
    try:
        bort = os.path.abspath(working_directory)
        #fort = os.path.abspath(python_file)
        borf = os.path.join(bort, python_file)
        frob = os.path.normpath(borf)
        dirok = os.path.commonpath([bort, frob]) == bort
        if dirok == False:
            return f'Error: Cannot execute "{python_file}" as it is outside the permitted working directory.'
        if os.path.isfile(frob) == False:
            return f'Error: Cannot execute "{python_file}" does not exist or is not a regular file.'
        if python_file[-3:] != ".py":
            return f'Error: "{python_file}" is not a Python file'
        else:
            print(f'"{python_file}" authorised for execution.')
    except:
        return f'Error: Got lost looking for "{python_file}"'
    
    try:
        command: list[str] = [RUN_CMD, frob]  
        if arguments:
            command.extend(arguments)
        #subprocess.run(*command)
        #go = time.time()
        result = subprocess.run([*command], capture_output=True, text=True, timeout=30)
        #halt = time.time()
        #elapsed = halt - go
        #print(elapsed)
    except:
        return f'Error: something wen wrong with {command}' # type: ignore
    retStr = ""
    if result.returncode != 0:
        retStr += f'"Process exited with code {result.returncode}"\n'
    if not result.stderr and not result.stdout:
        retStr += f'"No output produced."\n'
    else:
        retStr += f'STDOUT: {result.stdout}\nSTDERR: {result.stderr}\n'
    return retStr


    #time.sleep(30)