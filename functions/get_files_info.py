import os

class File:

    def __init__(self, name:str, size, isDir):
        self.name: str = name
        self.size: int = size
        self.isDir: bool = isDir


schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}


def get_files_info(working_directory: str, directory: str) -> str | None:

    try:
        bort = os.path.abspath(working_directory)
        #flort = os.path.abspath(directory)
        borf = os.path.join(bort, directory)
        frob = os.path.normpath(borf)
        dirok = os.path.commonpath([bort, frob]) == bort
        if dirok == False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if os.path.isdir(frob) == False:
            return f'Error: "{directory}" is not a directory'
        else:
            print(f'Authorised for listing of "{directory}"')
    except:
        return f'Error: Got lost looking for "{directory}"'

    try:
        dirList = os.listdir(frob)
        filList: list[File] = []
        for file in dirList:
            ffile = os.path.normpath(os.path.join(frob, file))
            freek = os.stat(ffile)
            #print(freek.st_size)
            filList.append(File(file, freek.st_size, os.path.isdir(ffile)))
    except:
        return f'Error: Not reading "{directory}"'

    retString: str = ""
    for doink in filList:
        retString += f'- {doink.name}: file_size={doink.size}, is_dir={doink.isDir}\n'
    return retString
    