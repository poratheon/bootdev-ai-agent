import os

def get_files_info(working_directory, directory=None):
    working_path = os.path.abspath(os.path.expanduser(working_directory))
    #print(f"The path is:  {working_path}")
    full_path = os.path.join(working_path, directory)
    #print(f"The full path (path + directory) is:  {full_path}")
    # print(f"The full path is:  {full_path}")
    if not full_path.startswith(working_path + os.sep) and full_path != working_path:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'

    try:
        files = os.listdir(full_path)
        results = []
    # print(f"The contents of this directory are:")
        for file in files:
            full_file_path = os.path.join(full_path, file)
            if os.path.isfile(full_file_path):
                size = os.path.getsize(full_file_path)
                results.append(f"- {file}: file_size={size} bytes, is_dir=False")
            elif os.path.isdir(full_file_path):
                size = os.path.getsize(full_file_path)
                results.append(f"- {file}: file_size={size} bytes, is_dir=True")
            else:
                print(f"No condition met for {file}")
        return "\n".join(results)

    except Exception as e:
        return f"Error: {str(e)}"


#print(get_files_info("/Users/stephen.porath@siemens.com/", "OneDrive - Siemens AG"))
